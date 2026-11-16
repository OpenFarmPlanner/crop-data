"""Regression checks for translation replacement semantics and catalogue identity."""
import copy
import csv
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('planner', Path(__file__).resolve().parents[1] / 'scripts/plan_species_translations.py')
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


class TranslationPlanTests(unittest.TestCase):
    def setUp(self):
        self.rows = [dict(
            german_name='Test crop', scientific_name='Testus cropus', language_code=language,
            common_name=f'Name {language}', synonyms=['New alias'], status='reviewed',
            sources=['https://example.org/taxon'], candidates=[], note='Identity checked',
        ) for language in planner.LANGUAGES]
        self.species = dict(
            id=1, name='Existing identity', scientific_name='Testus cropus', status='published',
            translations=[
                dict(language_code='de', common_name='Test crop', synonyms=['German alias'], regional_names={}),
                dict(language_code='en', common_name='English name', synonyms=['English alias'], regional_names={}),
                dict(language_code='it', common_name='Old name', synonyms=['Existing alias'], regional_names={'austria': 'Existing regional name'}),
            ],
        )

    def plan(self, **kwargs):
        return planner.build_plan(self.rows, [self.species], kwargs.get('enabled', ['it', 'pt', 'nl']))

    def test_patch_preserves_aliases_regions_and_omitted_languages(self):
        original = copy.deepcopy(self.species)
        plan = self.plan(enabled=['it'])
        changes = plan['patches'][0]['patch']['translations']
        self.assertEqual(changes, [dict(
            language_code='it', common_name='Name it',
            synonyms=['Existing alias', 'New alias'], regional_names={'austria': 'Existing regional name'},
        )])
        self.assertEqual(plan['patches'][0]['before'], original)
        self.assertEqual(self.species, original)
        self.assertEqual(set(plan['patches'][0]['patch']), {'translations'})

    def test_repeat_run_has_no_changes_or_duplicate_aliases(self):
        plan = self.plan()
        changes = {t['language_code']: t for t in plan['patches'][0]['patch']['translations']}
        current = {t['language_code']: t for t in self.species['translations']}
        current.update(changes)
        self.species['translations'] = list(current.values())
        repeated = self.plan()
        self.assertEqual(repeated['patches'], [])
        self.assertEqual(repeated['unchanged_translations'], 3)

    def test_unresolved_candidates_never_become_payload(self):
        self.rows[0].update(status='unresolved', common_name='', synonyms=[], candidates=['Unverified alias'])
        plan = self.plan()
        self.assertEqual(len(plan['unresolved']), 1)
        self.assertNotIn('it', [t['language_code'] for t in plan['patches'][0]['patch']['translations']])

    def test_disabled_languages_never_become_payload(self):
        self.assertEqual([t['language_code'] for t in self.plan(enabled=['pt'])['patches'][0]['patch']['translations']], ['pt'])
        with self.assertRaises(ValueError):
            self.plan(enabled=[])
        with self.assertRaises(ValueError):
            self.plan(enabled=['de'])

    def test_added_removed_or_renamed_identity_stops_planning(self):
        for field, value in [('scientific_name', 'Changed identity'), ('status', 'proposed')]:
            with self.subTest(field=field):
                changed = copy.deepcopy(self.species)
                changed[field] = value
                with self.assertRaises(ValueError):
                    planner.build_plan(self.rows, [changed], ['it'])
        changed = copy.deepcopy(self.species)
        changed['translations'][0]['common_name'] = 'Different use form'
        with self.assertRaises(ValueError):
            planner.build_plan(self.rows, [changed], ['it'])
        with self.assertRaises(ValueError):
            planner.build_plan(self.rows, [], ['it'])
        extra = copy.deepcopy(self.species)
        extra['id'] = 2
        extra['translations'][0]['common_name'] = 'New crop'
        with self.assertRaises(ValueError):
            planner.build_plan(self.rows, [self.species, extra], ['it'])

    def test_identical_botanical_names_are_not_merged(self):
        extra = copy.deepcopy(self.species)
        extra['id'] = 2
        extra['translations'] = [dict(language_code='de', common_name='Different use form')]
        rows = copy.deepcopy(self.rows)
        for row in self.rows:
            rows.append(dict(row, german_name='Different use form', common_name=row['common_name']+' specific'))
        plan = planner.build_plan(rows, [self.species, extra], ['pt'])
        self.assertEqual(len(plan['patches']), 2)
        self.assertEqual({p['id'] for p in plan['patches']}, {1, 2})

    def test_live_common_name_collision_blocks_plan(self):
        extra = copy.deepcopy(self.species)
        extra['id'] = 2
        extra['translations'][0]['common_name'] = 'Different crop'
        rows = copy.deepcopy(self.rows)
        for row in self.rows:
            rows.append(dict(row, german_name='Different crop', common_name=row['common_name']+' specific'))
        extra['translations'][-1]['common_name'] = 'Name it'
        with self.assertRaises(ValueError):
            planner.build_plan(rows, [self.species, extra], ['it'])

    def test_case_and_unicode_aliases_are_not_duplicated(self):
        self.rows[0]['synonyms'] = ['Éclair']
        self.species['translations'][-1]['synonyms'] = ['E\u0301CLAIR']
        aliases = self.plan(enabled=['it'])['patches'][0]['patch']['translations'][0]['synonyms']
        self.assertEqual(aliases, ['E\u0301CLAIR'])

    def test_public_research_has_complete_language_coverage(self):
        rows = planner.load_research()
        self.assertTrue(rows)
        self.assertEqual(len(rows), planner.coverage(rows)['species'] * 3)
        self.assertTrue(all(r['status'] == 'reviewed' for r in rows))

    def test_research_rejects_writable_unresolved_entries_and_duplicate_names(self):
        for change in ['unresolved-name', 'duplicate-name', 'missing-language']:
            with self.subTest(change=change), tempfile.TemporaryDirectory() as directory:
                rows = copy.deepcopy(self.rows)
                if change == 'unresolved-name':
                    rows[0]['status'] = 'unresolved'
                elif change == 'duplicate-name':
                    rows += [dict(r, german_name='Other crop') for r in self.rows]
                else:
                    rows.pop()
                path = Path(directory) / 'research.csv'
                with path.open('w', newline='') as stream:
                    writer = csv.DictWriter(stream, fieldnames=sorted(planner.FIELDS))
                    writer.writeheader()
                    for row in rows:
                        writer.writerow({k: json.dumps(v) if isinstance(v, list) else v for k, v in row.items()})
                with self.assertRaises(ValueError):
                    planner.load_research(path)


if __name__ == '__main__':
    unittest.main()
