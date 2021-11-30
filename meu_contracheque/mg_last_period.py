import sys
import click
from meu_contracheque.scraping_mg import (scraping_process_begin,
                                         scraping_single_process,
                                         csv_register,
                                         clean_process)


def scraping_mg_last_period(masp, senha):
  """
  Função responsável pela busca de informações do último contracheque dos servidores do Estado de Minas Gerais.
  Parâmetros:
  -------
  masp: string
    Masp do servidor do Estado de Minas Gerais
  senha: string
    Senha de acesso ao Portal do servidor do Estado de Minas Gerais
  Retorna:
  -------
  Arquivo "contracheques.csv" atualizado com as informações do último contracheque disponível no Portal do Servidor.
  """
  try:
    clean_process()
    start = scraping_process_begin()
    driver = start[0]
    period = start[1]
    scraping_single_process(driver, period, masp, senha)
    driver.quit()
    csv_register()
  except:
    print('Não foi possível finalizar o processo de busca do contracheque mais recente.')
    sys.exit(1)

@click.command(name='mais-recente')
@click.option('--masp', '-m', envvar='MASP', required=True,
              help="Masp do servidor do Estado de Minas Gerais")
@click.option('--senha', '-s', envvar='PORTAL_PWD', required=True,
              help="Senha de acesso ao Portal do servidor do Estado de Minas Gerais")
def scraping_mg_last_period_cli(masp, senha):
  """
  Função CLI responsável pela busca de informações do último contracheque dos servidores do Estado de Minas Gerais.
  Por padrão, função buscará masp e senha nas variáveis de ambiente MASP e PORTAL_PWD cadastradas na máquina ou
  em arquivo .env.
  Parâmetros:
  ----------
  masp: string
      Masp do servidor do Estado de Minas Gerais
    senha: string
      Senha de acesso ao Portal do servidor do Estado de Minas Gerais
    Retorna:
    -------
    Arquivo "contracheques.csv" atualizado com as informações do último contracheque disponível no Portal do Servidor.
  """
  scraping_last_period(masp, senha)
