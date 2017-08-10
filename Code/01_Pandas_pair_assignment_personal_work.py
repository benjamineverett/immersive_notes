import pandas as  pd

df = pd.read_csv('data/hospital-costs.csv')


if __name__ == '__main__':

    df.describe()
