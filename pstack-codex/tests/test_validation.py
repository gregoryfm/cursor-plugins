import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PLUGIN = Path(__file__).resolve().parents[1]


class RetentionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        shutil.copytree(PLUGIN, self.repo / 'pstack-codex', ignore=shutil.ignore_patterns('node_modules', '__pycache__'))
        shutil.copytree(PLUGIN.parent / 'pstack', self.repo / 'pstack')
        marketplace = self.repo / '.agents/plugins'
        marketplace.mkdir(parents=True)
        shutil.copy2(PLUGIN.parent / '.agents/plugins/marketplace.json', marketplace)
        self.mapping = self.repo / 'pstack-codex/docs/source-map.json'

    def validate(self):
        return subprocess.run([sys.executable, str(self.repo / 'pstack-codex/scripts/validate.py')], text=True, capture_output=True)

    def test_missing_resource_and_mapping_cannot_pass_together(self):
        relative = 'skills/poteto-mode/scripts/orch/store.ts'
        (self.repo / 'pstack-codex' / relative).unlink()
        value = json.loads(self.mapping.read_text())
        value['files'] = [row for row in value['files'] if row['source'] != relative]
        self.mapping.write_text(json.dumps(value))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('source inventory', result.stderr)

    def test_duplicate_mapping_is_rejected(self):
        value = json.loads(self.mapping.read_text())
        value['files'].append(value['files'][0])
        self.mapping.write_text(json.dumps(value))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('duplicate source', result.stderr)

    def test_changed_cursor_source_fails_hash_check(self):
        source = self.repo / 'pstack/skills/bro/SKILL.md'
        source.write_text(source.read_text() + '\nchanged source\n')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Cursor source changed', result.stderr)


if __name__ == '__main__':
    unittest.main()
