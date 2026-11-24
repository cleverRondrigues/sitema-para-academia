
import sqlite3

# configurações
conexao = sqlite3.connect('alunos.db')
cursor = conexao.cursor()


# inputs (temporários)
# nome = input("Digite o nome do arquivo: ")
# idade = int(input("Digite a idade: "))
# peso = float(input("Digite o peso: "))
# altura = float(input("Digite a altura: ")) / 100


# defs
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


# sqlite3
def criar_tabela():
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        idade INTEGER,
                        peso REAL,
                        altura REAL,
                        imc TEXT
                    )''')
    conexao.commit()


def cadastrar_aluno(nome, idade, peso, altura):
    imc = calcular_imc(peso, altura)

    cursor.execute('''INSERT INTO alunos
        (nome, idade, peso, altura, imc)
        VALUES (?, ?, ?, ?, ?)''',
        (nome, idade, peso, altura, imc))

    conexao.commit()


def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    return cursor.fetchall()


def consultar_aluno(nome):
    cursor.execute(
        "SELECT * FROM alunos WHERE nome LIKE ?",
        (f"%{nome}%",)
    )
    return cursor.fetchall()


# chama as funções
criar_tabela()


# testes
# print("O IMC é: ", calcular_imc(peso, altura))
