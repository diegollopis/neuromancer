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
    
    def __init__(
        self,
        message: str,
        severity: ErrorSeverity = ErrorSeverity.ERROR,
        details: Optional[str] = None,
        suggestion: Optional[str] = None,
        operation: Optional[str] = None
    ):
        """
        Initialize the error.
        
        Args:
            message: Main error message
            severity: Error severity level
            details: Additional error details (optional)
            suggestion: Suggestion on how to resolve the error (optional)
            operation: Name of the operation that failed (optional)
        """
        self.message = message
        self.severity = severity
        self.details = details
        self.suggestion = suggestion
        self.operation = operation
        super().__init__(self._format_message())
    
    def _format_message(self) -> str:
        """Format the complete error message."""
        msg = f"\n❌ {self.message}"
        
        if self.operation:
            msg = f"\n❌ Error executing operation '{self.operation}'"
        
        if self.details:
            msg += f"\n\nDetails:\n{self.details}"
        
        if self.suggestion:
            msg += f"\n\nSuggestion:\n{self.suggestion}"
        
        return msg
    
    def __str__(self) -> str:
        """Return the formatted error message."""
        return self._format_message()

    @classmethod
    def no_internet(cls) -> 'GitError':
        """Creates an error for no internet connection."""
        return cls(
            message="No internet connection",
            severity=ErrorSeverity.ERROR,
            suggestion="Check your internet connection and try again."
        )
    
    @classmethod
    def no_remote(cls) -> 'GitError':
        """Creates an error for no remote repository."""
        return cls(
            message="Remote repository not configured",
            severity=ErrorSeverity.ERROR,
            details="Use 'git remote add origin <url>' to configure the remote repository.",
            suggestion="Configure the remote repository with 'git remote add origin <url>'"
        )
    
    @classmethod
    def no_permission(cls, branch: Optional[str] = None) -> 'GitError':
        """Creates an error for no permission to access repository."""
        details = f"You don't have permission to push to branch {branch}" if branch else "Your credentials do not have permission to access this repository"
        return cls(
            message="No permission to access repository",
            severity=ErrorSeverity.ERROR,
            details=details,
            suggestion="Check your credentials and access permissions"
        )
    
    @classmethod
    def repo_not_found(cls) -> 'GitError':
        """Creates an error for repository not found."""
        return cls(
            message="Repository not found",
            severity=ErrorSeverity.ERROR,
            details="The remote repository does not exist or is not accessible",
            suggestion="Check if the repository URL is correct"
        )
    
    @classmethod
    def no_changes(cls) -> 'GitError':
        """Creates an error for no changes to commit."""
        return cls(
            message="No changes to commit",
            severity=ErrorSeverity.WARNING,
            suggestion="Make some changes to the files before trying to commit."
        )
    
    @classmethod
    def invalid_args(cls, details: str, suggestion: Optional[str] = None) -> 'GitError':
        """Creates an error for invalid arguments."""
        return cls(
            message="Invalid arguments",
            severity=ErrorSeverity.ERROR,
            details=details,
            suggestion=suggestion or "Use 'python app.py help' to see available commit types."
        )
    
    @classmethod
    def operation_failed(cls, operation: str, error: str, details: Optional[str] = None) -> 'GitError':
        """Creates an error for failed Git operation."""
        return cls(
            message=f"Error executing operation '{operation}'",
            severity=ErrorSeverity.ERROR,
            details=f"Error: {error}\n{details if details else ''}",
            suggestion="Check repository status with 'git status'.",
            operation=operation
        )
    
    @classmethod
    def not_git_repo(cls, path: str) -> 'GitError':
        """Creates an error for directory not being a Git repository."""
        return cls(
            message=f"The directory '{path}' is not a Git repository",
            severity=ErrorSeverity.ERROR,
            suggestion="Run 'git init' to initialize a Git repository."
        ) 