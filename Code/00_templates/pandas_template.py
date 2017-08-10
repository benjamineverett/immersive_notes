import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def get_data_frame(filename, random_sample=False, percent_of_df = .1):
    '''INPUT:
    filename = name of file
    random_sample = return a random sample of data
    percent_of_df = 0 < input < 1, returns percent of data frame specified by input
    OUTPUT:
    data frame
    '''

    if random_sample:
        df = pd.read_csv(filename)
        df.sample(frac = percent_of_df)
    else:
        df = pd.read_csv(filename)
    return df

def explore_data(dataframe):
    '''
    INPUT:
    filename = call get_data_frame function
    RETURN:
    print description of data and list of columns with types of data in columns
    '''
    df = dataframe
    print(df.describe())
    print(df.dtypes)

def get_all_columns_except(dataframe):
    df.ix[:, df.columns != 'b']
