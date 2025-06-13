from typing import Optional, List
from domain.git_repository import GitRepository
from domain.git_environment import GitEnvironment
from domain.git_operations import GitOperations
from domain.errors import GitError, ValidationError, GitOperationError, AuthorizationError
from utils.helper import Helper
from config import ERROR_MESSAGES

class GitController:
    """Controller responsible for coordinating Git operations."""
    
    def __init__(self, repo_path: str):
        """
        Initialize the Git controller.
        
        Args:
            repo_path: Path to the Git repository
        
        Raises:
            GitOperationError: If there is an error initializing the repository
            AuthorizationError: If there is no authorization to access the repository
        """
        try:
            self.repo = GitRepository(repo_path)
            self.environment = GitEnvironment(self.repo)
            self.operations = GitOperations(self.repo)
            
            # Check authorization during initialization
            self.environment.check_repo_authorization()
        except AuthorizationError:
            raise
        except Exception as e:
            raise GitOperationError(
                operation="initialize_controller",
                error=str(e),
                details="Error initializing Git controller"
            ) from e
    
    def process_commit(self, args: List[str]) -> None:
        """
        Process command line arguments and execute the commit.
        
        Args:
            args: List of command line arguments
        
        Raises:
            ValidationError: If the arguments are invalid
            GitOperationError: If there is an error in the Git operation
            AuthorizationError: If there is no authorization to access the repository
        """
        if len(args) < 2:
            raise ValidationError(
                message=ERROR_MESSAGES['insufficient_args']['message'],
                details=ERROR_MESSAGES['insufficient_args']['details'],
                suggestion=ERROR_MESSAGES['insufficient_args']['suggestion']
            )
        
        if args[1] == "help":
            Helper.print_helper()
            return
        
        if len(args) < 3:
            raise ValidationError(
                message=ERROR_MESSAGES['no_commit_message']['message'],
                details=ERROR_MESSAGES['no_commit_message']['details'],
                suggestion=ERROR_MESSAGES['no_commit_message']['suggestion']
            )
        
        if args[1] not in Helper.commit_message_types:
            raise ValidationError(
                message=ERROR_MESSAGES['invalid_commit_type']['message'].format(commit_type=args[1]),
                details=ERROR_MESSAGES['invalid_commit_type']['details'].format(
                    valid_types=', '.join(Helper.commit_message_types.keys())
                ),
                suggestion=ERROR_MESSAGES['invalid_commit_type']['suggestion']
            )
        
        commit_message = f"{args[1]}: {' '.join(args[2:])}"
        self.execute_commit(commit_message)
    
    def validate_environment(self) -> None:
        """
        Validates the Git environment before operations.
        
        This method checks:
        1. Changed files
        2. Internet connection
        
        Note: Repository authorization is checked during initialization.
        
        Raises:
            GitOperationError: If any validation fails
        """
        try:
            # Check changes first, as it's faster
            self.environment.check_changed_files()
            # Check internet connection last
            self.environment.check_internet_connection()
        except Exception as e:
            raise GitOperationError(
                operation="validate_environment",
                error=str(e),
                details="Error validating Git environment"
            ) from e
    
    def execute_commit(self, message: str) -> None:
        """
        Executes a complete commit operation.
        
        This method:
        1. Validates the environment (files and internet)
        2. Adds all changes
        3. Creates a commit
        4. Pushes to remote
        
        Note: Repository authorization is already checked during initialization.
        
        Args:
            message: Commit message
        
        Raises:
            GitOperationError: If any operation fails
        """
        try:
            self.validate_environment()
            self.operations.add_files()
            self.operations.commit(message)
            self.operations.push()
        except Exception as e:
            raise GitOperationError(
                operation="execute_commit",
                error=str(e),
                details=f"Error executing commit with message: {message}"
            ) from e
    
    def show_status(self) -> None:
        """
        Shows the current status of the repository.
        
        Raises:
            GitOperationError: If there is an error getting the status
        """
        try:
            self.operations.status()
        except Exception as e:
            raise GitOperationError(
                operation="show_status",
                error=str(e),
                details="Error showing repository status"
            ) from e 