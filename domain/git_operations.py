from time import sleep
from typing import List, Optional
from .git_repository import GitRepository
from .errors import handle_git_errors, GitOperationError

class GitOperations:
    """Responsible for performing Git operations."""
    
    def __init__(self, repo: GitRepository, delay: float = 1.0):
        """
        Initialize Git operations.
        
        Args:
            repo: Git repository instance to perform operations
            delay: Time between operations (in seconds)
        """
        self.repo = repo
        self.delay = delay
    
    def _execute_with_delay(self, command: list[str], name: str) -> None:
        """
        Executes a Git command with delay and feedback.
        
        Args:
            command: List of command and its arguments
            name: Name of the operation for feedback
        """
        try:
            self.repo.execute_git_command(command)
            sleep(self.delay)
            print(f'\n✅ git {name} done!\n')
        except Exception as e:
            raise GitOperationError(
                operation=name,
                error=str(e),
                details=f"Erro ao executar operação 'git {name}'"
            ) from e
    
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
                self.repo.execute_git_command(['git', 'add'] + files)
            else:
                self.repo.execute_git_command(['git', 'add', '.'])
        except Exception as e:
            raise GitOperationError(
                operation="add",
                error=str(e),
                details="Erro ao adicionar arquivos ao staging"
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
            self.repo.execute_git_command(['git', 'commit', '-m', message])
        except Exception as e:
            raise GitOperationError(
                operation="commit",
                error=str(e),
                details=f"Erro ao criar commit com mensagem: {message}"
            ) from e
    
    def push(self) -> None:
        """
        Pushes commits to the remote repository.
        
        Raises:
            GitOperationError: If the push operation fails
        """
        try:
            current_branch = self.repo.get_current_branch()
            self.repo.execute_git_command(['git', 'push', 'origin', current_branch])
        except Exception as e:
            raise GitOperationError(
                operation="push",
                error=str(e),
                details=f"Erro ao fazer push para a branch {current_branch}"
            ) from e
    
    def status(self) -> None:
        """
        Shows the current status of the repository.
        
        Raises:
            GitOperationError: If there is an error getting the status
        """
        try:
            self.repo.execute_git_command(['git', 'status'])
        except Exception as e:
            raise GitOperationError(
                operation="status",
                error=str(e),
                details="Erro ao obter status do repositório"
            ) from e
    
    @handle_git_errors
    def do_git_steps(self, message: str) -> None:
        """
        Executes the complete sequence of Git operations.
        
        Args:
            message: Commit message
        """
        self.add_files()
        self.commit(message)
        self.push()
        self.status()
        print() 