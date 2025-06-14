from urllib import request
import subprocess
from typing import List
from .git_repository import GitRepository
from .errors import (
    InternetConnectionError,
    AuthorizationError,
    NoChangesError,
    GitOperationError
)
from config import (
    INTERNET_CHECK_URL,
    INTERNET_CHECK_TIMEOUT,
    ERROR_MESSAGES,
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
            InternetConnectionError: If there is no internet connection
        """
        try:
            request.urlopen(INTERNET_CHECK_URL, timeout=INTERNET_CHECK_TIMEOUT)
            return True
        except Exception as e:
            raise InternetConnectionError(
                ERROR_MESSAGES['no_internet']['message']
            ) from e
    
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
                message=ERROR_MESSAGES['no_remote']['message'],
                details=ERROR_MESSAGES['no_remote']['details'],
                suggestion=ERROR_MESSAGES['no_remote']['suggestion']
            )
        
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
                raise AuthorizationError(
                    message=ERROR_MESSAGES['no_permission']['message'],
                    details=f"You don't have permission to push to branch {current_branch}",
                    suggestion=ERROR_MESSAGES['no_permission']['suggestion']
                )
            
            return True
            
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.lower() if e.stderr else str(e).lower()
            
            if "permission denied" in error_msg or "403" in error_msg:
                raise AuthorizationError(
                    message=ERROR_MESSAGES['no_permission']['message'],
                    details=ERROR_MESSAGES['no_permission']['details'],
                    suggestion=ERROR_MESSAGES['no_permission']['suggestion']
                )
            elif "not found" in error_msg or "404" in error_msg:
                raise AuthorizationError(
                    message=ERROR_MESSAGES['repo_not_found']['message'],
                    details=ERROR_MESSAGES['repo_not_found']['details'],
                    suggestion=ERROR_MESSAGES['repo_not_found']['suggestion']
                )
            else:
                raise AuthorizationError(
                    message="Error checking authorization",
                    details=str(e),
                    suggestion="Check your credentials and access permissions"
                )
            
        except subprocess.TimeoutExpired as e:
            raise AuthorizationError(
                message="Timeout connecting to remote repository",
                details=str(e),
                suggestion="Check your internet connection and try again"
            ) from e
        except Exception as e:
            raise AuthorizationError(
                message="Error checking authorization",
                details=str(e),
                suggestion="Check your credentials and access permissions"
            ) from e
    
    def check_changed_files(self) -> bool:
        """
        Checks if there are modified files in the repository.
        
        Returns:
            bool: True if there are modifications
        
        Raises:
            NoChangesError: If there are no modifications
            GitOperationError: If there is an error checking files
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
                raise NoChangesError(
                    ERROR_MESSAGES['no_changes']['message']
                )
            
            return True
        except NoChangesError:
            raise
        except Exception as e:
            raise GitOperationError(
                operation="check_changed_files",
                error=str(e),
                details="Error checking modified files"
            ) from e 