**Include your code and answers in** `pair.py`.

You will find in `src/pair_helper.py` some plotting functions to help explore the decision boundaries of SVM.


## Part 1: Preprocessing data for SVM

Intuitively, it makes sense that SVMs might need scaling. Since SVMs are sensitive to the distance of points relative to a hyperplane, if one dimension had units in the thousands, the distance along that dimension would overwhelm another dimension with values in `[0,1]`. And the model would focus disproportionately on this larger dimension. Scaling overcomes this.

1\. Load the file `data/part1_unscaled.csv` into a dataframe. Use columns 1 and 2 as attributes and column 3 as response. Compute statistics on these attributes (mean, minimum and maximum) to observe their respective scales. You can also use a scatter plot (in `src/pair_helper.py` function `plot_data_basic`) to explore the classes inside that dataset.

2\. Fit the linear SVC on the training set without scaling the data (out of the box). Measure its score on the testing set. Check the values of the coefficients. What do you notice ?

3\. We will now use the [`StandardScaler`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html) to scale our attributes. StandardScaler is used similarly to a ML algorithm : you can learn a scaling model using `.fit()` and apply that scaling model using `.transform()`. When using scaling as an input for a machine learning algorithm, the good practice is to obtain a scaling model and a ML model from the training set, then to apply both on the testing set. This way, both the training set and the testing set are scaled homogeneously for the application of the ML algorithm.

   The class [`Pipeline`](http://scikit-learn.org/stable/modules/pipeline.html#pipeline) can help you to integrate both the `StandardScaler` and `SVC` into a single process. `Pipeline` is a good practice to keep track of the transformations leading up to fitting the predictive model. Below is a snippet demonstrating the use of `Pipeline`.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipeline = Pipeline([('scaler', StandardScaler()),
                        ('svc', SVC(kernel='linear'))])
