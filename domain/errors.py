from typing import Callable, Any
from functools import wraps

class GitError(Exception):
    """Base class for Git-related errors"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class InternetConnectionError(GitError):
    """Error when there is no internet connection"""
    pass

class AuthorizationError(GitError):
    """Error when there is no repository authorization"""
    pass

class NotGitRepositoryError(GitError):
    """Error when the directory is not a Git repository"""
    pass

class NoChangesError(GitError):
    """Error when there are no changes to commit"""
    pass

class ValidationError(GitError):
    """Error when there are problems with commit arguments"""
    pass

class GitOperationError(GitError):
    """Error when a Git operation fails"""
    pass

def handle_git_errors(func: Callable) -> Callable:
    """Decorator to handle Git errors in a centralized way"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except GitError as e:
            print(f"\n❌ {e.message}\n")
            return None
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}\n")
            return None
    return wrapper 