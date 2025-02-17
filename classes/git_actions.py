import subprocess
from classes.utils import Utils

class GitAction:

    @classmethod
    def execute(cls, action: list):
        subprocess.run(action)
        Utils.wait()

    @classmethod
    def check_is_git_detected(cls):
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
    def add_files(cls):
        GitAction.execute(['git', 'add', "."])
        print('\nFiles ready to commit!\n')

    @classmethod
    def commit(cls, message: str):
        GitAction.execute(['git', 'commit', '-m', message])
        print('\nCommit setup done!\n')

    @classmethod
    def push(cls):
        branch_name = cls.get_current_branch()
        GitAction.execute(['git', 'push', '-u', 'origin', branch_name])
        print('\nPush to remote repo done successfully!\n')

    @classmethod
    def do_git_steps(cls, message: str):
        cls.add_files()
        cls.commit(message)
        cls.push()
