import recursos as Rec
from math import log


class Metodos:
    """Classe com métodos para cálculo de propriedades."""
    @staticmethod
    def first_autorship(md: str, fp: str) -> int:
        for c in Rec.Recursos().commits:
            if c.autor.nome == md:
                if any(m.nome_arquivo_atual == fp and m.tipo == "ADD" for m in c.modificacoes):
                    return 1
        return 0

    @staticmethod
    def deliveries(md: str, fp: str) -> int:
        rec = Rec.Recursos.get_instance()
        return sum(
            1 for c in rec.commits 
            if c.autor.nome == md or c.committer.nome == md 
            for m in c.modificacoes 
            if m.nome_arquivo_atual.startswith(fp)
        )

    @staticmethod
    def acceptances(md: str, fp: str) -> int:
        rec = Rec.Recursos.get_instance()
        return sum(
            1 for c in rec.commits 
            if c.autor.nome != md and c.committer.nome != md 
            for m in c.modificacoes 
            if m.nome_arquivo_atual == fp
        )

    @staticmethod
    def doa(md: str, fp: str) -> float:
        return 3.293 + 1.098 * Metodos.first_autorship(md, fp) + 0.164 * Metodos.deliveries(md, fp) - 0.321 * log(1 + Metodos.acceptances(md, fp))

    def centralidade(modulo: str) -> int:
        rec = Rec.Recursos.get_instance()
        return sum(1 for d in rec.desenvolvedores if Metodos.deliveries(d.nome, modulo) > 0)