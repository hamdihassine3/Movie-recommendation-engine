from database import *
from CollaborativeFiltering import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import pairwise_distances
from scipy.spatial.distance import pdist, squareform


conn=connection()

req_user="""SELECT * FROM user"""
user=execute_req(req_user)

req_item="""SELECT * FROM item"""
item=execute_req(req_item)

req_rating_base="""SELECT * FROM rating_base"""
rating=execute_req(req_rating_base)

n_users = len(user)
n_items = len(item)

#  we store the rating for each user-item pair in the matrix form (utility is our matrix)

utility = np.zeros((n_users, n_items))
for r in rating:
	base_user_id=0
	base_item_id=1
	base_rating=2
	base_timestamp=3
	utility[r[base_user_id] - 1][r[base_item_id] - 1] = r[base_rating]

#we will calculate in each loop Pairwise distances of train_data, calculate user_prediction using current k (numbers of top most similar users),
# calculate the evaluation and compare the result with the other evaluations 

best_rmse=10
best_user_prediction={}
for i in range(5,100,5):	
	# Create two user-item matrices , one for training and another for testing
	train_data, test_data = train_test_split(utility, test_size=0.2)
	
	#calculate similarity
	user_similarity = squareform(pdist(train_data, 'euclidean'))
	
	#calculate prediction
	user_prediction = predict(train_data, user_similarity, k=i)

	#calcul evaluation
	value_rmse=rmse(user_prediction, test_data)
	if(value_rmse<best_rmse):
		best_rmse=value_rmse
		best_user_prediction=user_prediction


print(best_user_prediction)
print 'User-based CF RMSE: ' + str(best_rmse) 








