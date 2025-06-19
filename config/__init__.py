"""
Configuration package for Neuromancer.
"""

from .settings import (
    # Commit settings
    COMMIT_MESSAGE_EXAMPLE,
    COMMIT_MESSAGE_TYPES,
    COMMIT_MESSAGE_REFERENCES,
    
    # Environment settings
    INTERNET_CHECK_URL,
    INTERNET_CHECK_TIMEOUT,
    GIT_REPO_CONFIG,
    
    # Operation settings
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
    
    # Operation settings
    'GIT_OPERATIONS_DELAY',
    'GIT_COMMANDS'
] 