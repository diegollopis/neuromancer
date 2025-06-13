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

# Git Environment Settings
INTERNET_CHECK_URL = 'https://www.google.com'
INTERNET_CHECK_TIMEOUT = 5  # Timeout in seconds

# Error Messages
ERROR_MESSAGES = {
    'insufficient_args': {
        'message': 'Insufficient arguments',
        'details': 'Usage: python app.py <commit_type> <message>\nExample: python app.py feat add new feature',
        'suggestion': 'Use \'python app.py help\' to see available commit types.'
    },
    'no_commit_message': {
        'message': 'Commit message not provided',
        'details': 'Usage: python app.py <commit_type> <message>',
        'suggestion': 'Provide a descriptive message for the commit'
    },
    'invalid_commit_type': {
        'message': 'Invalid commit type: {commit_type}',
        'details': 'Valid types: {valid_types}',
        'suggestion': 'Use \'python app.py help\' to see valid types.'
    },
    'no_internet': {
        'message': 'No internet connection',
        'suggestion': 'Check your internet connection and try again.'
    },
    'no_remote': {
        'message': 'Remote repository not configured',
        'details': 'Use \'git remote add origin <url>\' to configure the remote repository.',
        'suggestion': 'Configure the remote repository with \'git remote add origin <url>\''
    },
    'no_permission': {
        'message': 'No permission to access repository',
        'details': 'Your credentials do not have permission to access this repository',
        'suggestion': 'Check your credentials and access permissions'
    },
    'repo_not_found': {
        'message': 'Repository not found',
        'details': 'The remote repository does not exist or is not accessible',
        'suggestion': 'Check if the repository URL is correct'
    },
    'no_changes': {
        'message': 'No changes to commit',
        'suggestion': 'Make some changes to the files before trying to commit.'
    }
} 