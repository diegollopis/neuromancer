import sys
import os
from application.controller import GitController
from domain.errors import GitError

def main():
    """Main function that starts the application."""
    try:
        controller = GitController(repo_path=os.getcwd())
        controller.process_commit(sys.argv)
    except GitError as e:
        print(f"\n❌ {e.message}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()