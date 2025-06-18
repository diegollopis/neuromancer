from urllib import request
import subprocess
from typing import List
from .git_repository import GitRepository
from config import (
    INTERNET_CHECK_URL,
    INTERNET_CHECK_TIMEOUT,
    GIT_COMMANDS,
    GIT_REPO_CONFIG
)
from utils.helper import Helper

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
        """
        try:
            request.urlopen(INTERNET_CHECK_URL, timeout=INTERNET_CHECK_TIMEOUT)
            return True
        except Exception as e:
            Helper.print_error(
                "No internet connection.",
                "Check your connection and try again."
            )
    
    def check_repo_authorization(self) -> bool:
        """
        Checks if there is authorization to access the remote repository.
        
        Returns:
            bool: True if there is authorization
        """
        remote_url = self.repo.get_remote_url()
        if not remote_url:
            Helper.print_error(
                "No remote repository configured.",
                "Configure with: git remote add origin <url>"
            )
        
        Helper.print_info(f"🔗 Checking access to repository: {remote_url}")
        
        # Test fetch for basic authorization
        fetch_result = self.repo.execute_git_command(GIT_COMMANDS['fetch'])
        if fetch_result.returncode != 0:
            Helper.print_error(
                "Repository authorization failed.",
                "Check your credentials and permissions."
            )
        
        # Test push (dry-run) for write permissions
        current_branch = self.repo.get_current_branch()
        push_result = self.repo.execute_git_command(
            GIT_COMMANDS['push_dry_run'] + [GIT_REPO_CONFIG['remote_name'], current_branch]
        )
        
        if push_result.returncode != 0:
            if "Permission denied" in push_result.stderr or "403" in push_result.stderr:
                Helper.print_error(
                    "Permission denied for push.",
                    "Check your access credentials."
                )
            else:
                Helper.print_error("Failed to check push permissions.")
        
        Helper.print_success("Repository authorization verified!")
        return True
    
    def check_changed_files(self) -> bool:
        """
        Checks if there are modified files in the repository.
        
        Returns:
            bool: True if there are modifications
        """
        Helper.print_info("📝 Checking for modified files...")
        
        # Check modified files
        modified_result = self.repo.execute_git_command(GIT_COMMANDS['list_modified'])
        modified_files = modified_result.stdout.splitlines() if modified_result.stdout else []
        
        # Check untracked files
        untracked_result = self.repo.execute_git_command(GIT_COMMANDS['list_untracked'])
        untracked_files = untracked_result.stdout.splitlines() if untracked_result.stdout else []
        
        if not modified_files and not untracked_files:
            Helper.print_error(
                "No changes found to commit.",
                "Make some changes first."
            )
        
        Helper.print_success(f"Found {len(modified_files)} modified files and {len(untracked_files)} untracked files.")
        return True 