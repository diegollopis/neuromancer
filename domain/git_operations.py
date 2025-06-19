from .git_repository import GitRepository
from config import GIT_OPERATIONS_DELAY, GIT_COMMANDS
from utils.helper import Helper

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
        """
        Helper.print_info("📁 Adding files...")
        result = self.repo.execute_git_command(GIT_COMMANDS['add'] + ['.'])
        if result.returncode == 0:
            Helper.print_success("git add completed!")
        else:
            Helper.print_error("Error adding files")
    
    def commit(self, message: str):
        """
        Creates a commit with the staged changes.
        
        Args:
            message: Commit message
        """
        Helper.print_info(f"💾 Creating commit: {message}")
        result = self.repo.execute_git_command(GIT_COMMANDS['commit'] + [message])
        if result.returncode == 0:
            Helper.print_success("git commit completed!")
        else:
            Helper.print_error("Error creating commit")
    
    def push(self):
        """
        Pushes commits to the remote repository.
        """
        current_branch = self.repo.get_current_branch()
        Helper.print_info(f"🚀 Pushing to branch: {current_branch}")
        result = self.repo.execute_git_command(GIT_COMMANDS['push'] + ['origin', current_branch])
        if result.returncode == 0:
            Helper.print_success("git push completed!")
        else:
            Helper.print_error("Error pushing to remote repository") 