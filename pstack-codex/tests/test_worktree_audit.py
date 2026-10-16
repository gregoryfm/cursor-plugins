import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

PLUGIN = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('git') and shutil.which('jq'), 'git and jq are required by the audit')
class WorktreeAuditTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        self.worktree = self.root / 'checkout'
        self.git('init', '-b', 'main')
        (self.repo / 'file.txt').write_text('committed\n')
        self.git('add', 'file.txt')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-m', 'fixture')
        self.git('worktree', 'add', '-b', 'job', str(self.worktree))
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        for name, content in {'origin': '#!/bin/sh\nexit 1\n', 'gh': '#!/bin/sh\nprintf \'[{"number":1,"state":"MERGED","headRefName":"job"}]\\n\'\n'}.items():
            script = self.bin / name
            script.write_text(content)
            script.chmod(0o700)
        self.home = self.root / 'codex'
        (self.home / 'sessions').mkdir(parents=True)

    def git(self, *arguments):
        return subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'commit.gpgsign=false', *arguments], cwd=self.repo, check=True, capture_output=True, text=True)

    def history(self, modified):
        path = self.home / 'sessions/session.jsonl'
        path.write_text(json.dumps({'type': 'session_meta', 'payload': {'id': 'session', 'cwd': str(self.worktree)}}) + '\n')
        os.utime(path, (modified, modified))

    def bucket(self):
        script = PLUGIN / 'skills/poteto-mode/scripts/worktree-audit.sh'
        result = subprocess.run(['bash', str(script), '-b', 'main', str(self.repo)], text=True, capture_output=True, env={**os.environ, 'PATH': str(self.bin) + os.pathsep + os.environ['PATH'], 'CODEX_HOME': str(self.home)})
        self.assertEqual(result.returncode, 0, result.stderr)
        row = next(line.split('\t') for line in result.stdout.splitlines() if line.endswith(str(self.worktree)))
        return row[-2]

    def test_unknown_history_does_not_recommend_pruning(self):
        self.assertEqual(self.bucket(), 'review-no-history')

    def test_recent_history_holds_merged_worktree(self):
        self.history(time.time())
        self.assertEqual(self.bucket(), 'verify-recent-chat')

    def test_old_history_still_requires_usage_confirmation(self):
        self.history(946684800)
        self.assertEqual(self.bucket(), 'review-usage')

    def test_main_checkout_activity_cannot_be_cleared_by_old_worktree_history(self):
        self.history(946684800)
        path = self.home / 'sessions/main.jsonl'
        path.write_text(json.dumps({'type': 'session_meta', 'payload': {'id': 'main', 'cwd': str(self.repo)}}) + '\n' + json.dumps({'type': 'response_item', 'payload': {'type': 'function_call', 'arguments': str(self.worktree / 'file.txt')}}) + '\n')
        self.assertEqual(self.bucket(), 'review-usage')

    def test_tracked_wip_is_held_even_with_old_history(self):
        self.history(946684800)
        (self.worktree / 'file.txt').write_text('uncommitted\n')
        self.assertEqual(self.bucket(), 'hold-wip')


class DecisionLogTest(unittest.TestCase):
    def test_log_records_one_safe_tsv_row_without_losing_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'decisions.tsv'
            script = PLUGIN / 'skills/show-me-your-work/scripts/log.sh'
            result = subprocess.run(['bash', str(script), str(path), 'frame', '=formula\nnext', 'a\treason', 'evidence.txt', 'open'], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = path.read_text().splitlines()
            self.assertEqual(len(rows), 2)
            cells = rows[1].split('\t')
            self.assertEqual(len(cells), 6)
            self.assertTrue(cells[2].startswith("'=formula"))
            self.assertEqual(cells[4], 'evidence.txt')


if __name__ == '__main__':
    unittest.main()
