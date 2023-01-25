from dbConexion import conn

"""
from pymssql import _mssql

server = 'UDRUCA058ST'
user = 'sa'
password = '150480'
database = 'ControlMad'
conn = _mssql.connect(server = server, user = user, password = password, database = database)
"""

# conn = _mssql.connect(server='UDRUCA058ST', user='sa', password='150480', \
#     database='MAESTROS_ODSIS')

#print ("Ingresar Usuario: ")
usuario = str(input("Ingresar Usuario: "))

#print ("Ingresar Contraseña: ")
password = str(input("Ingresar Contraseña: "))

sqlcmd = """
Declare @res int
EXEC @res = sp_ValidarLogin
    @chrLogin = """ + usuario + """,
	@nvcPassword = """ + password + """
Select @res
"""

res = conn.execute_scalar(sqlcmd)
#res = conn.execute_scalar("exec sp_ValidarLogin " + usuario + ", " + password + "")
#print (res)

if res == 1:
    print ("Acceso permitido")
else:
    print ("Usuario y/o contraseña equivocados")

