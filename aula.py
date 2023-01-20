import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='bdyoutube',
)

cursor = conexao.cursor()

# CRUD | ao editar o banco de dados, temos que usar um conexao.commit()

# CREATE
nome_produto = "Toddynho"
valor = 4
comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()  # Usa-se ao editar o banco de dados
resultado = cursor.fetchall()  # Usa-se ao ler o banco de dados

# READ
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
#conexao.commit()  # Usa-se ao editar o banco de dados
resultado = cursor.fetchall()  # Usa-se ao ler o banco de dados
print(resultado)

# UPDATE
nome_produto = "Toddynho"
valor = 87
idvendas = 3
comando = f'UPDATE vendas SET valor = {valor} WHERE idvendas = "{idvendas}"'
cursor.execute(comando)
conexao.commit()  # Usa-se ao editar o banco de dados

#DELETE

comando = 'DELETE FROM vendas WHERE valor="87"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()
