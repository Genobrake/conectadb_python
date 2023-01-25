#Conexión a msssql con pymssql
import pymssql

server = 'UDRUCA058ST'
user = 'sa'
password = '150480'
database = 'MAESTROS_ODSIS'

conn = pymssql.connect(server, user, password, database)
#cursor = conn.cursor()
cursor = conn.cursor(as_dict = True)    #Permite referenciar las columnas de la tabla

cursor.execute('Select * From tmpEncuesta')
row = cursor.fetchone()
while row:
    #print ("CodRENAES=%s, CodSIS=%s, NombreEESS=%s" % (row[0], row[1], row[2]))
    print ("CodRENAES=%s, CodSIS=%s, NombreEESS=%s" % (row['CodRENAES'], row['CodSIS'], row['NombreEESS']))
    row = cursor.fetchone()

conn.close()

############################
#Conexión a mssql con _mssql
""" from pymssql import _mssql

server = 'UDRUCA058ST'
user = 'sa'
password = '150480'
database = 'MAESTROS_ODSIS'
conn = _mssql.connect(server = server, user = user, password = password, database = database)
# conn = _mssql.connect(server='UDRUCA058ST', user='sa', password='150480', \
#     database='MAESTROS_ODSIS')

conn.execute_query ('Select * From tmpEncuesta')
for row in conn:
    print ("CodRENAES=%s, CodSIS=%s, NombreEESS=%s" % (row['CodRENAES'], row['CodSIS'], row['NombreEESS'])) """