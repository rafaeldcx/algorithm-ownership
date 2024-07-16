import modificacao as Mod
import desenvolvedor as Dev
from typing import List
from datetime import datetime

class Commit:
    """Classe representando um commit."""

    def __init__(self, hash_commit, autor, committer, mensagem, data_autoria, data_commit, modificacoes: List[Mod.Modificacao]):
        """Inicializa um novo commit com os dados fornecidos."""
        self.hash_commit: str = hash_commit
        self.autor: Dev.Desenvolvedor = autor
        self.committer: Dev.Desenvolvedor = committer
        self.mensagem:str = mensagem
        self.data_autoria: datetime = data_autoria
        self.data_commit: datetime = data_commit
        self.modificacoes: List[Mod.Modificacao] = modificacoes

    def __rpr__(self):
        """Retorna uma representação em string do commit."""
        return (f"Commit [hash={self.hash_commit}, autor={self.autor}, committer={self.committer}, "
            f"mensagem={self.mensagem}, data_autoria={self.data_autoria}, data_commit={self.data_commit}, "
            f"modificacoes={self.modificacoes}]")
    
    
   