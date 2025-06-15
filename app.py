#!/usr/bin/env python3
import sys
import os
from application.controller import GitController
from domain.errors import GitError

def main():
    """
    Main entry point for the application.
    Handles command line arguments and executes the appropriate Git operations.
    """
    try:
        controller = GitController(repo_path=os.getcwd())
        controller.process_commit(sys.argv)
    except GitError as e:
        # Display formatted error message
        print(f"\n{str(e)}\n")
        sys.exit(1)
    except Exception as e:
        # For unhandled errors, display a generic message
        print("\n❌ An unexpected error occurred. Please report this issue.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()