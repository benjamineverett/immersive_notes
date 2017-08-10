## Week 3 Review Questions

1. ) Instantiate matrices A and B like:
``` python
A = np.arange(1, 17).reshape((4, 4))
B = np.ones((4, 3))
```
  a) Multiply matrices A and B.
  
  	**Adot(B)**

  b) Compute the euclidean distance between rows 1 and 3 of matrix A.
  
  	**np.linalg.norm(A[0] - A[2])**

  c) Compute the cosine similarity between columns 1 and 2 of matrix A.

 	**Transpose** 
 	
 	**A[:,0] -> gets first column**
 	
 d) Compute the transpose of B.
  
  	**B.T**

  e) Compute the inverse of A.
  
  	**see slack from Jordan**

2. Draw a confusion matrix for binary predictions.

	**

3. Give an example for each case:  

  * Precision is more important than recall. 
  	**court of law** 

  * Recall is more important than precision.  
  	**recall car seats**

  * You consider both to be important (and what metric would you use for that?)  

4. What are the assumptions behind OLS linear regression?
	
	**Model linear in parameters**
	**Random!**
	**Condition mean = 0**
	**No multi colinearity**
	**Spherical Errors: Homoscedastic errors preferred**
	**Errors should be normally distributed**

5. What are some metrics for linear regression goodness of fit, and what do they mean?

	**p-values of coefficients**
	**coefficients doesn't go through zero**
	**larger coefficient affecting output more**
	**adjusted R^2 for more than 1 feature**
	**f-statistic:**

6. In the context of machine learning, what are bias and variance?  And what is the bias-variance trade-off?

7. Explain what kFold cross-validation is and why it's used.

8. What is the curse of dimensionality?  How is it addressed?

9. We talked about L1 and L2 regularization.  What are they and in what situations might one be used instead of the other?

10. How is a ROC curve generated?  What does it show?

11. What are the similarities and differences between linear and logistic regression regression and how do you interpret the coefficients in each case?
