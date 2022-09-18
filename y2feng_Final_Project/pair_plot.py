
import os

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from prettytable import PrettyTable
import statistics
from sklearn.model_selection import train_test_split
import seaborn as sns
from load_df import get_df

df = get_df()
df = df[['Source Port', 'Destination Port', 'Bytes', 'Bytes Sent', 'Class_2']]


train, test = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :4], df.loc[:, "Class_2"],
                     test_size=0.5, random_state=3)

X_train_1 = X_train[train["Class_2"] == 1]
X_train_0 = X_train[train["Class_2"] == 0]
def get_plot():
    sns.pairplot(X_train_0)
    #plt.savefig('pair_0.pdf')
    plt.show()
    sns.pairplot(X_train_1)
    #plt.savefig('pair_1.pdf')
    plt.show()

get_plot()