pipeline.fit(x, y)
```

Apply [`StandardScaler`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html) and [`Pipeline`](http://scikit-learn.org/stable/modules/pipeline.html#pipeline) to fit a linear kernel `SVC` on your dataset. Measure the score on the testing set. Check the values of the coefficients. What do you notice ?

4\. Plot the decision boundary along with the data points (in `src/pair_helper.py` see function `plot_svm_decision`).

5\. Use `cross_val_score` to compute the average `accuracy` of a 5-fold cross validation of the scaled model versus the unscaled model.


## Part 2: Hyperparameter C

You have probably noticed that the dataset used in `Part 1` is not linearly separable. In reality, you will rarely encounter a dataset that is linearly separable. In such cases, SVMs have a tradeoff between maximizing the margin and minimizing the classification error. The hyperparameter `C` controls this tradeoff.

> **Warning**: Depending on your textbook, you may encounter `C` as in the convex optimization problem or as in the re-expressed dual form of this problem.
- _Introduction to Statistical Learning_ p346 considers `C` on the convex optimization problem and hence defines its behavior as "*when `C` is small, we seek narrow margins that are rarely violated [...] on the other hand when `C` is larger, the margin is wider and we allow more violations to it*".
- _Elements of Statistical Learning_ p421 relies on the dual form to define its behavior (inverse to ISL): "*larger values of `C` focus attention more on (correctly classified) points near the decision boundary while smaller values involve data further away*".

> **The implementation of `SVC` in `sklearn` relies on this second definition.**

We are going to try to see this behavior now (also see [this link](http://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel) for a schematic description). For this section, you can use `data/part2_scaled.csv` (it is a scaled version of `data/part1_unscaled.csv`).

1. For each value of `C` in `{0.01, 0.1, 1.0, 10.0, 100.0}`, use `plot_svm_decision` to plot the decision boundary obtained with an `SVC` using this value for `C`. How would you describe the influence of C on the decision boundary obtained ? What does happen for large values of C ?

## Part 3: Kernel Tricks

We will now challenge SVMs on another dataset that is not linearly separable. It will require us to use kernel functions. Load the dataset from file `data/part3_nonseparable.csv` and use it from now on.

SVMs can use kernel functions to transform the features into a new feature
space. Thus far we have been using a linear kernel, but SVMs can use non-linear
kernels.

Two of the most common nonlinear kernels are the polynomial kernel function and
the Gaussian kernel function (also known as the Radial Basis Function, or RBF).

Both of these kernels transform the data into a new space where the
data may be (more) linearly separable.

#### RBF Kernel

`K(x, z) = exp(gamma * (distance(x, z))^2)`

`gamma` is a hyperparameter that determines the spread of the Gaussian around each point. `distance` is Euclidean distance.

[Wikipedia - RBF
Kernel](http://en.wikipedia.org/wiki/Radial_basis_function_kernel)

#### Polynomial Kernel

`K(x, z) = (1 + x.T.dot(z))^d`


`d` is a hyperparameter that determines the degree of the polynomial transform.

[Wikipedia - Polynomial Kernel](http://en.wikipedia.org/wiki/Polynomial_kernel)

In practice, RBF kernels are more often used (scikit learn uses the RBF as the
default kernel in SVC). The polynomial kernel at high degrees often leads to
overfitting.

1\. Load the file `data/part3_nonseparable.csv` into a dataframe.

2\. Train your model using both the RBF kernel and the polynomial kernel out of the box. How does each perform on this dataset compared to the linear kernel in terms of cross-validated accuracy?

3\. Use the function below (in `src/pair_helper.py` function `decision_boundary`) to visualize non-linear decision boundaries of the models.

```python
def decision_boundary(clf, X, Y, h=.02):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1, figsize=(4, 3))
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.show()
```

<br>

## Part 4: Grid Search

We can use kernel tricks with SVM, but we can't just rely on out-of-the-box parameters. We need to tune our hyperparameters for each case. For the `poly` kernel, there are two hyperparameters: `C` as described above, and `degree` the degree of the polynomial kernel.

What we'd like to know is which combination of hyperparameters yields the best results.

Scikit-learn's [`grid_search`](http://scikit-learn.org/stable/modules/generated/sklearn.grid_search.GridSearchCV.html)
module has just what we need.

1\. Create an instance `g` of `GridSearchCV`, set `scoring='accuracy'` to set the scoring type to classification accuracy and `cv=10` to set the number of folds in K-fold CV to 10. Use that instance to find the best combination of values for `C` and `degree` using appropriate scales.

2\. Once `GridSearchCV` had found this combinarion, you can obtain the result of the grid search in `g.grid_scores_` and the winner in `g.best_params_`. Conduct a grid search over several possible values of `C` and `degree` and find out what the best combination is.

3\. Do the same for an `rbf` kernel searching over values of `C` and `gamma`.

4\. Compare the improvement in accuracy of doing a grid search in the RBF and polynomial models to the untuned models.

<br>

## Part 5: Unbalanced classes

Sometimes our data is unbalanced across classes (i.e. 95% of our data is class 0
and only 5% class 1). SVMs don't deal with this regime well and we need to take
action to correct it.

One method used to correct for class imbalance is weighting the training
examples by the inverse frequency of their class. That is, if a certain class is
only a small part of the dataset, we'd weight those examples more heavily so
that they have relatively equal weight to the more dominant class.

1\. You'll find an unbalanced dataset in `data/part5_unbalanced.csv`. Train 2 SVM models to do the classification, one with weighting and the other without. You can use the keyword argument
   `class_weight` in SVC's constructor to specify the class weights manually. Or you can have scikit-learn do it automatically for you by passing in `class_weight='balanced'`.

2\. Plot the decision boundaries of both models and see the difference weighting makes.

## Part 6: Real-world Modeling

In most cases, we won't be able to visualize our SVM solution, we'll have too many variables.
In such cases, we have to rely exclusively on cross-validation to select from among competing solutions.

You'll find in `data/svmguide1.csv` the [`svmguide1` dataset](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html) used in the [libsvm paper](http://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf) to assess performance of SVMs. It is an astroparticle application from Jan Conrad of Uppsala University, Sweden and consists in 7089 observations and 4 attibutes.

1\. Load the file `'data/svmguide1.csv'` into a dataframe.

2\. Try different models, kernels etc. and see which performs best in cross validation. Use `StandardScaler` to scale the data. Perform `GridSearchCV` as appropriate as it is a timely process. You should be able to achieve over **90% accuracy** with this dataset.t.

<br>

## Part 7: SVM Applications to Wide and Tall Data

In general, as the number of features increases, the gain of accuracy of using an RBF kernel instead of a linear kernel becomes smaller. Here we explore the [Golub microarray dataset](https://github.com/ramhiser/datamicroarray/wiki/Golub-%281999%29) that _"consist of 47 patients with acute lymphoblastic leukemia (ALL) and 25 patients with acute myeloid leukemia (AML). Each of the 72 patients had bone marrow samples obtained at the time of diagnosis. Furthermore, the observations have been assayed with Affymetrix Hgu6800 chips, resulting in 7129 gene expressions (Affymetrix probes)"_.

1\. Load the file `'data/golub1999.csv'` into a dataframe. Use column `class` as `y` and all others as `X`. Split it using a `0.3` ratio.

2\. Fit and perform `GridSearchCV` with a RBF kernel and a linear kernel on their respective parameters.

3\. Compare the performance of the two kernels. What are the advantages of using a linear kernel when the performance is similar to an RBF?


**From now on**, we will explore a "tall" dataset, where there are 200,000 entries and 13 features. This one has been generated for the purpose of this exercise.

4\. Load the file `'data/part7_tall.csv'` into a dataframe. It has been scaled, so you will not need to scale it.
   Subsample 20,000 rows to shorten our training time. Normally if time is not a constraint, then subsample is
   not necessary.

5\. Use `GridSearchCV` to select the best model for linear and RBF kernels. Use `sklearn.svm.LinearSVC` to fit a linear model. This uses a different underlying library
for finding the solution and is much faster. Comment on their relative performance. Be careful not to search the parameter space too exhaustively, or you'll find it takes a long time. Start with no more than 5 values.

<br>

## Part 8: Multiclass SVM

So far, we've focused on two-class classification problems, but what if we have multiple classes?
We might want to classify which section of a newspaper an article belongs in, what digit is
represented by an image, etc. So how can we extend our binary classifiers to deal with such cases?

To train a binary classifier to identify multiple classes often something called one-vs-rest is used, which trains each possible class against all other classes at a time. Another option, implemented by default in SVC is one-vs-one, which trains each class against the other.

1\. How many models need to be trained to predict all classes in a one-vs-rest approach? In a one-vs-one? (Remember, you don't need to train both x vs. y and y vs. x).

**Note**: In scikit-learn the default SVC handles multiclass internally  one-vs-one , but other classification algorithms use one-vs-rest.  For this exercise we will be using [scikit-learns](http://scikit-learn.org/stable/modules/multiclass.html#one-vs-the-rest) one-vs-the-rest classifier.

3\. Load the [digit data set](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits).

<4\. Use [sklearn.multiclass.OneVsOneClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html) and [sklearn.multiclass.OneVsRestClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html) to create a one-vs-one classifier and a one-vs-rest classifier for both LinearSVC and LogisticRegression.

For the one-vs-rest logistic regression, you'll have to use the built-in multi-class support instead of the OneVsRest class. Use the one-vs-rest classifier for both the LinearSVC and the LogisticRegression. Compare the performance of each for accuracy. Feel free to sample the dataset if it is taking too long to run.


## Extra Credit: Bacterial Identification

The data in `data/bio.csv` is a dataset of microbiome data. More specifically samples from two separate locations (stool or tissue) and the counts of different bacteria obtained from RNA sequencing.  `location` is your label in this case.

1. We will need to clean the data slightly.  First drop the `Group` column as we wil not be using it.
2. Pivot the data to look like the following (each row corresponds to a patient's bacteria counts in stool or tissue):

<table border=\1\ class=\dataframe\>
          <thead>
            <tr style=\text-align: right;\>
              <th>Taxon</th>
              <th>Location</th>
              <th>Actinobacteria</th>
              <th>Bacteroidetes</th>
              <th>Firmicutes</th>
              <th>Other</th>
              <th>Proteobacteria</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>0</th>
              <td> 0</td>
              <td> 1590</td>
              <td> 67</td>
              <td>  136</td>
              <td> 195</td>
              <td> 2469</td>
            </tr>
            <tr>
              <th>1</th>
              <td> 1</td>
              <td>    4</td>
              <td>  0</td>
              <td> 4182</td>
              <td>  18</td>
              <td> 1821</td>
            </tr>
            <tr>
              <th>2</th>
              <td> 0</td>
              <td>   25</td>
              <td>  0</td>
              <td> 1174</td>
              <td>  42</td>
              <td>  839</td>
            </tr>
            <tr>
              <th>3</th>
              <td> 1</td>
              <td>    2</td>
              <td>  0</td>
              <td>  703</td>
              <td>   2</td>
              <td>  661</td>
            </tr>
            <tr>
              <th>4</th>
              <td> 0</td>
              <td>  259</td>
              <td> 85</td>
              <td>  408</td>
              <td> 316</td>
              <td> 4414</td>
            </tr>
          </tbody>
        </table>

2. Try to fit a SVM to this data experimenting with different kernels and parameter values.
2. Use GridSearch to find the optimal parameters.
