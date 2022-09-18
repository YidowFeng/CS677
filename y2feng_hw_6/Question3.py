"""
Yiduo Feng
Class: CS 677
Date: 04/24/2022
Homework Problem: 3
Description of Problem (just a 1-2 line summary!):
use K_means to predict the data
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

train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :7], df.loc[:, "L"],
                     test_size=0.5, random_state=3)
inertia_list = []
for k in range(1, 9):
    kmeans_clf = KMeans(n_clusters=k)
    X_scaled = StandardScaler().fit_transform(X_train.values)
    kmeans_clf.fit(X_scaled)
    y_kmeans = kmeans_clf.predict(X_test.values)
    inertia = kmeans_clf.inertia_
    inertia_list.append(inertia)

fig, ax = plt.subplots(1, figsize=(7,5))
plt.plot(range(1, 9), inertia_list, marker ='o', color='green')
#plt.legend()
plt.xlabel('number of clusters: k')
plt.ylabel('inertia')
plt.tight_layout()
def get_k_plot():
    plt.show()

# 3.2 -------------------------------------------------------

features = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7']
fea_1, fea_2 = random.sample(features, 2)
df = df[[fea_1, fea_2, 'L']]
train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :2], df.loc[:, "L"],
                     test_size=0.5, random_state=3)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X_train)
y_kmeans = kmeans.predict(X_test) + 1

centers = kmeans.cluster_centers_
centers_1 = centers[0]
centers_2 = centers[1]
centers_3 = centers[2]


# 3.3 -------------------------------------------------------
def centroid_label(centers_main, tmp_1, tmp_2):
    tmp_class = []
    for i in range(len(X_test[fea_1].values)):
        cur_point = [X_test[fea_1].values.tolist()[i],
                     X_test[fea_2].values.tolist()[i]]
        cur_y = Y_test.values.tolist()[i]
        # dst_main = np.linalg.norm(cur_point - centers_main)
        # dst_2 = np.linalg.norm(cur_point - tmp_1)
        # dst_3 = np.linalg.norm(cur_point - tmp_2)
        dst_main = math.dist(cur_point, centers_main)
        dst_2 = math.dist(cur_point, tmp_1)
        dst_3 = math.dist(cur_point, tmp_2)
        if dst_main <= dst_2 and dst_main <= dst_3:
            tmp_class.append(cur_y)
    # print(tmp_class)
    label = mode(tmp_class)
    return([centers_main, label])

cen_lab_1 = centroid_label(centers_1, centers_2, centers_3)
cen_lab_2 = centroid_label(centers_2, centers_3, centers_1)
cen_lab_3 = centroid_label(centers_3, centers_2, centers_1)

def get_cen_la():
    print("centroid: ", cen_lab_1[0], "label: ", cen_lab_1[1])
    print("centroid: ", cen_lab_2[0], "label: ", cen_lab_2[1])
    print("centroid: ", cen_lab_3[0], "label: ", cen_lab_3[1])
# 3.4 -------------------------------------------------------
y_new_pred = []
for i in range(len(X_test[fea_1].values)):
    cur_point = [X_test[fea_1].values.tolist()[i],
                 X_test[fea_2].values.tolist()[i]]
    dst_1 = np.linalg.norm(cur_point - centers_1)
    dst_2 = np.linalg.norm(cur_point - centers_2)
    dst_3 = np.linalg.norm(cur_point - centers_3)
    if dst_1 <= dst_2 and dst_1 <= dst_3:
        y_new_pred.append(cen_lab_1[1])
    elif dst_2 <= dst_1 and dst_2 <= dst_3:
        y_new_pred.append(cen_lab_2[1])
    elif dst_3 <= dst_2 and dst_3 <= dst_1:
        y_new_pred.append(cen_lab_3[1])

accuracy = accuracy_score(Y_test, y_new_pred)
def overall_acc():
    print(accuracy)

# 3.5---------------------------------------------------------------
file_name = "seeds_dataset.csv"
colnames=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'L']
#get data frame
df = pd.read_csv(file_name, names=colnames, sep="\t")
df = df.loc[df["L"] != 2]

train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :7], df.loc[:, "L"],
                     test_size=0.5, random_state=3)

y_pred = []
for i in range(len(X_test[fea_1].values)):
    cur_point = [X_test[fea_1].values.tolist()[i],
                 X_test[fea_2].values.tolist()[i]]
    dst_1 = np.linalg.norm(cur_point - centers_1)
    dst_2 = np.linalg.norm(cur_point - centers_2)
    dst_3 = np.linalg.norm(cur_point - centers_3)
    if dst_1 <= dst_2 and dst_1 <= dst_3:
        y_pred.append(cen_lab_1[1])
    elif dst_2 <= dst_1 and dst_2 <= dst_3:
        y_pred.append(cen_lab_2[1])
    elif dst_3 <= dst_2 and dst_3 <= dst_1:
        y_pred.append(cen_lab_3[1])

accuracy = accuracy_score(Y_test, y_pred)
def new_acc():
    print(accuracy)
    print(confusion_matrix(Y_test,y_pred))