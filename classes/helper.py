from os import system as cmd

class Helper:

    commit_message_example = '''
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
    '''

    commit_message_types = {
        'feat' : '(new feature for the user, not a new feature for build script)',
        'fix' : '(bug fix for the user, not a fix to a build script)',
        'docs' : '(changes to the documentation)',
        'style' : '(formatting, missing semi colons, etc; no production code change)',
        'refactor' : '(refactoring production code, eg. renaming a variable)',
        'test' : '(adding missing tests, refactoring tests; no production code change)',
        'chore' : '(updating grunt tasks etc; no production code change)'
    }
        
    def print_helper(self):
        cmd('clear')
        print(f'{self.commit_message_example}\n')
        for key, value in self.commit_message_types.items():
            print(f'{key}: {value}')
        print()