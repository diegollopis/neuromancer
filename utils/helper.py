from os import system as cmd
from config import (
    COMMIT_MESSAGE_EXAMPLE,
    COMMIT_MESSAGE_TYPES,
    COMMIT_MESSAGE_REFERENCES
)

class Helper:
    """Helper class for commit message conventions."""

    commit_message_example = COMMIT_MESSAGE_EXAMPLE
    commit_message_types = COMMIT_MESSAGE_TYPES
    references = COMMIT_MESSAGE_REFERENCES

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