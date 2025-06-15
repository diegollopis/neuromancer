#!/usr/bin/env python3
from typing import List
from domain.git_repository import GitRepository
from domain.git_environment import GitEnvironment
from domain.git_operations import GitOperations
from domain.errors import GitError
from utils.helper import Helper

class GitController:
    """Controller class for Git operations."""
    
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
        except GitError:
            raise
        except Exception as e:
            raise GitError.operation_failed(
                operation="initialize_controller",
                error=str(e),
                details="Error initializing Git controller"
            ) from e
    
    def process_commit(self, args: List[str]):
        """
        Process command line arguments and execute the commit.
        
        Args:
            args: List of command line arguments
        
        Raises:
            GitError: If there is an error in the Git operation
        """
        # Check if there are enough arguments
        if len(args) < 2:
            raise GitError.invalid_args(
                details="No arguments provided.\nExpected: neuromancer <commit_type> <message>",
                suggestion="Use 'neuromancer help' to see available options"
            )
        
        # Check if it's a help request
        if args[1] == "help":
            Helper.print_helper()
            return
        
        # Check if there's a commit message
        if len(args) < 3:
            raise GitError.invalid_args(
                details="No commit message provided.\nExpected: neuromancer <commit_type> <message>",
                suggestion="Provide a commit message after the commit type"
            )
        
        # Check if commit type is valid
        commit_type = args[1]
        if commit_type not in Helper.commit_message_types:
            valid_types = ', '.join(f"'{t}'" for t in Helper.commit_message_types.keys())
            raise GitError.invalid_args(
                details=f"Invalid commit type: '{commit_type}'.\nValid types are: {valid_types}",
                suggestion="Use one of the valid commit types above"
            )
        
        # Build and execute commit
        commit_message = f"{commit_type}: {' '.join(args[2:])}"
        self.execute_commit(commit_message)
    
    def validate_environment(self):
        """
        Validates the Git environment before operations.
        
        This method checks in order:
        1. Internet connection (first, as it's a basic requirement)
        2. Repository authorization (after confirming internet connection)
        3. Changed files (after confirming both internet and authorization)
        
        Raises:
            GitError: If any validation fails
        """
        try:
            # Check internet connection first, as it's a basic requirement
            self.environment.check_internet_connection()
            
            # Then check repository authorization
            self.environment.check_repo_authorization()
            
            # Finally check for changes
            self.environment.check_changed_files()
        except GitError:
            raise
        except Exception as e:
            raise GitError.operation_failed(
                operation="validate_environment",
                error=str(e),
                details="Error validating Git environment"
            ) from e
    
    def execute_commit(self, message: str):
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
            GitError: If any operation fails
        """
        try:
            self.validate_environment()
            self.operations.add_files()
            self.operations.commit(message)
            self.operations.push()
            self.operations.status()
        except GitError:
            raise
        except Exception as e:
            raise GitError.operation_failed(
                operation="execute_commit",
                error=str(e),
                details=f"Error executing commit with message: {message}"
            ) from e
    
    def show_status(self):
        """
        Shows the current status of the repository.
        
        Raises:
            GitError: If there is an error getting the status
        """
        try:
            self.operations.status()
        except GitError:
            raise
        except Exception as e:
            raise GitError.operation_failed(
                operation="show_status",
                error=str(e),
                details="Error showing repository status"
            ) from e 