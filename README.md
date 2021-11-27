Meu Contracheque :bookmark_tabs:
===

## Sobre este repositório :open_book:

Meu contracheque é um pacote Python, acessível via interface CLI, utilizado para buscar informações de contracheques via web scraping.

A primeira versão deste pacote conta com a busca de contracheques dos servidores públicos do Estado de Minas Gerais, disponibilizados na aba "Emissão de Contracheque" do site [Portal do Servidor](https://www.portaldoservidor.mg.gov.br/index.php/servicos/emissao-de-contracheque).


## Orientações gerais

- Instalação de [Python 3](https://www.python.org/downloads/).

- Utilização de navegador Google Chrome.

- Não copie e cole os comandos abaixo cegamente, modifique os textos entre "< >" com as informações pertinente à sua realidade.

## Setup da máquina

Recomendo utilizar uma pasta específica para execução dos comandos do pacote, criando e ativando ambiente Python dentro da mesma, conforme sugerido abaixo:

#### Pasta para execução dos comandos e ativação de ambiente python

- Necessário instalação de [Python 3](https://www.python.org/downloads/) antes da execução os comandos abaixo para ambos os sistemas operacionais.

- Sistema operacional Linux:

```Terminal
# Criação da pasta para execução do projeto
$ mkdir <nome-desejado-para-pasta>

# Acessando a pasta criada
$ cd <nome-desejado-para-pasta>

# Criação ambiente python
$ python3 -m venv venv

# Ativação ambiente python
$ source venv/bin/activate
```

- Sistema operacional Windows:
  - Recomendo a utilização de Git Bash disponível com instalação de [Git para Windows](https://gitforwindows.org/).

```Terminal
# Criação da pasta para execução do projeto
$ mkdir <nome-desejado-para-pasta>

# Acessando a pasta criada
$ cd <nome-desejado-para-pasta>

# Criação ambiente python
$ python -m venv venv

# Ativação ambiente python
$ source venv/Scripts/activate
```

#### Instalação cromedriver

- Identifique a versão do navegador Chrome instalado em sua máquina digitando `chrome://version/` na barra de navegação do mesmo.

- Realize o download do [drive específico](https://chromedriver.storage.googleapis.com/index.html) para versão chrome instalada em sua máquina.

- Necessário descompactar arquivo baixado.

- Para sistema operacional Windows basta incluir o caminho do arquivo descompactado no path.

- Para sistema operacional Linux incluir o arquivo no caminho `/usr/local/bin`.

### Passando suas credenciais para buscar o contracheque

## Instalação

O `meu-contracheque` está disponível no Python Package Index - [PyPI](https://pypi.org/project/meu-contracheque/) e pode ser instalado utilizando-se o comando abaixo:

```bash
# Antes de executar o comando abaixo lembre-se que ambiente Python deverá estar ativo
$ pip install meu-contracheque
```

## Utilização

O resultado da execução dos comandos abaixo será a criação do arquivo "contracheques.csv". As informações retornadas estão organizadas em formato tabular.
Toda execução subscreve o arquivo "contracheques.csv" anteriormente gerado.

- Buscar informações do contracheque mais recente:

```Terminal
$ contracheque mg mais-recente
```

- Buscar informações de todos os contracheques emitidos:

```Terminal
$ contracheque mg todos
```

Obs.: Esta opção poderá demorar, a depender do número de contracheques a serem exportados. O log de execução do comando será exibido no terminal, facilitando o entendimento que está acontecendo.


## Encontrou algo errado no código ou quer melhorá-lo

Abra um [Issue](https://github.com/gabrielbdornas/meu-contracheque/issues) ou um [Pull Request](https://github.com/gabrielbdornas/meu-contracheque/pulls)!!!

Este tipo de contribuição auxiliará no crescimento do código de maneira exponencial!
