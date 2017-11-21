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
	base_user_id=0
	base_item_id=1
	base_rating=2
	base_timestamp=3
	utility[r[base_user_id] - 1][r[base_item_id] - 1] = r[base_rating]
 

test = np.zeros((n_users, n_items))
for r in rating_test:
	test_user_id=0
	test_item_id=1
	test_rating=2
	test_timestamp=3
	test[r[test_user_id] - 1][r[test_item_id] - 1] = r[test_rating]

#print(utility)
print(test)





