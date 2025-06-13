from typing import List, Tuple
from utils.helper import Helper
from domain.git_action import GitAction
from domain.errors import ValidationError, handle_git_errors

class Controller:
    COMMIT_TYPES: Tuple[str, ...] = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore')

    @classmethod
    def validate_commit_args(cls, argv: List[str]) -> str:
        """Valida os argumentos do commit e retorna a mensagem formatada"""
        if len(argv) == 1:
            raise ValidationError('A commit option and message are required.')

        if len(argv) == 2:
            if argv[1] == 'help':
                Helper.print_helper()
                return None
            if argv[1] not in cls.COMMIT_TYPES:
                raise ValidationError(f'Commit option is not valid! Only options below are available.\n\n{cls.COMMIT_TYPES}\n')
            raise ValidationError('You need to add a commit message.')

        return f"{argv[1]}: {' '.join(argv[2:])}"

    @classmethod
    @handle_git_errors
    def main(cls, argv: List[str]) -> None:
        # Validação inicial do ambiente Git
        GitAction.check_internet_connection()
        GitAction.check_repo_authorization()
        GitAction.check_is_repo_git()
        GitAction.check_changed_files()

        # Validação dos argumentos do commit
        commit_message = cls.validate_commit_args(argv)
        if commit_message:
            cls.confirm_message_and_do_git_steps_or_cancel(commit_message)

    @classmethod
    def confirm_message_and_do_git_steps_or_cancel(cls, message: str) -> None:
        confirm_options = ['n', 'y']
        confirm = input(f'\n"{message}". Confirm? [y/n]: ').lower()
        while confirm not in confirm_options:
            confirm = input('\n❌ Wrong input. Try again [y/n]: ').lower()
        if confirm == 'y':
            GitAction.do_git_steps(message)
        else:
            print('\n❌ Operation cancelled.\n') 