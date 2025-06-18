#!/usr/bin/env python3
from typing import List
from domain.git_repository import GitRepository
from domain.git_environment import GitEnvironment
from domain.git_operations import GitOperations
from utils.helper import Helper

class GitController:
    """Controller class for Git operations."""
    
    def __init__(self, repo_path: str):
        """
        Initialize the Git controller.
        
        Args:
            repo_path: Path to the Git repository
        """
        self.repo = GitRepository(repo_path)
        self.environment = GitEnvironment(self.repo)
        self.operations = GitOperations(self.repo)
    
    def process_commit(self, args: List[str]):
        """
        Process command line arguments and execute the commit.
        
        Args:
            args: List of command line arguments
        """
        # Check if there are enough arguments
        if len(args) < 2:
            Helper.print_error(
                "No arguments provided.",
                "Expected usage: neuromancer <commit_type> <message>\nUse 'neuromancer help' to see available options"
            )
        
        # Check if it's a help request
        if args[1] == "help":
            Helper.print_helper()
            return
        
        # Check if there's a commit message
        if len(args) < 3:
            Helper.print_error(
                "No commit message provided.",
                "Expected usage: neuromancer <commit_type> <message>\nProvide a commit message after the commit type"
            )
        
        # Check if commit type is valid
        commit_type = args[1]
        if commit_type not in Helper.commit_message_types:
            valid_types = ', '.join(f"'{t}'" for t in Helper.commit_message_types.keys())
            Helper.print_error(
                f"Invalid commit type: '{commit_type}'.",
                f"Valid types are: {valid_types}\nUse one of the valid types above"
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
        """
        Helper.print_info("🔍 Validating Git environment...")
        
        # Check internet connection first, as it's a basic requirement
        self.environment.check_internet_connection()
        
        # Then check repository authorization
        self.environment.check_repo_authorization()
        
        # Finally check for changes
        self.environment.check_changed_files()
        
        Helper.print_success("Environment successfully validated!")
    
    def execute_commit(self, message: str):
        """
        Executes a complete commit operation.
        
        This method:
        1. Validates the environment (files and internet)
        2. Adds all changes
        3. Creates a commit
        4. Pushes to remote
        
        Args:
            message: Commit message
        """
        Helper.print_info(f"🚀 Starting commit process: {message}")
        
        self.validate_environment()
        self.operations.add_files()
        self.operations.commit(message)
        self.operations.push()
        
        Helper.print_success("Commit process completed successfully!") 