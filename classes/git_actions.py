import subprocess
from classes.utils import Utils

class GitAction:

    @classmethod
    def execute(cls, action: list):
        subprocess.run(action)
        Utils.wait()

    @classmethod
    def check_is_repo_git(cls):
        response = subprocess.run(
            ['git', 'rev-parse', '--git-dir'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return response.returncode == 0 

    @classmethod
    def check_changed_files(cls):
        response = subprocess.run(
            ['git', 'ls-files', '-m', '-o', '--exclude-from=.gitignore'],
            capture_output=True,
            text=True
        )
        files_changed_list = response.stdout.splitlines()
        return len(files_changed_list) > 0

    @classmethod
    def get_current_branch(cls):
        branch_name = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).strip().decode("utf-8")
        return branch_name

    @classmethod
    def config_git_action(cls, action: list, name: str):
        GitAction.execute(action)
        print(f'\ngit {name} done!\n')

    @classmethod
    def add_files(cls):
        cls.config_git_action(['git', 'add', '.'], 'add')

    @classmethod
    def commit(cls, message: str):
        cls.config_git_action(['git', 'commit', '-m', message], 'commit')

    @classmethod
    def push(cls):
        branch_name = cls.get_current_branch()
        cls.config_git_action(['git', 'push', '-u', 'origin', branch_name], 'push')

    @classmethod
    def status(cls):
        cls.execute(['git', 'status'])

    @classmethod
    def do_git_steps(cls, message: str):
        cls.add_files()
        cls.commit(message)
        cls.push()
        cls.status()
        print()
