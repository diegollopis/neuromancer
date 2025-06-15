from urllib import request
import subprocess
from typing import List
from .git_repository import GitRepository
from .errors import GitError
from config import (
    INTERNET_CHECK_URL,
    INTERNET_CHECK_TIMEOUT,
    GIT_COMMANDS,
    GIT_REPO_CONFIG
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
            GitError: If there is no internet connection
        """
        try:
            request.urlopen(INTERNET_CHECK_URL, timeout=INTERNET_CHECK_TIMEOUT)
            return True
        except Exception as e:
            raise GitError.internet_connection() from e
    
    def check_repo_authorization(self) -> bool:
        """
        Checks if there is authorization to access the remote repository.
        
        Returns:
            bool: True if there is authorization
        
        Raises:
            GitError: If there is no authorization, no internet connection, or if the remote is not configured
        """
        remote_url = self.repo.get_remote_url()
        if not remote_url:
            raise GitError.no_remote()
        
        try:
            # First try to get information from the remote repository
            fetch_result = self.repo.execute_git_command(
                GIT_COMMANDS['fetch'],
                capture_output=True
            )
            
            # If we got here, we have basic authorization
            # Now check if we have push permission
            current_branch = self.repo.get_current_branch()
            push_result = self.repo.execute_git_command(
                GIT_COMMANDS['push_dry_run'] + [GIT_REPO_CONFIG['remote_name'], current_branch],
                capture_output=True
            )
            
            # Check for specific permission errors
            if "Permission denied" in push_result.stderr or "403" in push_result.stderr:
                raise GitError.auth_failed()
            
            return True
            
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.lower() if e.stderr else str(e).lower()
            
            # Check for internet connection errors first
            if any(msg in error_msg for msg in ["could not resolve host", "failed to connect", "connection refused", "network is unreachable"]):
                raise GitError.internet_connection()
            
            # Then check for other specific errors
            if "permission denied" in error_msg or "403" in error_msg:
                raise GitError.auth_failed()
            elif "not found" in error_msg or "404" in error_msg:
                raise GitError.repo_not_found()
            else:
                raise GitError.operation_failed(
                    operation="check_authorization",
                    error=str(e),
                    details="Error checking repository authorization"
                )
            
        except subprocess.TimeoutExpired as e:
            # Timeout usually means internet connection issues
            raise GitError.internet_connection() from e
        except Exception as e:
            # Check if it's a network-related error
            error_msg = str(e).lower()
            if any(msg in error_msg for msg in ["connection", "network", "host", "timeout", "refused"]):
                raise GitError.internet_connection() from e
            
            raise GitError.operation_failed(
                operation="check_authorization",
                error=str(e),
                details="Error checking repository authorization"
            ) from e
    
    def check_changed_files(self) -> bool:
        """
        Checks if there are modified files in the repository.
        
        Returns:
            bool: True if there are modifications
        
        Raises:
            GitError: If there are no modifications or if there is an error checking files
        """
        try:
            # Check modified files
            modified = self.repo.execute_git_command(
                GIT_COMMANDS['list_modified'],
                capture_output=True
            )
            
            # Check untracked files
            untracked = self.repo.execute_git_command(
                GIT_COMMANDS['list_untracked'],
                capture_output=True
            )
            
            modified_files = modified.stdout.splitlines()
            untracked_files = untracked.stdout.splitlines()
            
            if not modified_files and not untracked_files:
                raise GitError.no_changes()
            
            return True
        except GitError:
            raise
        except Exception as e:
            raise GitError.operation_failed(
                operation="check_changed_files",
                error=str(e),
                details="Error checking modified files"
            ) from e 