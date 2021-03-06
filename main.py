"""
Desafio GnTech 1
Escreva uma função utilizando a linguagem python que faça a conexão com o banco de dados Postgres,
essa função deve:
a) criar uma tabela;
b) inserir uma linha contendo uma coluna indexada, uma coluna texto, uma coluna numérica,
uma coluna booleana e uma coluna datetime;
c) faça o versionamento no github ou gitlab.
"""
import psycopg2


# função para conectar com Banco de Dados PostgreSQL
def conecta_db():
    con = psycopg2.connect(host='localhost',
                           database='desafiogt1',
                           user='postgres',
                           password='1234')
    return con


# Função para criar tabela no PostgreSQL
def criar_tabela(tabela):
    sql = f'CREATE TABLE {tabela}(' \
          f'id serial NOT NULL, ' \
          f'texto varchar(50), ' \
          f'numero int, ' \
          f'opcao bit, ' \
          f'data date, ' \
          f'PRIMARY KEY (id));'
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


# Função para inserir dados em uma tabela PostgreSQL
def insere_dados(tabela, text, num, op, dat):
    sql = f"INSERT INTO {tabela} (texto, numero, opcao, data) VALUES " \
          f"('{text}', '{num}', '{op}', '{dat}');"
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


# Função para executar comando SQL no PostgreSQL
def executar_comando(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


# Função para apagar tabela no PostgreSQL
def apaga_tabela(tabela):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(f'DROP TABLE IF EXISTS {tabela};')
    con.commit()
    con.close()


# nome da tabela a ser manipulada
nomedatabela = 'desafiogt1'

# dados a serem inseridos no Banco de Dados
texto = 'São José-SC'
numero = '111444777'
opcao = '1'
data = '2021-09-11'

# comandos usando funções para manipular PostgreSQL, basta retirar o '#' do início da linha
# criar_tabela(nomedatabela)
# insere_dados(nomedatabela, texto, numero, opcao, data)
# apaga_tabela(nomedatabela)
