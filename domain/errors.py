"""
Custom error classes for Git operations.
"""

from typing import Optional
from enum import Enum, auto

class ErrorSeverity(Enum):
    """Error severity levels."""
    INFO = auto()      # Informational only
    WARNING = auto()   # Warning, but doesn't prevent operation
    ERROR = auto()     # Error that prevents operation
    CRITICAL = auto()  # Critical error that may affect the system

class GitError(Exception):
    """Base class for Git-related errors."""
    
    def __init__(self, title: str, details: str = None, suggestion: str = None, operation: str = None):
        """
        Initialize a Git error.
        
        Args:
            title: Short error title/description
            details: Detailed error message
            suggestion: Suggestion for fixing the error
            operation: Optional operation that failed
        """
        self.title = title
        self.details = details
        self.suggestion = suggestion
        self.operation = operation
        super().__init__(title)
    
    @classmethod
    def invalid_args(cls, details: str = None, suggestion: str = None) -> 'GitError':
        """Create an error for invalid arguments."""
        return cls(
            title="Invalid arguments",
            details=details,
            suggestion=suggestion
        )
    
    @classmethod
    def operation_failed(cls, operation: str, error: str, details: str = None) -> 'GitError':
        """Create an error for failed Git operations."""
        return cls(
            title=f"Git operation failed: {operation}",
            details=details or error,
            suggestion="Check your Git configuration and try again.",
            operation=operation
        )
    
    @classmethod
    def internet_connection(cls) -> 'GitError':
        """Create an error for internet connection issues."""
        return cls(
            title="Internet connection error",
            details="No internet connection available.",
            suggestion="Check your internet connection and try again."
        )
    
    @classmethod
    def git_not_installed(cls) -> 'GitError':
        """Create an error when Git is not installed."""
        return cls(
            title="Git not installed",
            details="Git is not installed on the system.",
            suggestion="Install Git and try again."
        )
    
    @classmethod
    def not_git_repo(cls) -> 'GitError':
        """Create an error when current directory is not a Git repository."""
        return cls(
            title="Not a Git repository",
            details="Current directory is not a Git repository.",
            suggestion="Run git init to initialize a Git repository."
        )
    
    @classmethod
    def no_remote(cls) -> 'GitError':
        """Create an error when no remote repository is configured."""
        return cls(
            title="No remote repository",
            details="No remote repository configured.",
            suggestion="Configure a remote repository using git remote add."
        )
    
    @classmethod
    def auth_failed(cls) -> 'GitError':
        """Create an error for authentication failures."""
        return cls(
            title="Authentication failed",
            details="Authentication failed with remote repository.",
            suggestion="Check your credentials and try again."
        )
    
    @classmethod
    def push_failed(cls) -> 'GitError':
        """Create an error for push failures."""
        return cls(
            title="Push failed",
            details="Failed to push changes to remote repository.",
            suggestion="Check your connection and try again."
        )
    
    @classmethod
    def commit_failed(cls) -> 'GitError':
        """Create an error for commit failures."""
        return cls(
            title="Commit failed",
            details="Failed to create commit.",
            suggestion="Check if there are changes to commit."
        )
    
    @classmethod
    def add_failed(cls) -> 'GitError':
        """Create an error for add failures."""
        return cls(
            title="Add failed",
            details="Failed to add files to staging.",
            suggestion="Check if there are files to add."
        )

    def __str__(self) -> str:
        """Return the formatted error message."""
        return f"{self.title}\n\nDetails:\n{self.details}\n\nSuggestion:\n{self.suggestion}"

    @classmethod
    def no_permission(cls, branch: Optional[str] = None) -> 'GitError':
        """Creates an error for no permission to access repository."""
        details = f"You don't have permission to push to branch {branch}" if branch else "Your credentials do not have permission to access this repository"
        return cls(
            title="No permission to access repository",
            details=details,
            suggestion="Check your credentials and access permissions"
        )
    
    @classmethod
    def repo_not_found(cls) -> 'GitError':
        """Creates an error for repository not found."""
        return cls(
            title="Repository not found",
            details="The remote repository does not exist or is not accessible",
            suggestion="Check if the repository URL is correct"
        )
    
    @classmethod
    def no_changes(cls) -> 'GitError':
        """Creates an error for no changes to commit."""
        return cls(
            title="No changes to commit",
            suggestion="Make some changes to the files before trying to commit."
        )
    
    @classmethod
    def not_git_repo(cls, path: str) -> 'GitError':
        """Creates an error for directory not being a Git repository."""
        return cls(
            title=f"The directory '{path}' is not a Git repository",
            details="",
            suggestion="Run 'git init' to initialize a Git repository."
        ) 