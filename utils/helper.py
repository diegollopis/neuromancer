from os import system as cmd

class Helper:
    """Helper class for commit message conventions."""

    commit_message_example = '''
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
    '''

    commit_message_types = {
        'feat': '(new feature for the user, not a new feature for build script)',
        'fix': '(bug fix for the user, not a fix to a build script)',
        'docs': '(changes to the documentation)',
        'style': '(formatting, missing semi colons, etc; no production code change)',
        'refactor': '(refactoring production code, eg. renaming a variable)',
        'test': '(adding missing tests, refactoring tests; no production code change)',
        'chore': '(updating grunt tasks etc; no production code change)'
    }

    references = [
        'www.conventionalcommits.org/',
        'seesparkbox.com/foundry/semantic_commit_messages',
        'karma-runner.github.io/1.0/dev/git-commit-msg.html'
    ]

    @classmethod
    def print_message_example(cls):
        """Prints the commit message example and available types."""
        print(f'{cls.commit_message_example}\n')
        for key, value in cls.commit_message_types.items():
            print(f'{key}: {value}')
        print()

    @classmethod
    def print_references(cls):
        """Prints the reference links."""
        print('References\n')
        for reference in cls.references:
            print(reference)
        print()

    @classmethod
    def print_helper(cls):
        """Prints the complete help information."""
        cmd('clear')
        cls.print_message_example()
        cls.print_references() 