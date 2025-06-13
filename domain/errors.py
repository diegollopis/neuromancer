from typing import Callable, Any, Optional
from functools import wraps
from enum import Enum, auto

class ErrorSeverity(Enum):
    """Níveis de severidade dos erros."""
    INFO = auto()      # Apenas informativo
    WARNING = auto()   # Aviso, mas não impede a operação
    ERROR = auto()     # Erro que impede a operação
    CRITICAL = auto()  # Erro crítico que pode afetar o sistema

class GitError(Exception):
    """Classe base para erros relacionados ao Git."""
    
    def __init__(
        self,
        message: str,
        severity: ErrorSeverity = ErrorSeverity.ERROR,
        details: Optional[str] = None,
        suggestion: Optional[str] = None
    ):
        """
        Inicializa o erro.
        
        Args:
            message: Mensagem principal do erro
            severity: Nível de severidade do erro
            details: Detalhes adicionais sobre o erro (opcional)
            suggestion: Sugestão de como resolver o erro (opcional)
        """
        self.message = message
        self.severity = severity
        self.details = details
        self.suggestion = suggestion
        super().__init__(self._format_message())
    
    def _format_message(self) -> str:
        """Formata a mensagem completa do erro."""
        msg = f"\n❌ {self.message}"
        
        if self.details:
            msg += f"\n\nDetalhes:\n{self.details}"
        
        if self.suggestion:
            msg += f"\n\nSugestão:\n{self.suggestion}"
        
        return msg
    
    def __str__(self) -> str:
        """Retorna a mensagem formatada do erro."""
        return self._format_message()

class InternetConnectionError(GitError):
    """Erro quando não há conexão com a internet."""
    def __init__(self, message: str = "Sem conexão com a internet"):
        super().__init__(
            message=message,
            severity=ErrorSeverity.ERROR,
            suggestion="Verifique sua conexão com a internet e tente novamente."
        )

class AuthorizationError(GitError):
    """Erro quando não há autorização para acessar o repositório."""
    def __init__(
        self,
        message: str,
        details: Optional[str] = None,
        suggestion: Optional[str] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.ERROR,
            details=details,
            suggestion=suggestion or "Verifique suas credenciais e permissões de acesso."
        )

class NotGitRepositoryError(GitError):
    """Erro quando o diretório não é um repositório Git."""
    def __init__(self, path: str):
        super().__init__(
            message=f"O diretório '{path}' não é um repositório Git",
            severity=ErrorSeverity.ERROR,
            suggestion="Execute 'git init' para inicializar um repositório Git."
        )

class NoChangesError(GitError):
    """Erro quando não há mudanças para commitar."""
    def __init__(self, message: str = "Não há mudanças para commitar"):
        super().__init__(
            message=message,
            severity=ErrorSeverity.WARNING,
            suggestion="Faça algumas alterações nos arquivos antes de tentar commitar."
        )

class ValidationError(GitError):
    """Erro quando há problemas com os argumentos do commit."""
    def __init__(
        self,
        message: str,
        details: Optional[str] = None,
        suggestion: Optional[str] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.ERROR,
            details=details,
            suggestion=suggestion or "Use 'python app.py help' para ver os tipos de commit disponíveis."
        )

class GitOperationError(GitError):
    """Erro quando uma operação do Git falha."""
    def __init__(
        self,
        operation: str,
        error: str,
        details: Optional[str] = None
    ):
        super().__init__(
            message=f"Erro ao executar operação '{operation}'",
            severity=ErrorSeverity.ERROR,
            details=f"Erro: {error}\n{details if details else ''}",
            suggestion="Verifique o status do repositório com 'git status'."
        )

def handle_git_errors(func: Callable) -> Callable:
    """
    Decorator para tratar erros do Git de forma centralizada.
    
    Este decorator:
    1. Captura exceções GitError
    2. Formata a mensagem de erro
    3. Retorna None em caso de erro
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except GitError as e:
            if e.severity == ErrorSeverity.CRITICAL:
                print(f"\n💥 {e.message}")
            elif e.severity == ErrorSeverity.WARNING:
                print(f"\n⚠️ {e.message}")
            else:
                print(str(e))
            return None
        except Exception as e:
            print(f"\n❌ Erro inesperado: {str(e)}")
            return None
    return wrapper 