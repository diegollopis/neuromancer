import subprocess
from utils import Utils

class GitAction:

    utils = Utils()

    def execute(self, list):
        subprocess.run(list)
        self.utils.wait()

    def check_git(self):
        response = subprocess.run(['git', 'rev-parse', '--git-dir'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return response.returncode == 0 

    def add(self):
        self.execute(['git', 'add', "."])

    def commit(self, message):
        self.execute(['git', 'commit', '-m', message])

    def status(self):
        response = subprocess.run(['git', 'ls-files', '-m', '-o', '--exclude-from=.gitignore'], capture_output=True, text=True)
        files_list = response.stdout.splitlines()
        return len(files_list) > 0

    def push(self):
        branch_name = self.getCurrentBranch()
        self.execute(['git', 'push', '-u', 'origin', branch_name])

    def get_current_branch(self):
        branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode("utf-8")
        return branch_name
    
    def do_git_steps(self, message):
        self.add()
        self.commit(message)
        self.push()
