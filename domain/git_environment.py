from urllib import request
import subprocess
from typing import List
from .git_repository import GitRepository
from .errors import (
    InternetConnectionError,
    AuthorizationError,
    NoChangesError
)

class GitEnvironment:
    """Responsible for verifying the Git environment."""
    
    def __init__(self, repo: GitRepository):
        """
        Initialize the Git environment checker.
        
        Args:
            repo: Git repository instance to be verified
        """
        self.repo = repo
    
    def check_internet_connection(self) -> bool:
        """
        Checks if there is an internet connection.
        
        Returns:
            bool: True if there is a connection
        
        Raises:
            InternetConnectionError: If there is no internet connection
        """
        try:
            request.urlopen('https://www.google.com', timeout=5)
            return True
        except Exception as e:
            raise InternetConnectionError('No internet connection available') from e
    
    def check_repo_authorization(self) -> bool:
        """
        Checks if there is authorization to access the remote repository.
        
        Returns:
            bool: True if there is authorization
        
        Raises:
            AuthorizationError: If there is no authorization or if the remote is not configured
        """
        remote_url = self.repo.get_remote_url()
        if not remote_url:
            raise AuthorizationError(
                "Remote repository not configured. Use 'git remote add origin <url>' to configure."
            )
        
        try:
            result = self.repo.execute_git_command(
                ["git", "ls-remote", "--exit-code"],
                capture_output=True
            )
            
            if result.returncode != 0:
                raise AuthorizationError(
                    "Unable to access remote repository. Please check your credentials."
                )
            
            return True
            
        except subprocess.TimeoutExpired as e:
            raise AuthorizationError("Timeout while connecting to remote repository") from e
        except Exception as e:
            raise AuthorizationError(f"Error checking authorization: {str(e)}") from e
    
    def check_changed_files(self) -> bool:
        """
        Checks if there are modified files in the repository.
        
        Returns:
            bool: True if there are modifications
        
        Raises:
            NoChangesError: If there are no modifications
        """
        # Check modified files
        modified = self.repo.execute_git_command(
            ['git', 'ls-files', '-m'],
            capture_output=True
        )
        
        # Check untracked files
        untracked = self.repo.execute_git_command(
            ['git', 'ls-files', '--others', '--exclude-standard'],
            capture_output=True
        )
        
        modified_files = modified.stdout.splitlines()
        untracked_files = untracked.stdout.splitlines()
        
        if not modified_files and not untracked_files:
            raise NoChangesError('No changes to commit in this repository')
        
        return True 