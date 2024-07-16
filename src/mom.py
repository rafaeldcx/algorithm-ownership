import recursos as Rec
import normalizacao as Nor
import metodos as Met
import desenvolvedor as Dev
from typing import List
from collections import defaultdict
import csv

class Mom:
    def __init__(self):
        self.modulos: list[str] = []
        self.desenvolvedores: list[Dev.Desenvolvedor] = Rec.Recursos.get_instance().desenvolvedores
        self.propriedades: list[list[float]] = []

    def iniciar_modulos(self, arquivos: List[str]) -> List[str]:
        try:
            modulos_list: list[str] = []
            for arquivo in arquivos:
                dir = arquivo.split("/")
                if dir[0] not in modulos_list:
                    modulos_list.append(dir[0])
            return modulos_list
        except Exception as e:
            print(f"Erro ao iniciar módulos: {e}")
            

    def principais_modulos_centralidade(self, media_equipe: int):
        try:
            
            modulos_list: List[str] = self.iniciar_modulos(Rec.Recursos.get_instance().arquivos)
            print(f"modulos_list: {modulos_list}")  # Debug print

            centralidade_por_modulo: dict[str, int] = defaultdict(int)
            arquivo: str
            modulo: str
            novo_modulo: str
        
            #novo_dicionario = {modulo: Met.Metodos.centralidade(modulo) for modulo in modulos_list}
            #centralidade_por_modulo.update(novo_dicionario)
            for modulo in modulos_list:
                centralidade_por_modulo[modulo] = Met.Metodos.centralidade(modulo)
                print(f' {modulo}: {centralidade_por_modulo[modulo]}')  # Debug print
            
            for modulo in modulos_list:
                centralidade: int = centralidade_por_modulo[modulo]
                if centralidade >= media_equipe:
                    for arquivo in Rec.Recursos.get_instance().arquivos:
                        novo_modulo = self.gerar_modulo(modulo, arquivo, media_equipe)
                        if novo_modulo is not None:
                            aux:list[str] = novo_modulo.split(",")
                            for s in aux:
                                if s not in self.modulos and s is not None:
                                    self.modulos.append(s)
            print(f"Modulos: {self.modulos}")  # Debug print               
        except Exception as e:
            print(f"Error in principais_modulos_centralidade: {e}")

    def gerar_modulo(self, modulo: str, arquivo: str, media_equipe: int):
        try:
            if arquivo.startswith(modulo):
                if arquivo == modulo:
                    return arquivo
                modulo_split = modulo.split("/")
                arquivo_split = arquivo.split("/")
                try:
                    novo_modulo = arquivo[:len(modulo) + 1 + len(arquivo_split[len(modulo_split)])]
                    centralidade = Met.Metodos.centralidade(novo_modulo)
                    if centralidade >= media_equipe:
                        return novo_modulo + "," + self.gerar_modulo(novo_modulo, arquivo, media_equipe)
                except Exception:
                    return None
            return None
        except Exception as e:
            print(f"Error in gerar_modulo: {e}")

    def calcular_propriedade_mom(self):
        try:
            rec = Rec.Recursos.get_instance()
            print("Calculando propriedade...")
            self.principais_modulos_centralidade(5)

            for d in self.desenvolvedores:
                d.calcular_propriedade()

            propriedades_arquivos: list[list[float]] = []
            for arquivo in rec.arquivos:
                propriedades_arquivo: list[float] = []
                for d in self.desenvolvedores:
                    propriedades_arquivo.append(d.propriedades.get(arquivo, 0))
                #print(f"Propriedades do arquivo após adicionar um desenvolvedor: {propriedades_arquivo}")
                propriedades_arquivos.append(propriedades_arquivo)

            propriedades_arquivos_normalizadas: list[list[float]] = []

            for propriedades_arquivos_list in propriedades_arquivos:
                propriedades_normalizadas = Nor.Normalizacao.normalizar(propriedades_arquivos_list)
                #print(f"Propriedades normalizadas: {propriedades_normalizadas}")
                propriedades_arquivos_normalizadas.append(propriedades_normalizadas)

            hash_proprietarios: dict[str, list[Dev.Desenvolvedor]] = defaultdict(list)

            for modulo in self.modulos:
                propriedade_list = []

                for i in range(len(self.desenvolvedores)):
                    soma_arquivos = 0
                    soma_propriedades = 0

                    recursos = Rec.Recursos.get_instance().arquivos
                    for j in range(len(recursos)):
                        if recursos[j].startswith(modulo):
                            soma_arquivos += 1
                            if self.desenvolvedores[i].e_proprietario(
                                0.75, 3.293, propriedades_arquivos_normalizadas[j][i], propriedades_arquivos[j][i]
                            ):
                                soma_propriedades += 1
                                if recursos[j] not in self.desenvolvedores[i].arquivos:
                                    self.desenvolvedores[i].arquivos.append(recursos[j])
                                if recursos[j] not in hash_proprietarios:
                                    hash_proprietarios[recursos[j]] = []
                                    hash_proprietarios[recursos[j]].append(self.desenvolvedores[i])
                                elif self.desenvolvedores[i] not in hash_proprietarios[recursos[j]]:
                                    hash_proprietarios[recursos[j]].append(self.desenvolvedores[i])

                    porcentagem_i = (soma_propriedades / soma_arquivos) * 100 if soma_arquivos > 0 else 0
                    porcentagem_arquivo = 100 / soma_arquivos if soma_arquivos > 0 else 0
                    divisao = 0.0
                    cont = 0.0

                    if porcentagem_i >= 5:
                        for arquivo in self.desenvolvedores[i].arquivos:
                            if arquivo.startswith(modulo) and hash_proprietarios[arquivo] is not None:
                                divisao = 1.0 / len(hash_proprietarios[arquivo])

                                for dev in hash_proprietarios[arquivo]:
                                    x: int = self.desenvolvedores.index(dev)
                                    self.desenvolvedores[x].tem_propriedade[arquivo] = divisao
                                    aux = 0.0

                                    if x < len(propriedade_list):
                                        for arq in self.desenvolvedores[x].arquivos:
                                            if arq.startswith(modulo):
                                                if self.desenvolvedores[x].tem_propriedade[arq] is not None:
                                                    aux += self.desenvolvedores[x].tem_propriedade[arq]

                                        porcent_nova = aux * porcentagem_arquivo
                                        propriedade_list[x] = porcent_nova

                                cont += divisao

                    porcentagem = cont * porcentagem_arquivo
                    propriedade_list.append(porcentagem)

                self.propriedades.append(propriedade_list)
                print(f"Propriedades do módulo {modulo}: {propriedade_list}")

        except Exception as e:
            print(f"Error in calcular_propriedade: {e}")

    def save(self, nome_arquivo: str):
        try:
            print(f"Salvando em {nome_arquivo}...")
            with open(nome_arquivo, 'a', newline='') as file:
                writer = csv.writer(file)

                # Escrevendo os nomes dos desenvolvedores
                writer.writerow([''] + [d.nome for d in self.desenvolvedores])

                # Escrevendo os e-mails dos desenvolvedores
                writer.writerow([''] + [d.email for d in self.desenvolvedores])

                # Escrevendo as propriedades de cada módulo
                for modulo, propriedades_modulo in zip(self.modulos, self.propriedades):
                    writer.writerow([modulo] + propriedades_modulo)
                    
            print("Escrito com sucesso.")
        except Exception as e:
            print(f"Error in save: {e}")


    