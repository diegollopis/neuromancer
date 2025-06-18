"""
Configuration settings for the Neuromancer project.
"""

# Commit Message Settings
COMMIT_MESSAGE_EXAMPLE = '''
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
'''

COMMIT_MESSAGE_TYPES = {
    'feat': '(new feature for the user, not a new feature for build script)',
    'fix': '(bug fix for the user, not a fix to a build script)',
    'docs': '(changes to the documentation)',
    'style': '(formatting, missing semi colons, etc; no production code change)',
    'refactor': '(refactoring production code, eg. renaming a variable)',
    'test': '(adding missing tests, refactoring tests; no production code change)',
    'chore': '(updating grunt tasks etc; no production code change)'
}

COMMIT_MESSAGE_REFERENCES = [
    'www.conventionalcommits.org/',
    'seesparkbox.com/foundry/semantic_commit_messages',
    'karma-runner.github.io/1.0/dev/git-commit-msg.html'
]

# Git Operations Settings
GIT_OPERATIONS_DELAY = 1.0  # Time between operations in seconds

# Git Command Settings
GIT_COMMANDS = {
    'add': ['git', 'add'],
    'commit': ['git', 'commit', '-m'],
    'push': ['git', 'push'],
    'fetch': ['git', 'fetch', '--dry-run'],
    'push_dry_run': ['git', 'push', '--dry-run'],
    'get_branch': ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
    'get_remote': ['git', 'config', '--get', 'remote.origin.url'],
    'list_modified': ['git', 'ls-files', '-m'],
    'list_untracked': ['git', 'ls-files', '--others', '--exclude-standard']
}

# Environment Settings
INTERNET_CHECK_URL = 'https://www.google.com'
INTERNET_CHECK_TIMEOUT = 5  # Timeout in seconds

# Git Repository Settings
GIT_REPO_CONFIG = {
    'remote_name': 'origin',
    'default_branch': 'main'
} 