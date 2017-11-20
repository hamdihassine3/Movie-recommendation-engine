from database import *
import numpy as np



conn=connection()

#test database
"""
for row in rows:
	print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))
	
close_connection(conn)	
"""

req_user="""SELECT * FROM user"""
user=execute_req(req_user)

req_item="""SELECT * FROM item"""
item=execute_req(req_item)

req_rating_base="""SELECT * FROM rating_base"""
rating=execute_req(req_rating_base)

req_rating_test="""SELECT * FROM rating_test"""
rating_test=execute_req(req_rating_test)


n_users = len(user)
n_items = len(item)


# The utility matrix is used to store the rating for each user-item pair in the
# matrix form

utility = np.zeros((n_users, n_items))
for r in rating:
	var_user_id=0
	var_item_id=1
	var_rating=2
	var_timestamp=3
	utility[r[var_user_id] - 1][r[var_item_id] - 1] = r[var_rating]
 

   
print(utility)