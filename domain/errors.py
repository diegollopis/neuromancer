from typing import Callable, Any
from functools import wraps

class GitError(Exception):
    """Classe base para erros relacionados ao Git"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class InternetConnectionError(GitError):
    """Erro quando não há conexão com a internet"""
    pass

class AuthorizationError(GitError):
    """Erro quando não há autorização no repositório"""
    pass

class NotGitRepositoryError(GitError):
    """Erro quando o diretório não é um repositório Git"""
    pass

class NoChangesError(GitError):
    """Erro quando não há mudanças para commitar"""
    pass

class ValidationError(GitError):
    """Erro quando há problemas com os argumentos do commit"""
    pass

def handle_git_errors(func: Callable) -> Callable:
    """Decorator para tratar erros do Git de forma centralizada"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except GitError as e:
            print(f"\n❌ {e.message}\n")
            return None
        except Exception as e:
            print(f"\n❌ Erro inesperado: {str(e)}\n")
            return None
    return wrapper 