import pandas as pd
import desenvolvedor as Dev
import commit as Com
import limpeza as Lim
import modificacao as Mod
from typing import List

class Recursos:
    SEPARADOR = ","
    rec = None

    @staticmethod
    def get_instance():
        if Recursos.rec is None:
            Recursos.rec = Recursos()
        return Recursos.rec

    def __init__(self):
        self.desenvolvedores: List[Dev.Desenvolvedor] = []
        self.arquivos: List[str] = []
        self.commits: List[Com.Commit] = []
        self.arquivos_scan_code: List[str] = []

    def set_desenvolvedores(self):
        for commit in self.commits:
            flag = False
            for dev in self.desenvolvedores:
                if dev.nome == commit.autor.nome:
                    flag = True
                    break
            if not flag:
                self.desenvolvedores.append(commit.autor)

            flag = False
            for dev in self.desenvolvedores:
                if dev.nome == commit.committer.nome:
                    flag = True
                    break
            if not flag:
                self.desenvolvedores.append(commit.committer)

    def set_arquivos(self):
        for commit in self.commits:
            for modificacao in commit.modificacoes:
                if modificacao.nome_arquivo_atual not in self.arquivos:
                    self.arquivos.append(modificacao.nome_arquivo_atual)

    def transforma_digito(self, s: str) -> int:
        aux = ""
        for c in s:
            if c.isdigit():
                aux += c
        return int(aux) if aux else 0

    def remove_separador(self, s: str) -> str:
        aux = ""
        for char in s:
            if char != self.SEPARADOR and char != '\n':
                aux += char
        return aux

    def ler_commit(self, linha: List[str]) -> Com.Commit:
        hash = linha[0]
        tipo_modificacao = linha[1]
        nome_arquivo_atual = linha[2]
        nome_arquivo_antigo = linha[3]
        nome_arquivo_novo = linha[4]
        nome_autor = linha[6]
        email_autor = linha[7]
        nome_committer = linha[9]
        email_committer = linha[10]

        autor = Dev.Desenvolvedor(nome_autor, email_autor)
        committer = Dev.Desenvolvedor(nome_committer, email_committer)
        modificacao = Mod.Modificacao(tipo_modificacao, nome_arquivo_atual, nome_arquivo_antigo, nome_arquivo_novo)
        
        modificacoes = [modificacao]
        
        commit = Com.Commit(hash, autor, committer, None, None, None, modificacoes)
        return commit
    
    def criar_recursos_pydriller(self, diretorio_arquivo: str):
        try:
            df = pd.read_csv(diretorio_arquivo, sep=self.SEPARADOR, encoding='latin-1')

            for index, row in df.iterrows():
                if row.isna().any():
                    print("Linha vazia")
                    continue
                linha = row.tolist()
                flag = False

                if len(linha) != 12:
                    continue

                hash = linha[0]

                for commit in self.commits:
                    if commit.hash_commit == hash:
                        tipo_modificacao = linha[1]
                        nome_arquivo_atual = linha[2]
                        nome_arquivo_antigo = linha[3]
                        nome_arquivo_novo = linha[4]

                        modificacao = Mod.Modificacao(tipo_modificacao, nome_arquivo_atual, nome_arquivo_antigo, nome_arquivo_novo)
                        commit.modificacoes.append(modificacao)
                        flag = True
                        break

                if not flag:
                    novo_commit = self.ler_commit(linha)
                    if novo_commit:
                        self.commits.append(novo_commit)

            Lim.Limpeza.alterar_diretorios_renomeados()
            self.set_desenvolvedores()
            self.set_arquivos()

        except IOError as e:
            print("Erro ao abrir o arquivo:", e) 
   