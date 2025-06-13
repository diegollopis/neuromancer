from urllib import request
import subprocess
from typing import List
from .git_repository import GitRepository
from .errors import (
    InternetConnectionError,
    AuthorizationError,
    NoChangesError,
    GitOperationError
)

class GitEnvironment:
    """Responsible for verifying the Git environment."""
    
    def __init__(self, repo: GitRepository):
        """
        Initialize the Git environment checker.
        
        Args:
            repo: Git repository instance to be verified
        """
        self.repo = repo
    
    def check_internet_connection(self) -> bool:
        """
        Checks if there is an internet connection.
        
        Returns:
            bool: True if there is a connection
        
        Raises:
            InternetConnectionError: If there is no internet connection
        """
        try:
            request.urlopen('https://www.google.com', timeout=5)
            return True
        except Exception as e:
            raise InternetConnectionError(
                f"Sem conexão com a internet: {str(e)}"
            ) from e
    
    def check_repo_authorization(self) -> bool:
        """
        Checks if there is authorization to access the remote repository.
        
        Returns:
            bool: True if there is authorization
        
        Raises:
            AuthorizationError: If there is no authorization or if the remote is not configured
        """
        remote_url = self.repo.get_remote_url()
        if not remote_url:
            raise AuthorizationError(
                message="Repositório remoto não configurado",
                details="Use 'git remote add origin <url>' para configurar o repositório remoto.",
                suggestion="Configure o repositório remoto com 'git remote add origin <url>'"
            )
        
        try:
            # Primeiro tenta obter informações do repositório remoto
            fetch_result = self.repo.execute_git_command(
                ["git", "fetch", "--dry-run"],
                capture_output=True
            )
            
            # Se chegou aqui, tem autorização básica
            # Agora verifica se tem permissão de push
            current_branch = self.repo.get_current_branch()
            push_result = self.repo.execute_git_command(
                ["git", "push", "--dry-run", "origin", current_branch],
                capture_output=True
            )
            
            # Verifica se há erros específicos de permissão
            if "Permission denied" in push_result.stderr or "403" in push_result.stderr:
                raise AuthorizationError(
                    message="Sem permissão para fazer push no repositório",
                    details=f"Você não tem permissão para fazer push na branch {current_branch}",
                    suggestion="Verifique suas credenciais e permissões de acesso ao repositório"
                )
            
            return True
            
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.lower() if e.stderr else str(e).lower()
            
            if "permission denied" in error_msg or "403" in error_msg:
                raise AuthorizationError(
                    message="Sem permissão para acessar o repositório",
                    details="Suas credenciais não têm permissão para acessar este repositório",
                    suggestion="Verifique suas credenciais e permissões de acesso"
                )
            elif "not found" in error_msg or "404" in error_msg:
                raise AuthorizationError(
                    message="Repositório não encontrado",
                    details="O repositório remoto não existe ou não está acessível",
                    suggestion="Verifique se a URL do repositório está correta"
                )
            else:
                raise AuthorizationError(
                    message="Erro ao verificar autorização",
                    details=str(e),
                    suggestion="Verifique suas credenciais e permissões de acesso"
                )
            
        except subprocess.TimeoutExpired as e:
            raise AuthorizationError(
                message="Timeout ao conectar ao repositório remoto",
                details=str(e),
                suggestion="Verifique sua conexão com a internet e tente novamente"
            ) from e
        except Exception as e:
            raise AuthorizationError(
                message="Erro ao verificar autorização",
                details=str(e),
                suggestion="Verifique suas credenciais e permissões de acesso"
            ) from e
    
    def check_changed_files(self) -> bool:
        """
        Checks if there are modified files in the repository.
        
        Returns:
            bool: True if there are modifications
        
        Raises:
            NoChangesError: If there are no modifications
            GitOperationError: If there is an error checking files
        """
        try:
            # Check modified files
            modified = self.repo.execute_git_command(
                ['git', 'ls-files', '-m'],
                capture_output=True
            )
            
            # Check untracked files
            untracked = self.repo.execute_git_command(
                ['git', 'ls-files', '--others', '--exclude-standard'],
                capture_output=True
            )
            
            modified_files = modified.stdout.splitlines()
            untracked_files = untracked.stdout.splitlines()
            
            if not modified_files and not untracked_files:
                raise NoChangesError(
                    "Não há mudanças para commitar neste repositório"
                )
            
            return True
        except NoChangesError:
            raise
        except Exception as e:
            raise GitOperationError(
                operation="check_changed_files",
                error=str(e),
                details="Erro ao verificar arquivos modificados"
            ) from e 