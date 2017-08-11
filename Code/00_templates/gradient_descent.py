import numpy as np

## Gradient Descent

X = np.array([[-9, -7, -1],
            [ 6, -5, -2],
            [-7, -1,  8],
            [ 3, -1,  6]])

y = np.array([[-26],
            [-10],
            [ 15],
            [ 19]])

##derivative of function =  -2/N * (y -X*beta) * X
#X.shape =(4,3)
#y.shape=(4,1)
#beta.shape(3,1)

 '''
 -2/4 * y - X.dot(beta).T.dot(X)
 '''

#y - (x1*B1 + x2*B2 +x3*B3)x1 + y - (x1*B1 + x2*B2 +x3*B3)x2 + y - (x1*B1 + x2*B2 +x3*B3)x3

gradient = ([22.5, -41, -106.5])

##beta update##
beta_new = beta + 0.001 * G
beta_new = [1.00225, .9959, .98935]
