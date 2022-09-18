"""
Yiduo Feng
Class: CS 677
Date: 04/24/2022
Homework Problem: 2
Description of Problem (just a 1-2 line summary!):
use a logisticRegression and summarize the results.
"""

# the last digit of my BUID is 8, so I choose R = 2

import pandas as pd
from prettytable import PrettyTable
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from Question1 import lin_row, Gau_row, poly_row

file_name = "seeds_dataset.csv"
colnames=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'L']
#get data frame
df = pd.read_csv(file_name, names=colnames, sep="\t")
df = df.loc[df["L"] != 2]

train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :7], df.loc[:, "L"],
                     test_size=0.5, random_state=3)

classifier = LogisticRegression()
classifier.fit(X_train.values, Y_train.values)
y_pred = classifier.predict(X_test.values)
accuracy = accuracy_score(Y_test, y_pred)
def Log_acc():
    print(accuracy)
    print(confusion_matrix(Y_test,y_pred))


TP = 0
FP = 0
TN = 0
FN = 0
true_label = Y_test.values.tolist()
for i in range(len(true_label)):
    cur_prdct = y_pred[i]
    cur_true = true_label[i]
    if cur_prdct == 3 and cur_prdct == cur_true:
        TP = TP + 1
    elif cur_prdct == 3 and cur_prdct != cur_true:
        FP = FP + 1
    elif cur_prdct == 1 and cur_prdct == cur_true:
        TN = TN + 1
    elif cur_prdct == 1 and cur_prdct != cur_true:
        FN = FN + 1
accuracy = (TP + TN)/len(true_label)
TPR = TP/(TP + FN)
TNR = TN / (TN + FP)
result_row = ["Logistic Regression", TP, FP, TN, FN, accuracy, TPR, TNR]

def get_table():
    #create table
    table = PrettyTable(
        ["Model", "TP", "FP", "TN", "FN",
         "accuracy", "TPR", "TNR"])
    #build table
    table.add_row(lin_row())
    table.add_row(Gau_row())
    table.add_row(poly_row())
    table.add_row(result_row)
    #print the table
    print(table)

