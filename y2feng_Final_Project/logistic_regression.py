"""
Yiduo Feng
Class: CS 677
Date: 04/27/2022

Description of Problem (just a 1-2 line summary!):
logistic regression

"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from prettytable import PrettyTable
import statistics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from load_df import get_df

df = get_df()
df = df[['Source Port', 'Destination Port', 'Bytes', 'Bytes Sent', 'Class_2']]

train, test = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :4], df.loc[:, "Class_2"],
                     test_size=0.5, random_state=3)

X_train_1 = X_train[train["Class_2"] == 1]
X_train_0 = X_train[train["Class_2"] == 0]


classifier = LogisticRegression()
classifier.fit(X_train.values, Y_train.values)
Y_pred = classifier.predict(X_test.values)

accuracy = accuracy_score(Y_test, Y_pred)
def get_accuracy_logistic():
    print(accuracy)

get_accuracy_logistic()

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

def get_table_logistic():
    #create table
    table = PrettyTable(
        ["TP", "FP", "TN", "FN",
         "accuracy", "TPR", "TNR"])
    #build table

    table.add_row(result_row)
    #print the table
    print(table)

get_table_logistic()

