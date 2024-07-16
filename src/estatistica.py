import random
from math import sqrt

class Estatistica:
    @staticmethod
    def kMeans(amostra, k):
        amostra_copia = amostra.copy()

        centroids = random.sample(amostra_copia, k)
        clusters = [[] for _ in range(k)]
        clusters_copia = [[] for _ in range(k)]

        maior_valor = max(amostra)
        parada = 10

        while parada != 0:
            for valor in amostra:
                menor_distancia = maior_valor
                distancia_por_valor = []

                for centroid in centroids:
                    distancia_por_valor.append(Estatistica.distanciaEuclidiana(centroid, valor))

                menor_distancia = min(distancia_por_valor)
                indice_menor = distancia_por_valor.index(menor_distancia)
                clusters[indice_menor].append(valor)

            centroids.clear()
            clusters_copia = [cluster.copy() for cluster in clusters]

            for i in range(k):
                centroids.append(Estatistica.media(clusters[i]))

            clusters = [[] for _ in range(k)]
            parada -= 1

        return clusters_copia

    @staticmethod
    def distanciaEuclidiana(num1, num2):
        return sqrt((num1 - num2) ** 2)

    @staticmethod
    def media(valores):
        if len(valores) == 0:
            return 0
        soma = sum(valores)
        return soma / len(valores)
