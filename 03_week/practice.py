import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

credit_card = sm.datasets.ccard.load_pandas().data
y = credit_card['AVGEXP']
x = credit_card.drop('AVGEXP', axis=1)
x['INCOME^2'] = x['INCOME']**2
x = sm.add_constant(x)
# print(x.head())


def get_model(x,y, prt=False):
    model = sm.OLS(y,x).fit()
    summary = model.summary()
    if prt:
        print(summary)
    return model


def scatter_matrix(df,name=False,show=False):
    scatter_matrix(df, diagonal='kde')
    if name:
        plt.savefig('scatter.png')
    if show:
        plt.show()

def get_student_resid():
    model = get_model()
    student_y = model.outlier_test()['student_resid']
    student_x = x
    plot.scatterplot(student_x, student_y)
    plt.show()

if __name__ == '__main__':
    get_student_resid()
