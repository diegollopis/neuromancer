import subprocess
from pathlib import Path
from typing import Optional
from .errors import GitError

class GitRepository:
    """Represents a Git repository and its basic operations."""
    
    def __init__(self, repo_path: str):
        """
        Initialize a Git repository.
        
        Args:
            repo_path: Path to the Git repository
        
        Raises:
            GitError: If the directory is not a valid Git repository
        """
        self.repo_path = Path(repo_path)
        self._validate_git_repo()
    
    def _validate_git_repo(self) -> None:
        """
        Validates if the directory is a valid Git repository.
        
        Raises:
            GitError: If the directory is not a Git repository
        """
        if not (self.repo_path / '.git').exists():
            raise GitError('Directory is not a Git repository')
    
    def get_current_branch(self) -> str:
        """
        Returns the name of the current branch.
        
        Returns:
            str: Name of the current branch
        
        Raises:
            GitError: If there is an error getting the branch name
        """
        try:
            result = self.execute_git_command(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                capture_output=True
            )
            return result.stdout.strip()
        except Exception as e:
            raise GitError('Error getting current branch') from e
    
    def get_remote_url(self) -> Optional[str]:
        """
        Returns the URL of the remote repository.
        
        Returns:
            Optional[str]: Remote URL if configured, None otherwise
        
        Raises:
            GitError: If there is an error getting the remote URL
        """
        try:
            result = self.execute_git_command(
                ['git', 'config', '--get', 'remote.origin.url'],
                capture_output=True
            )
            return result.stdout.strip() if result.stdout else None
        except Exception as e:
            raise GitError('Error getting remote URL') from e
    
    def execute_git_command(self, command: list[str], capture_output: bool = False) -> subprocess.CompletedProcess:
        """
        Executes a Git command.
        
        Args:
            command: List of command and its arguments
            capture_output: Whether to capture command output
        
        Returns:
            subprocess.CompletedProcess: Command execution result
        
        Raises:
            GitError: If the command execution fails
        """
        try:
            return subprocess.run(
                command,
                cwd=self.repo_path,
                check=True,
                capture_output=capture_output,
                text=True
            )
        except subprocess.CalledProcessError as e:
            raise GitError(f'Git command failed: {e.stderr}') from e
        except Exception as e:
            raise GitError(f'Error executing Git command: {str(e)}') from e 