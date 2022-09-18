"""
Yiduo Feng
Class: CS 677
Date: 03/30/2022
Homework Problem: 3
Description of Problem (just a 1-2 line summary!): Bult the tables and
predict by LogisticRegression
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
train, test = train_test_split(df, test_size=0.34, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :4], df.loc[:, "class"],
                     test_size=0.5, random_state=3)

X_train_1 = X_train[train["class"] == 1]
X_train_0 = X_train[train["class"] == 0]

# sc_X = StandardScaler()
# X_train_sc = sc_X.fit_transform(X_train)
# X_test_sc = sc_X.transform(X_test)

classifier = LogisticRegression()
classifier.fit(X_train.values, Y_train.values)
Y_pred = classifier.predict(X_test.values)
print(accuracy_score(Y_test, Y_pred))

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

def get_table_5():
    #create table
    table = PrettyTable(
        ["TP", "FP", "TN", "FN",
         "accuracy", "TPR", "TNR"])
    #build table

    table.add_row(result_row)
    #print the table
    print(table)

def BUID_5():
    df_ID = pd.DataFrame(data={'f1': [9], 'f2': [3], 'f3': [1], 'f4': [8]})
    BUID = classifier.predict(df_ID.values)
    print("logistic regression: ", BUID)

BUID_5()