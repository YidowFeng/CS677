"""
Yiduo Feng
Class: CS 677
Date: 03/30/2022
Homework Problem: 3
Description of Problem (just a 1-2 line summary!): Bult the tables and
predict by K-NN
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


# def get_frames():

#read files
file = "data_banknote_authentication.txt"
df = pd.read_csv(file, sep=",", header=None,names=["f1", "f2", "f3", "f4",
                                                   "class"])
#get the color column
color = []
for r in df['class'].values:
    if r == 0:
        color.append('green')
    else:
        color.append('red')
df['color'] = color

df_green = df[df['class'] == 0]
df_red = df[df['class'] == 1]
train, test = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :4], df.loc[:, "class"],
                     test_size=0.5, random_state=3)

X_train_1 = X_train[train["class"] == 1]
X_train_0 = X_train[train["class"] == 0]

sc_X = StandardScaler()
X_train_sc = sc_X.fit_transform(X_train)
X_test_sc = sc_X.transform(X_test)

X_train_sc = pd.DataFrame(X_train_sc)
X_test_sc = pd.DataFrame(X_test_sc)

accuracy = []
#get accuracy
for i in [3, 5, 7, 9, 11]:
  classifier = KNeighborsClassifier(n_neighbors=i, p=2, metric='euclidean')
  classifier.fit(X_train_sc.values, Y_train.values)
  Y_pred = classifier.predict(X_test_sc.values)
  accuracy.append(accuracy_score(Y_test, Y_pred))

def get_accuracy_3():
    print(accuracy)

get_accuracy_3()
#plot the graph
plt.plot([3, 5, 7, 9, 11], accuracy, "r-")
plt.xlabel("k")
plt.ylabel("Accuracy of Predictions")
plt.title("Plot of Accuracy vs k value for kNN")
def get_plot_3():
    plt.show()

get_plot_3()
#get the best k and predict
best_k = accuracy.index(max(accuracy))
classifier = KNeighborsClassifier(n_neighbors=3, p=2, metric='euclidean')
classifier.fit(X_train_sc, Y_train)
Y_pred = classifier.predict(X_test_sc)

TP = 0
FP = 0
TN = 0
FN = 0
true_label = test['class'].values.tolist()
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

def get_table_3():
    #create table
    table = PrettyTable(
        ["TP", "FP", "TN", "FN",
         "accuracy", "TPR", "TNR"])
    #build table

    table.add_row(result_row)
    #print the table
    print(table)

def simple_detect(f1, f2, f3, f4):
    if f1 < -2.5 or f2 < -8 or f3 > 10:
        x = 1 #x = "fake"
    else:
        x = 0 #x = "good"

    return(x)

def BUID_3():
    print("simple classifier： ", simple_detect(9, 3, 1, 8))

    print("best k: ", classifier.predict(pd.DataFrame(data={'f1': [9],
                                    'f2': [3], 'f3': [1], 'f4': [8]}).values))

BUID_3()