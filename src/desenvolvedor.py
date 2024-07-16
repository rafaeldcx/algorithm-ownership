from collections import defaultdict
import recursos as Rec
import metodos as Met
from typing import List

class Desenvolvedor:
    """Classe representando um desenvolvedor."""

    def __init__(self, nome: str, email: str):
        """Inicializa um novo desenvolvedor com nome, email e propriedades padrão."""
        self.nome: str = nome
        self.email: str = email
        self.propriedades = defaultdict(float)
        self.tem_propriedade = defaultdict(float)
        self.arquivos: List[str] = []

    def calcular_propriedade(self):
        """Calcula a propriedade do desenvolvedor sobre os arquivos."""
        rec = Rec.Recursos.get_instance()
        met = Met.Metodos
        self.propriedades = {arquivo: met.doa(self.nome, arquivo) for arquivo in rec.arquivos}
      

    def e_proprietario(self, lim_normalizado:float, lim_absoluto:float, valor_normalizado:float, valor_absoluto:float):
        if valor_normalizado >= lim_normalizado and valor_absoluto >= lim_absoluto:
            return True
        return False

    def __rpr__(self):
        """Retorna uma representação em string do desenvolvedor."""
        return "Desenvolvedor [nome={}, email={}]".format(self.nome, self.email)
    
    