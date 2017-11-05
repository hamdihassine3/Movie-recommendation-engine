import mysql.connector 

def connection():
	conn = mysql.connector.connect(host="localhost",user="root",password="", database="movies")
	return conn 

def execute_req(req):
	conn=connection()	
	cursor = conn.cursor()
	cursor.execute(req)
	rows = cursor.fetchall()
	return rows

def close_connection(conn):
	conn.close()






