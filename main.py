from database import *

conn=connection()
req="""SELECT user_id, item_id, rating FROM rating_base"""
rows=execute_req(req)

#test database
for row in rows:
	print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))
	
close_connection(conn)	