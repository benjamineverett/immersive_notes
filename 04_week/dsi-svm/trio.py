import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import src.pair_helper as pair
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import scale
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV
import os

def load_data():
    if not os.path.exists('data/pickled_data.pkl'):
        df = pd.read_csv('data/svmguide1.csv')
        df.to_pickle('data/pickled_data.pkl')
    else:
        df=pd.read_pickle('data/pickled_data.pkl')
    y=df.pop('y').values
    X=df.values
    X= scale(X)
    X_train, X_test, y_train, y_test = train_test_split(X,y)
    # pair.plot_data_basic(X, y)
    return X_train, X_test, y_train, y_test

def loop_plot(C_lst,X,y):
    for elem in C_lst:
        model = SVC(kernel='linear',C=elem)
        model.fit(X,y)
        pair.plot_svm_decision(model,X,y,np.ones(y_train.shape)*10, 'C = {}'.format(elem))
    plt.legend()
    plt.show()

def k_plot(X,y,k_lst):
    for k in k_lst:
        model = SVC(kernel=k)
        model.fit(X_train,y_train)
        predict = model.predict(X_test)
        print(k, ': ', model.score(X_test,y_test))
        pair.decision_boundary(model, X_train, y_train,k)

def grid_C(X,y,k):
    model = SVC(kernel=k)
    model.fit(X_train,y_train)
    param_space = {'C':np.array([0.01, 0.1, 1.0, 10.0, 100.0])}
    grid_search = GridSearchCV(model,param_space,scoring='accuracy',cv=10)
    grid_search.fit(X_train,y_train)
    print('grid scores:',grid_search.grid_scores_)
    print('\nbest parameter:',grid_search.best_params_)
    print('\nbest score:',grid_search.best_score_)

def grid_degree(X,y, k):
    model = SVC(kernel=k[0])
    model.fit(X_train,y_train)
    if k[1]=='gamma':
        param_space = {'gamma':np.logspace(-3,3,15)}
    elif k[1]=='degree':
        param_space = {'degree':np.array(range(1,10))}
    elif k[1]==None:
        return None
    grid_search = GridSearchCV(model,param_space,scoring='accuracy',cv=10)
    grid_search.fit(X_train,y_train)
    print('grid scores:',grid_search.grid_scores_)
    print('\nbest parameter:',grid_search.best_params_)
    print('\nbest score:',grid_search.best_score_)

def generalized(X,y,k,**kargs):
    model = SVC(kernel=k)
    model.fit(X ,y)
    pass
def linear(X,y):
    pass


if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_data()
    model = SVC(kernel='poly')
    model.fit(X_train,y_train)
    predict = model.predict(X_test)
    # print('rbf', ': ', model.score(X_test,y_test))
    # plt.show()
    # print(k, ': ', cross_val_score(model, X_train, y_train, cv=5))
    # pair.decision_boundary(model, X_train, y_train,'name')
    lst = [('linear',None), ('rbf','gamma'), ('poly', 'degree')]
    for k in lst:
        grid_C(X_train,y_train,k[0])
        print('\n\n\n\n')
        grid_degree(X_train,y_train, k)
