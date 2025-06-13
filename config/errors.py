"""
Error message configuration settings.
"""

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