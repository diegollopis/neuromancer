import subprocess
import time
import os

items = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore']

def chooseOption():
    print("-------------") 
    for item in items:
        print(item)
    print("-------------") 
    option = input(": ").lower()
    while option not in items:
        option = input("Opção não permitida. Digite novamente: ")
    return option

def execute(list):
    subprocess.run(list)
    time.sleep(2)

def checkGit():
    response = subprocess.run(['git', 'rev-parse', '--git-dir'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return True if response.returncode == 0 else False

def gitAdd():
    execute(['git', 'add', "."])

def gitCommit(message):
    execute(['git', 'commit', '-m', message])

def gitStatus():
    # git ls-files -m -o --exclude-from=.gitignore
    response = subprocess.run(['git', 'ls-files', '-m', '-o', '--exclude-from=.gitignore'], capture_output=True, text=True)
    file_list = response.stdout.splitlines()
    return True if len(file_list) > 0 else False

def gitPush():
    branch_name = getCurrentBranch()
    execute(['git', 'push', '-u', 'origin', branch_name])

def getCurrentBranch():
    branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode("utf-8")
    return branch_name

def formatMessage():
    type = chooseOption()
    message = input('Digite a mensagem do commit: ')
    return f'{type}: {message}'

def doGitSteps(message):
    gitAdd()
    gitCommit(message)
    gitPush()

def main():
    isGit = checkGit()
    areChanges = gitStatus()
    
    if not isGit:
        print('Não é um diretório git!')
        return 
    
    if not areChanges:
        print('Não há modificações no repo!')
        return

    os.system('clear')
    message = formatMessage()
    doGitSteps(message)

if __name__ == "__main__":
    main()
