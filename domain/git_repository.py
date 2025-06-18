import subprocess
from pathlib import Path
from typing import Optional
from utils.helper import Helper

class GitRepository:
    """Represents a Git repository and its basic operations."""
    
    def __init__(self, repo_path: str):
        """
        Initialize a Git repository.
        
        Args:
            repo_path: Path to the Git repository
        """
        self.repo_path = Path(repo_path)
        self._validate_git_repo()
    
    def _validate_git_repo(self):
        """
        Validates if the directory is a valid Git repository.
        """
        if not (self.repo_path / '.git').exists():
            Helper.print_error(
                f"'{self.repo_path}' is not a valid Git repository.",
                "Run 'git init' to initialize a repository."
            )
    
    def get_current_branch(self) -> str:
        """
        Returns the name of the current branch.
        
        Returns:
            str: Name of the current branch
        """
        result = self.execute_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            Helper.print_error("Error getting current branch", result.stderr)
    
    def get_remote_url(self) -> Optional[str]:
        """
        Returns the URL of the remote repository.
        
        Returns:
            Optional[str]: Remote URL if configured, None otherwise
        """
        result = self.execute_git_command(['git', 'config', '--get', 'remote.origin.url'])
        if result.returncode == 0:
            return result.stdout.strip() if result.stdout else None
        return None
    
    def execute_git_command(self, command: list[str]) -> subprocess.CompletedProcess:
        """
        Executes a Git command and shows output directly.
        
        Args:
            command: List of command and its arguments
        
        Returns:
            subprocess.CompletedProcess: Command execution result
        """
        result = subprocess.run(
            command,
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        
        # Show command output
        if result.stdout:
            print(result.stdout)
        
        # Show errors if any
        if result.stderr:
            print(result.stderr)
        
        return result 