import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Main(object):
    def __init__(self):
        self.filename = 'data/part1_unscaled.csv'
        # self.df = None
        self._get_dataframe()


    def _get_dataframe(self):
        return pd.read_csv(self.filename)

    def get_info(self):
        print(self.df.head())


if __name__ == '__main__':
    df = Main()
