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
        # Exibe apenas a mensagem formatada do erro, sem o traceback
        print(f"\n❌ {e.title}\n")
        if e.details:
            print(f"Details:\n{e.details}\n")
        if e.suggestion:
            print(f"Suggestion:\n{e.suggestion}\n")
        sys.exit(1)
    except Exception as e:
        # Para erros não tratados, exibe uma mensagem genérica
        print("\n❌ An unexpected error occurred\n")
        print(f"Details:\n{str(e)}\n")
        print("Suggestion:\nPlease report this issue to the project maintainers.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()