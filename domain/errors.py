"""
Error handling module for Git operations.
"""

class GitError(Exception):
    """Base class for Git-related errors."""
    
    def __init__(self, message: str):
        """
        Initialize a Git error.
        
        Args:
            message: Clear and direct error message
        """
        self.message = message
        super().__init__(message)
    
    @classmethod
    def invalid_args(cls, details: str = None, suggestion: str = None) -> 'GitError':
        """Create an error for invalid arguments."""
        if details and suggestion:
            return cls(f"Invalid arguments: {details}.\n{suggestion}")
        return cls("Invalid arguments")
    
    @classmethod
    def operation_failed(cls, operation: str, error: str, details: str = None) -> 'GitError':
        """Create an error for failed Git operations."""
        return cls(f"Git operation '{operation}' failed.\n{error}")
    
    @classmethod
    def internet_connection(cls) -> 'GitError':
        """Create an error for internet connection issues."""
        return cls("No internet connection.\nCheck your connection")
    
    @classmethod
    def git_not_installed(cls) -> 'GitError':
        """Create an error when Git is not installed."""
        return cls("Git not installed.\nInstall Git to continue")
    
    @classmethod
    def not_git_repo(cls) -> 'GitError':
        """Create an error when current directory is not a Git repository."""
        return cls("Not a Git repository.\nRun 'git init' to start")
    
    @classmethod
    def no_remote(cls) -> 'GitError':
        """Create an error when no remote repository is configured."""
        return cls("No remote repository.\nConfigure with 'git remote add'")
    
    @classmethod
    def auth_failed(cls) -> 'GitError':
        """Create an error for authentication failures."""
        return cls("Authentication failed.\nCheck your credentials")
    
    @classmethod
    def push_failed(cls) -> 'GitError':
        """Create an error for push failures."""
        return cls("Push failed.\nCheck your connection and try again")
    
    @classmethod
    def commit_failed(cls) -> 'GitError':
        """Create an error for commit failures."""
        return cls("Commit failed.\nCheck if there are changes to commit")
    
    @classmethod
    def add_failed(cls) -> 'GitError':
        """Create an error for add failures."""
        return cls("Add failed.\nCheck if there are files to add")
    
    @classmethod
    def repo_not_found(cls) -> 'GitError':
        """Create an error for repository not found."""
        return cls("Repository not found.\nCheck the repository URL")
    
    @classmethod
    def no_changes(cls) -> 'GitError':
        """Create an error for no changes to commit."""
        return cls("No changes to commit.\nMake some changes first")
    
    def __str__(self) -> str:
        """Return the error message."""
        return f"❌ {self.message}" 