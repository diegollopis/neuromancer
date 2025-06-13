"""
Git operations configuration settings.
"""

# Operation timing settings
GIT_OPERATIONS_DELAY = 1.0  # Time between operations in seconds

# Git command settings
GIT_COMMANDS = {
    'add': ['git', 'add'],
    'commit': ['git', 'commit', '-m'],
    'push': ['git', 'push'],
    'status': ['git', 'status'],
    'fetch': ['git', 'fetch', '--dry-run'],
    'push_dry_run': ['git', 'push', '--dry-run'],
    'get_branch': ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
    'get_remote': ['git', 'config', '--get', 'remote.origin.url'],
    'list_modified': ['git', 'ls-files', '-m'],
    'list_untracked': ['git', 'ls-files', '--others', '--exclude-standard']
} 