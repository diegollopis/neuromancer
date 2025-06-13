"""
Configuration package for Neuromancer.
"""

from .commit import (
    COMMIT_MESSAGE_EXAMPLE,
    COMMIT_MESSAGE_TYPES,
    COMMIT_MESSAGE_REFERENCES
)

from .environment import (
    INTERNET_CHECK_URL,
    INTERNET_CHECK_TIMEOUT,
    GIT_REPO_CONFIG
)

from .errors import ERROR_MESSAGES

from .operations import (
    GIT_OPERATIONS_DELAY,
    GIT_COMMANDS
)

__all__ = [
    # Commit settings
    'COMMIT_MESSAGE_EXAMPLE',
    'COMMIT_MESSAGE_TYPES',
    'COMMIT_MESSAGE_REFERENCES',
    
    # Environment settings
    'INTERNET_CHECK_URL',
    'INTERNET_CHECK_TIMEOUT',
    'GIT_REPO_CONFIG',
    
    # Error messages
    'ERROR_MESSAGES',
    
    # Operation settings
    'GIT_OPERATIONS_DELAY',
    'GIT_COMMANDS'
] 