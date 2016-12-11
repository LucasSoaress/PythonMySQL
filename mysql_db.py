import pymysql

dataBase = pymysql.connect(host='localhost',user='root',password='',db='teste')

email = str(raw_input("Digite o seu email: "))
senha = str(raw_input("Digite uma senha para seu cadastro: "))
nome = str(raw_input("Digite seu nome: "))
cur = dataBase.cursor()

try:
	cur.execute("INSERT INTO usuarios (nome, email, senha) values (%s, %s, %s)",(nome,email,senha))
	dataBase.commit()
	print("Cadastro realizado com sucesso")
except Exception as e:
	print("Error ", e)


dataBase.close()
