import mysql.connector

# Conectar ao banco de dados MariaDB
cnxn = mysql.connector.connect(
    host="localhost",     # Ou o IP do servidor MariaDB
    user="root",            # Seu usuário MariaDB
    password="",      # Sua senha MariaDB
    database="escola_py"  # Nome do banco de dados
)

# Criar um cursor para executar consultas
cursor = cnxn.cursor()

# Executar a consulta SQL
cursor.execute("SELECT matricula, nome FROM alunos")

# Obter e exibir os resultados
row = cursor.fetchone()
if row:
    print(f"Matricula: {row[0]}, Nome: {row[1]}")
else:
    print("Nenhum dado encontrado.")

# Fechar o cursor e a conexão
cursor.close()
cnxn.close()
