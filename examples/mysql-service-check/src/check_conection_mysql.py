import pymysql
import os

#variable host
HOSTCONECTION = os.environ['HOSTCONECTION']

try:
	conexion = pymysql.connect(host=HOSTCONECTION,
                             user='root',
                             password='pass1234',
                             db='peliculas')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)