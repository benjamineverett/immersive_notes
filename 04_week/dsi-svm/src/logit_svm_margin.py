from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Part 1 question 1
def plot_data_basic(X, y):
    """Plots a scatter plot for data_scientist.csv using

    Parameters
    ----------
    X : the dataset from data_scientist.csv with 'gym_hours' as col 0 and 'email_hours' as col 1
    y : the label `data_scientist` in data_scientist.csv

    Returns
    -------
    None
    """
    pass


# Part 1 questions 3 and 5
def plot_logit_decision(logreg_clf, X, y, label_sizes=None):
    """Plots the Logistic Regression decision boundary over a scatter plot of data_scientist.csv

    Parameters
    ----------
    logreg_clf : a LogisticRegression model as returned by LogisticRegression().fit()
    X : the dataset from data_scientist.csv with 'gym_hours' as col 0 and 'email_hours' as col 1
    y : the label in data_scientist.csv (1 for red, 0 for blue)
    label_sizes : (for question 1.5) an array corresponding to shape of y, indicating for each point its size on plot

    Returns
    -------
    None
    """
    pass


# Part 1 question 4
def calc_logreg_margin(logreg_clf, X):
    """Computes the margin for each observation in X

    Parameters
    ----------
    logreg_clf : a LogisticRegression model as returned by LogisticRegression().fit()
    X : the dataset from data_scientist.csv with 'gym_hours' as col 0 and 'email_hours' as col 1

    Returns
    -------
    array : the margin computed for each row of X.
    """
    pass


# Part 2 question 2 and question 4
def plot_svm_decision(svc_clf, X, y, label_sizes=None):
    """Plots the Support Vector Classifier decision boundary over a scatter plot of data_scientist.csv

    Parameters
    ----------
    svc_clf : a SVC model as returned by SVC().fit()
    X : the dataset from data_scientist.csv with 'gym_hours' as col 0 and 'email_hours' as col 1
    y : the label in data_scientist.csv (1 for red, 0 for blue)
    label_sizes : (for question 2.4) an array corresponding to shape of y, indicating for each point its size on plot

    Returns
    -------
    None
    """
    # get the separating hyperplane
    w = svc_clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(5, 35)
    yy = a * xx - (svc_clf.intercept_[0]) / w[1]

    # plot the parallels to the separating hyperplane that pass through the
    # support vectors
    margin = 1 / np.sqrt(np.sum(svc_clf.coef_ ** 2))
    yy_down = yy + a * margin
    yy_up = yy - a * margin

    # plot the line, the points, and the nearest vectors to the plane
    colors = ['red' if x else 'blue' for x in y]
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111)

    # if label_sizes are provided, use that as an argument of ax.scatter
    if (label_sizes is not None) :
        ax.scatter(X[:,0], X[:,1], color=colors, s=label_sizes, alpha=0.5)
    else:
        ax.scatter(X[:,0], X[:,1], color=colors, alpha=0.5)

    ax.plot(xx, yy, 'k-')
    ax.plot(xx, yy_down, 'k--')
    ax.plot(xx, yy_up, 'k--')
    ax.set_title('SVM Decision Boundary')
    ax.set_xlabel('Gym Hours')
    ax.set_ylabel('Email Hours')
    ax.set_aspect('equal')
    plt.show()


# Part 2 question 3
def calc_svm_margin(svc_clf, X):
    """Computes the margin for each observation in X

    Parameters
    ----------
    svc_clf : a SVC model as returned by SVC().fit()
    X : the dataset from data_scientist.csv with 'gym_hours' as col 0 and 'email_hours' as col 1

    Returns
    -------
    array : the margin computed for each row of X.
    """


if __name__ == '__main__':
    # First look at the data
    df = pd.read_csv('data/data_scientist.csv')
    X = df[['gym_hours', 'email_hours']].values
    y = df['data_scientist'].values
    plot_data_basic(X,y)

    # Fit and visualize Logistic Regression
    clf = LogisticRegression().fit(X, y)
    plot_logit_decision(clf, X, y)

    # Fit and visualize SVM
    svc_clf = SVC(kernel='linear').fit(X, y)
    plot_svm_decision(svc_clf, X, y)

    # Calculate margins
    logit_margin = calc_logreg_margin(clf, X)
    svm_margin = calc_svm_margin(svc_clf, X)
    print 'Logit sum of margin:', np.sum(logit_margin)
    print 'SVC sum of margin:', np.sum(svm_margin)
