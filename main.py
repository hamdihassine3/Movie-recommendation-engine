from database import *
from CollaborativeFiltering import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import pairwise_distances
from scipy.spatial.distance import pdist, squareform


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

#req_rating_test="""SELECT * FROM rating_test"""
#rating_test=execute_req(req_rating_test)


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

#we will calculate in each loop Pairwise distances of train_data, calculate user_prediction ,
# calculate the evaluation and comare the result with the other evaluations 
L=['braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation', 'cosine', 'euclidean', 'hamming','minkowski','sqeuclidean']
best_rmse=10
best_user_prediction={}
for i in range(10):	
	# Create two user-item matrices , one for training and another for testing
	train_data, test_data = train_test_split(utility, test_size=0.25)
	#calculate similarity
	user_similarity = squareform(pdist(train_data, L[i]))
	#calculate preduction
	#item_prediction = predict(train_data, item_similarity, type='item')
	user_prediction = predict(train_data, user_similarity, type='user')
	#calcul evaluation
	value_rmse=rmse(user_prediction, test_data)
	if(value_rmse<best_rmse):
		best_rmse=value_rmse
		best_user_prediction=user_prediction


print(best_user_prediction)
print 'User-based CF RMSE: ' + str(best_rmse) 

#print 'User-based CF RMSE: ' + str(rmse(user_prediction, test_data)) 
#print 'Item-based CF RMSE: ' + str(rmse(item_prediction, test_data))


#on peut utiliser cette partie a la fin pour faire plus de test en utilisant la table rating_test de notre base 
"""
test = np.zeros((n_users, n_items))
for r in rating_test:
	test_user_id=0
	test_item_id=1
	test_rating=2
	test_timestamp=3
	test[r[test_user_id] - 1][r[test_item_id] - 1] = r[test_rating]
"""






