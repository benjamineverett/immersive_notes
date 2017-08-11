import numpy as np
import matplotlib.pyplot as plt


def plot_data_basic(X, y):
    """Plots a scatter plot

    Parameters
    ----------
    X : a dataset with two columns
    y : a label column in {0,1}

    Returns
    -------
    None
    """
    colors = ['red' if x else 'blue' for x in y]
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111)
    ax.scatter(X[:,0], X[:,1], color=colors, alpha=0.5)
    plt.xlabel('X1')
    plt.ylabel('X2')


def plot_svm_decision(model, X, y, label_sizes, name):
    """Plots the Support Vector Classifier decision boundary over a scatter plot of data_scientist.csv

    Parameters
    ----------
    model : a SVC model as returned by SVC().fit()
    X : a dataset with two columns
    y : a label column in {0,1}
    label_sizes : an array corresponding to shape of y, indicating for each point its size on plot
    name : a name for the figure (for enhanced readibility)

    Returns
    -------
    None
    """
    # get the separating hyperplane
    w = model.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(min(X[:,0]), max(X[:,0]))
    yy = a * xx - (model.intercept_[0]) / w[1]

    # plot the parallels to the separating hyperplane that pass through the
    # support vectors
    margin = 1 / np.sqrt(np.sum(model.coef_ ** 2))
    yy_down = yy + a * margin
    yy_up = yy - a * margin

    # plot the line, the points, and the nearest vectors to the plane
    colors = ['red' if x else 'blue' for x in y]
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111)

    ax.scatter(X[:,0], X[:,1], color=colors, s=label_sizes, alpha=0.5)
    ax.plot(xx, yy, 'k-')
    ax.plot(xx, yy_down, 'k--')
    ax.plot(xx, yy_up, 'k--')

    # applying a limit on the plot to focus on the point clouds
    plt.xlim(min(X[:,0]), max(X[:,0]))
    plt.ylim(min(X[:,1]), max(X[:,1]))

    plt.title('SVM Decision Boundary %s' % name)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


# NOTE: function used in part 3 for non-linear separation
def decision_boundary(clf, X, Y, name, h=.02):
    """Plots non-linear decision boundaries by plotting decision for every pixel on the plot

    Parameters
    ----------
    clf : a classification model
    X : a dataset with two columns
    y : a label column in {0,1}
    label_sizes : an array corresponding to shape of y, indicating for each point its size on plot
    name : a name for the figure (for enhanced readibility)
    h : the step for pixel plotting within the figure (homogeneous to scale of attributes in X)

    Returns
    -------
    None
    """
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1, figsize=(10, 7))
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title('%s' % name)
    plt.show()
