"""
Yiduo Feng
Class: CS 677
Date: 03/30/2022
Homework Problem: 2
Description of Problem (just a 1-2 line summary!):
predict by simple classifier
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from prettytable import PrettyTable
import statistics
from sklearn.model_selection import train_test_split
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
def get_plot():
    sns.pairplot(X_train_0)
    plt.savefig("good_bills.pdf", format="pdf", bbox_inches="tight")
    plt.show()
    sns.pairplot(X_train_1)
    plt.savefig("fake_bills.pdf", format="pdf", bbox_inches="tight")
    plt.show()

def detect(f1, f2, f3, f4):
    if f1 < -2.5 or f2 < -8 or f3 > 10:
        x = 1 #x = "fake"
    else:
        x = 0 #x = "good"

    return(x)


predict_test = []
for i in range(len(X_test)):
    cur_x = detect(X_test['f1'].values.tolist()[i],
        X_test['f2'].values.tolist()[i], X_test['f3'].values.tolist()[i],
        X_test['f4'].values.tolist()[i])

    predict_test.append(cur_x)

X_test['class'] = predict_test

def get_test_2():
    print(X_test)

TP = 0
FP = 0
TN = 0
FN = 0
true_label = test['class'].values.tolist()
for i in range(len(true_label)):
    cur_prdct = predict_test[i]
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

def get_table_2():
    #create table
    table = PrettyTable(
        ["TP", "FP", "TN", "FN",
         "accuracy", "TPR", "TNR"])
    #build table

    table.add_row(result_row)
    #print the table
    print(table)
