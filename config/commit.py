"""
Commit message configuration settings.
"""

COMMIT_MESSAGE_EXAMPLE = '''
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
'''

COMMIT_MESSAGE_TYPES = {
    'feat': '(new feature for the user, not a new feature for build script)',
    'fix': '(bug fix for the user, not a fix to a build script)',
    'docs': '(changes to the documentation)',
    'style': '(formatting, missing semi colons, etc; no production code change)',
    'refactor': '(refactoring production code, eg. renaming a variable)',
    'test': '(adding missing tests, refactoring tests; no production code change)',
    'chore': '(updating grunt tasks etc; no production code change)'
}

COMMIT_MESSAGE_REFERENCES = [
    'www.conventionalcommits.org/',
    'seesparkbox.com/foundry/semantic_commit_messages',
    'karma-runner.github.io/1.0/dev/git-commit-msg.html'
] 