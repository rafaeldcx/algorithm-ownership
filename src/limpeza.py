import recursos as Rec
import modificacao as Mod
import commit as Com

class Limpeza:
    """Classe para realizar operações de limpeza nos dados."""

    @staticmethod
    def alterar_diretorios_renomeados():
        """Altera os nomes dos diretórios que foram renomeados em todos os commits."""
        commit: Com.Commit
        modificacao: Mod.Modificacao
        commit1: Com.Commit
        modificacao1: Mod.Modificacao
        for commit in Rec.Recursos().commits:
            for modificacao in commit.modificacoes:
                if modificacao.tipo == "RENAME":
                    for commit1 in Rec.Recursos().commits:
                        for modificacao1 in commit1.modificacoes:
                            if modificacao1.nome_arquivo_atual == modificacao.nome_arquivo_antigo:
                                modificacao1.nome_arquivo_atual = modificacao.nome_arquivo_atual