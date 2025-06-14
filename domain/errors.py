"""
Custom error classes for Git operations.
"""

from typing import Callable, Any, Optional
from functools import wraps
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
        suggestion: Optional[str] = None
    ):
        """
        Initialize the error.
        
        Args:
            message: Main error message
            severity: Error severity level
            details: Additional error details (optional)
            suggestion: Suggestion on how to resolve the error (optional)
        """
        self.message = message
        self.severity = severity
        self.details = details
        self.suggestion = suggestion
        super().__init__(self._format_message())
    
    def _format_message(self) -> str:
        """Format the complete error message."""
        msg = f"\n❌ {self.message}"
        
        if self.details:
            msg += f"\n\nDetails:\n{self.details}"
        
        if self.suggestion:
            msg += f"\n\nSuggestion:\n{self.suggestion}"
        
        return msg
    
    def __str__(self) -> str:
        """Return the formatted error message."""
        return self._format_message()

class InternetConnectionError(GitError):
    """Error when there is no internet connection."""
    def __init__(self, message: str = "No internet connection"):
        super().__init__(
            message=message,
            severity=ErrorSeverity.ERROR,
            suggestion="Check your internet connection and try again."
        )

class AuthorizationError(GitError):
    """Error when there is no authorization to access the repository."""
    def __init__(
        self,
        message: str,
        details: Optional[str] = None,
        suggestion: Optional[str] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.ERROR,
            details=details,
            suggestion=suggestion or "Check your credentials and access permissions."
        )

class NotGitRepositoryError(GitError):
    """Error when the directory is not a Git repository."""
    def __init__(self, path: str):
        super().__init__(
            message=f"The directory '{path}' is not a Git repository",
            severity=ErrorSeverity.ERROR,
            suggestion="Run 'git init' to initialize a Git repository."
        )

class NoChangesError(GitError):
    """Error when there are no changes to commit."""
    def __init__(self, message: str = "No changes to commit"):
        super().__init__(
            message=message,
            severity=ErrorSeverity.WARNING,
            suggestion="Make some changes to the files before trying to commit."
        )

class ValidationError(GitError):
    """Error when there are problems with commit arguments."""
    def __init__(
        self,
        message: str,
        details: Optional[str] = None,
        suggestion: Optional[str] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.ERROR,
            details=details,
            suggestion=suggestion or "Use 'python app.py help' to see available commit types."
        )

class GitOperationError(GitError):
    """Error when a Git operation fails."""
    def __init__(
        self,
        operation: str,
        error: str,
        details: Optional[str] = None
    ):
        super().__init__(
            message=f"Error executing operation '{operation}'",
            severity=ErrorSeverity.ERROR,
            details=f"Error: {error}\n{details if details else ''}",
            suggestion="Check repository status with 'git status'."
        )

def handle_git_errors(func: Callable) -> Callable:
    """
    Decorator to handle Git errors centrally.
    
    This decorator:
    1. Catches GitError exceptions
    2. Formats the error message
    3. Returns None in case of error
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except GitError as e:
            if e.severity == ErrorSeverity.CRITICAL:
                print(f"\n💥 {e.message}")
            elif e.severity == ErrorSeverity.WARNING:
                print(f"\n⚠️ {e.message}")
            else:
                print(str(e))
            return None
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")
            return None
    return wrapper 