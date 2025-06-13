import subprocess
from time import sleep as timer
from urllib import request
from .errors import (
    InternetConnectionError,
    AuthorizationError,
    NotGitRepositoryError,
    NoChangesError,
    handle_git_errors
)

class GitAction:

    @classmethod
    def check_internet_connection(cls) -> bool:
        try:
            request.urlopen('https://www.google.com', timeout=5)
            return True
        except:
            raise InternetConnectionError('No internet connection.')

    @classmethod
    def execute(cls, action: list) -> None:
        subprocess.run(action)
        timer(1)

    @classmethod
    def config_git_action(cls, action: list, name: str) -> None:
        cls.execute(action)
        print(f'\n✅ git {name} done!\n')

    @classmethod
    def check_repo_authorization(cls) -> bool:
        try:
            # Verifica se há um remote configurado
            remote_result = subprocess.run(
                ["git", "remote", "-v"],
                capture_output=True,
                text=True
            )
            
            if not remote_result.stdout.strip():
                raise AuthorizationError("No remote repository configured. Use 'git remote add origin <url>' to add one.")
            
            # Tenta listar as referências remotas (mais leve que push)
            result = subprocess.run(
                ["git", "ls-remote", "--exit-code"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                raise AuthorizationError("Unable to access the remote repository. Please check your credentials.")
            
            return True
            
        except subprocess.TimeoutExpired:
            raise AuthorizationError("Connection to remote repository timed out.")
        except Exception as e:
            raise AuthorizationError(f"Error checking repository authorization: {str(e)}")

    @classmethod
    def check_is_repo_git(cls) -> bool:
        response = subprocess.run(
            ['git', 'rev-parse', '--git-dir'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if response.returncode != 0:
            raise NotGitRepositoryError('Git not found.')
        return True

    @classmethod
    def check_changed_files(cls) -> bool:
        response = subprocess.run(
            ['git', 'ls-files', '-m', '-o', '--exclude-from=.gitignore'],
            capture_output=True,
            text=True
        )
        files_changed_list = response.stdout.splitlines()
        if len(files_changed_list) == 0:
            raise NoChangesError('There are no modifications in this repository.')
        return True

    @classmethod
    def get_current_branch(cls) -> str:
        return subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).strip().decode("utf-8")

    @classmethod
    def add(cls) -> None:
        cls.config_git_action(['git', 'add', '.'], 'add')

    @classmethod
    def commit(cls, message: str) -> None:
        cls.config_git_action(['git', 'commit', '-m', message], 'commit')

    @classmethod
    def push(cls) -> None:
        branch_name = cls.get_current_branch()
        cls.config_git_action(['git', 'push', '-u', 'origin', branch_name], 'push')

    @classmethod
    def status(cls) -> None:
        cls.execute(['git', 'status'])

    @classmethod
    @handle_git_errors
    def do_git_steps(cls, message: str) -> None:
        cls.add()
        cls.commit(message)
        cls.push()
        cls.status()
        print() 