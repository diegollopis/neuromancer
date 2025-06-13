from typing import Optional, List
from domain.git_repository import GitRepository
from domain.git_environment import GitEnvironment
from domain.git_operations import GitOperations
from domain.errors import GitError, ValidationError
from utils.helper import Helper

class GitController:
    """Controller responsible for coordinating Git operations."""
    
    def __init__(self, repo_path: str):
        """
        Initialize the Git controller.
        
        Args:
            repo_path: Path to the Git repository
        
        Raises:
            GitError: If there is an error initializing the repository
        """
        try:
            self.repo = GitRepository(repo_path)
            self.environment = GitEnvironment(self.repo)
            self.operations = GitOperations(self.repo)
        except Exception as e:
            raise GitError(f"Error initializing Git controller: {str(e)}") from e
    
    def process_commit(self, args: List[str]) -> None:
        """
        Processa os argumentos da linha de comando e executa o commit.
        
        Args:
            args: Lista de argumentos da linha de comando
        
        Raises:
            ValidationError: Se os argumentos forem inválidos
            GitError: Se houver erro na operação do Git
        """
        if len(args) < 2:
            raise ValidationError(
                "Uso: python app.py <tipo_commit> <mensagem>\n"
                "Exemplo: python app.py feat add new feature\n"
                "\nUse 'python app.py help' para ver os tipos de commit disponíveis."
            )
        
        if args[1] == "help":
            Helper.print_helper()
            return
        
        if len(args) < 3:
            raise ValidationError(
                "Erro: mensagem do commit não fornecida.\n"
                "Uso: python app.py <tipo_commit> <mensagem>"
            )
        
        if args[1] not in Helper.commit_message_types:
            raise ValidationError(
                f"Tipo de commit inválido: {args[1]}\n"
                "Use 'python app.py help' para ver os tipos válidos."
            )
        
        commit_message = f"{args[1]}: {' '.join(args[2:])}"
        self.execute_commit(commit_message)
    
    def validate_environment(self) -> None:
        """
        Validates the Git environment before operations.
        
        This method checks:
        1. Internet connection
        2. Repository authorization
        3. Changed files
        
        Raises:
            GitError: If any validation fails
        """
        try:
            self.environment.check_internet_connection()
            self.environment.check_repo_authorization()
            self.environment.check_changed_files()
        except Exception as e:
            raise GitError(f"Error validating environment: {str(e)}") from e
    
    def execute_commit(self, message: str) -> None:
        """
        Executes a complete commit operation.
        
        This method:
        1. Validates the environment
        2. Adds all changes
        3. Creates a commit
        4. Pushes to remote
        
        Args:
            message: Commit message
        
        Raises:
            GitError: If any operation fails
        """
        try:
            self.validate_environment()
            self.operations.add_files()
            self.operations.commit(message)
            self.operations.push()
        except Exception as e:
            raise GitError(f"Error executing commit operation: {str(e)}") from e
    
    def show_status(self) -> None:
        """
        Shows the current status of the repository.
        
        Raises:
            GitError: If there is an error getting the status
        """
        try:
            self.operations.status()
        except Exception as e:
            raise GitError(f"Error showing repository status: {str(e)}") from e 