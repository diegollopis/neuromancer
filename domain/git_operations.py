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
    
    def add_files(self):
        """
        Adds files to the staging area.
        
        Raises:
            GitOperationError: If the add operation fails
        """
        try:
            self.repo.execute_git_command(GIT_COMMANDS['add'] + ['.'])
            print(f'\n✅ git add done!\n')
        except Exception as e:
            raise GitOperationError(
                operation="add",
                error=str(e),
                details="Error adding files to staging"
            ) from e
    
    def commit(self, message: str):
        """
        Creates a commit with the staged changes.
        
        Args:
            message: Commit message
        
        Raises:
            GitOperationError: If the commit operation fails
        """
        try:
            self.repo.execute_git_command(GIT_COMMANDS['commit'] + [message])
            print(f'\n✅ git commit done!\n')
        except Exception as e:
            raise GitOperationError(
                operation="commit",
                error=str(e),
                details=f"Error creating commit with message: {message}"
            ) from e
    
    def push(self):
        """
        Pushes commits to the remote repository.
        
        Raises:
            GitOperationError: If the push operation fails
        """
        try:
            current_branch = self.repo.get_current_branch()
            self.repo.execute_git_command(GIT_COMMANDS['push'] + ['origin', current_branch])
            print(f'\n✅ git push done!\n')
        except Exception as e:
            raise GitOperationError(
                operation="push",
                error=str(e),
                details=f"Error pushing to branch {current_branch}"
            ) from e
    
    def status(self):
        """
        Shows the current status of the repository.
        
        Raises:
            GitOperationError: If there is an error getting the status
        """
        try:
            self.repo.execute_git_command(GIT_COMMANDS['status'])
            print(f'\n✅ git status done!\n')
        except Exception as e:
            raise GitOperationError(
                operation="status",
                error=str(e),
                details="Error getting repository status"
            ) from e 