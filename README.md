# Algorithm Ownership 

Geração de matrizes que indicam a relação de responsabilidade entre os principais contribuidores e os módulos de um sistema.

## Descrição

Esta ferramenta utiliza como entrada bases de dados em CSV geradas pela mineração de repositórios com o framework [PyDriller](https://github.com/ishepard/pydriller). A partir desses dados, a ferramenta é capaz de automaticamente detectar os principais módulos do repositório, definir a responsabilidade de cada módulo para cada desenvolvedor e gerar uma matriz contendo a relação desses dados. Para isso, basta informar o nome do arquivo de saída e o separador dos valores.

## Instalação e Uso

1. Clone o repositório e acesse o diretório `algorithm-ownership`:

```bash
:~$ git https://github.com/rafaeldcx/algorithm-ownership
:~$ cd algorithm-ownership
```

2. O código principal está no arquivo main.py. Por padrão, ele está configurado para utilizar um exemplo com o arquivo data_FreeRTOS.csv. Para rodar o exemplo, basta executar o seguinte comando:

```bash
:~$ python3 main.py
```
Isso irá gerar uma matriz de propriedade no arquivo exemplo.csv dentro do diretório principal.Na execução, o programa mostrará que está "Calculando a propriedade...", indicando uma lista de diretórios e os valores de centralidade desses diretórios dentro do projeto. O programa demonstra a geração do arquivo CSV com a mensagem "Salvando em exemplo.csv". Após gerar esse arquivo, ele exibirá a mensagem "Escrito com sucesso".

## **Personalizando o Código**

Para utilizar outros exemplos ou bases de dados próprias, siga os passos abaixo:

Abra o diretório algorithm-ownership.
Abra o arquivo main.py em um editor de texto.
Altere o caminho do arquivo de entrada na função recursos.criar_recursos_pydriller(). Exemplo:

```python

recursos.criar_recursos_pydriller("../../algorithm-ownership/data/data_amazon-freertos.csv")
```
Para alterar o nome do arquivo de saída, edite a função mom.save():

```python

mom.save("seu_arquivo_saida.csv")
```
Após realizar as alterações, execute novamente o programa com:

```bash

:~$ python3 main.py
```

## Acessando os Notebooks de Análise

Dentro do repositório, existe um diretório chamado `data analysis` que contém notebooks Jupyter para cada projeto, organizados em pastas específicas. Esses notebooks fornecem análises detalhadas dos dados de cada projeto.

### Abrindo os Notebooks

Você pode abrir os notebooks de três maneiras: localmente no Jupyter Notebook, no [Google Colab](https://colab.google/) ou em uma versão online do Jupyter, como o [JupyterLite](https://jupyter.org/try-jupyter/lab/). Basta executá-los nas ferramentas citadas.




