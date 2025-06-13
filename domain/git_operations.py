from time import sleep
from typing import List, Optional
from .git_repository import GitRepository
from .errors import handle_git_errors, GitOperationError
from config import GIT_OPERATIONS_DELAY, GIT_COMMANDS

class GitOperations:
    """Responsible for performing Git operations."""
    
    def __init__(self, repo: GitRepository, delay: float = GIT_OPERATIONS_DELAY):
        """
        Initialize Git operations.
        
        Args:
            repo: Git repository instance to perform operations
            delay: Time between operations (in seconds)
        """
        self.repo = repo
        self.delay = delay
    
    def add_files(self, files: Optional[List[str]] = None) -> None:
        """
        Adds files to the staging area.
        
        Args:
            files: List of files to add. If None, adds all files
        
        Raises:
            GitOperationError: If the add operation fails
        """
        try:
            if files:
                self.repo.execute_git_command(GIT_COMMANDS['add'] + files)
            else:
                self.repo.execute_git_command(GIT_COMMANDS['add'] + ['.'])
        except Exception as e:
            raise GitOperationError(
                operation="add",
                error=str(e),
                details="Error adding files to staging"
            ) from e
    
    def commit(self, message: str) -> None:
        """
        Creates a commit with the staged changes.
        
        Args:
            message: Commit message
        
        Raises:
            GitOperationError: If the commit operation fails
        """
        try:
            self.repo.execute_git_command(GIT_COMMANDS['commit'] + [message])
        except Exception as e:
            raise GitOperationError(
                operation="commit",
                error=str(e),
                details=f"Error creating commit with message: {message}"
            ) from e
    
    def push(self) -> None:
        """
        Pushes commits to the remote repository.
        
        Raises:
            GitOperationError: If the push operation fails
        """
        try:
            current_branch = self.repo.get_current_branch()
            self.repo.execute_git_command(GIT_COMMANDS['push'] + ['origin', current_branch])
        except Exception as e:
            raise GitOperationError(
                operation="push",
                error=str(e),
                details=f"Error pushing to branch {current_branch}"
            ) from e
    
    def status(self) -> None:
        """
        Shows the current status of the repository.
        
        Raises:
            GitOperationError: If there is an error getting the status
        """
        try:
            self.repo.execute_git_command(GIT_COMMANDS['status'])
        except Exception as e:
            raise GitOperationError(
                operation="status",
                error=str(e),
                details="Error getting repository status"
            ) from e 