import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt


# define the predict function 
def predict(ratings, similarity, k=20):
    pred = np.zeros(ratings.shape)

    for i in xrange(ratings.shape[0]):
        top_k_users = [np.argsort(similarity[:,i])[:-k-1:-1]]
        for j in xrange(ratings.shape[1]):
            pred[i, j] = similarity[i, :][top_k_users].dot(ratings[:, j][top_k_users]) 
            pred[i, j] /= np.sum(np.abs(similarity[i, :][top_k_users]))
   
    
    return pred




#Evaluation
def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

