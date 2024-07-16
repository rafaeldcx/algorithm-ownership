class Modificacao:
    def __init__(self, tipo, nome_arquivo_atual, nome_arquivo_antigo, nome_arquivo_novo):
        self.tipo:str = tipo
        self.nome_arquivo_atual:str = nome_arquivo_atual
        self.nome_arquivo_antigo:str = nome_arquivo_antigo
        self.nome_arquivo_novo:str = nome_arquivo_novo

    def __str__(self):
        return f"Modificacao [tipo={self.tipo}, nome_arquivo_atual={self.nome_arquivo_atual}, " \
               f"nome_arquivo_antigo={self.nome_arquivo_antigo}, nome_arquivo_novo={self.nome_arquivo_novo}]"
    
    __rpr__ = __str__