"""
Yiduo Feng
Class: CS 677
Date: 04/24/2022
Homework Problem: 3.2
Description of Problem (just a 1-2 line summary!):
In order to get the graph, this is a part of Question3.py
"""

# the last digit of my BUID is 8, so I choose R = 2
import math
import random
from statistics import mode

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from prettytable import PrettyTable
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, \
    pairwise_distances_argmin
from sklearn.preprocessing import StandardScaler

from Question1 import lin_row, Gau_row, poly_row

file_name = "seeds_dataset.csv"
colnames=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'L']
#get data frame
df = pd.read_csv(file_name, names=colnames, sep="\t")

features = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7']
fea_1, fea_2 = random.sample(features, 2)
def two_features():
    print(fea_1, fea_2)
df = df[[fea_1, fea_2, 'L']]
train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :2], df.loc[:, "L"],
                     test_size=0.5, random_state=3)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X_train)
y_kmeans = kmeans.predict(X_test) + 1

plot =plt.scatter(X_test[fea_1].values, X_test[fea_2].values,
            c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
centers_1 = centers[0]
centers_2 = centers[1]
centers_3 = centers[2]
print(centers)
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.8)
def datapoint():
    plt.show()

