#!/usr/bin/env python3
import sys
import os
from application.controller import GitController
from utils.helper import Helper

def main():
    """
    Main entry point for the application.
    Handles command line arguments and executes the appropriate Git operations.
    """
    try:
        controller = GitController(repo_path=os.getcwd())
        controller.process_commit(sys.argv)
    except KeyboardInterrupt:
        Helper.print_error("Operation cancelled by user.")
    except Exception as e:
        # For unhandled errors, display a generic message
        Helper.print_error(
            f"Unexpected error: {str(e)}",
            "Please report this issue."
        )

if __name__ == "__main__":
    main()