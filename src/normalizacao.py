class Normalizacao:
    @staticmethod
    def normalizar(valores):
        valores_normalizados = []
        porcentagem = 0
        maior_valor = max(valores, default=0)

        if maior_valor != 0:
            porcentagem = (1 - maior_valor) / maior_valor

        for valor in valores:
            valores_normalizados.append(valor + (porcentagem * valor))

        return valores_normalizados
