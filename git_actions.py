import subprocess
from utils import Utils

class GitAction:

    utils = Utils()

    def execute(self, list: list):
        subprocess.run(list)
        self.utils.wait()

    def check_is_git_detected(self):
        response = subprocess.run(['git', 'rev-parse', '--git-dir'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return response.returncode == 0 
    
    def get_current_branch(self):
        branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode("utf-8")
        return branch_name

    def add_files(self):
        self.execute(['git', 'add', "."])

    def commit(self, message: str):
        self.execute(['git', 'commit', '-m', message])

    def check_changed_files(self):
        response = subprocess.run(['git', 'ls-files', '-m', '-o', '--exclude-from=.gitignore'], capture_output=True, text=True)
        files_changed_list = response.stdout.splitlines()
        return len(files_changed_list) > 0

    def push(self):
        branch_name = self.get_current_branch()
        self.execute(['git', 'push', '-u', 'origin', branch_name])
    
    def do_git_steps(self, message: str):
        self.add_files()
        self.commit(message)
        self.push()
