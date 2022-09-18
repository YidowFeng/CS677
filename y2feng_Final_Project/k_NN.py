"""
Yiduo Feng
Class: CS 677
Date: 04/27/2022

Description of Problem (just a 1-2 line summary!):
 construct the visual representations of
k-nn

"""
import os

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from prettytable import PrettyTable
import statistics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import seaborn as sns
from load_df import get_df


# def get_frames():
df = get_df()
df = df.drop(columns=["Action", "Class_1"])
train, test = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :11], df.loc[:, "Class_2"],
                     test_size=0.5, random_state=3)

X_train_1 = X_train[train["Class_2"] == 1]
X_train_0 = X_train[train["Class_2"] == 0]

sc_X = StandardScaler()
X_train_sc = sc_X.fit_transform(X_train)
X_test_sc = sc_X.transform(X_test)

X_train_sc = pd.DataFrame(X_train_sc)
X_test_sc = pd.DataFrame(X_test_sc)

accuracy = []
test_k = [3, 5, 7, 9, 11, 13, 15]
#get accuracy
for i in test_k:
  classifier = KNeighborsClassifier(n_neighbors=i, p=2, metric='euclidean')
  classifier.fit(X_train_sc.values, Y_train.values)
  Y_pred = classifier.predict(X_test_sc.values)
  accuracy.append(accuracy_score(Y_test, Y_pred))

def get_accuracy_knn():
    print(accuracy)

get_accuracy_knn()

#plot the graph
plt.plot(test_k, accuracy, "r-")
plt.xlabel("k")
plt.ylabel("Accuracy of Predictions")
plt.title("Plot of Accuracy vs k value for kNN")

def get_plot_knn():
    plt.show()

get_plot_knn()
#get the best k and predict
best_k = test_k[accuracy.index(max(accuracy))]
classifier = KNeighborsClassifier(n_neighbors=best_k, p=2, metric='euclidean')
classifier.fit(X_train_sc, Y_train)
Y_pred = classifier.predict(X_test_sc)

TP = 0
FP = 0
TN = 0
FN = 0
true_label = test['Class_2'].values.tolist()
for i in range(len(true_label)):
    cur_prdct = Y_pred[i]
    cur_true = true_label[i]
    if cur_prdct == 0 and cur_prdct == cur_true:
        TP = TP + 1
    elif cur_prdct == 0 and cur_prdct != cur_true:
        FP = FP + 1
    elif cur_prdct == 1 and cur_prdct == cur_true:
        TN = TN + 1
    elif cur_prdct == 1 and cur_prdct != cur_true:
        FN = FN + 1
accuracy = (TP + TN)/len(true_label)
TPR = TP/(TP + FN)
TNR = TN / (TN + FP)
result_row = [TP, FP, TN, FN, accuracy, TPR, TNR]

def get_table_knn():
    #create table
    table = PrettyTable(
        ["TP", "FP", "TN", "FN",
         "accuracy", "TPR", "TNR"])
    #build table

    table.add_row(result_row)
    #print the table
    print(table)

get_table_knn()

