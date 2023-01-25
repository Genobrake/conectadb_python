from pymssql import _mssql

server = 'UDRUCA058ST'
user = 'sa'
password = '150480'
database = 'ControlMad'
conn = _mssql.connect(server = server, user = user, password = password, database = database)