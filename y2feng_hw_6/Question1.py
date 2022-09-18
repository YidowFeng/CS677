"""
Yiduo Feng
Class: CS 677
Date: 04/24/2022
Homework Problem: 1
Description of Problem (just a 1-2 line summary!):
get dataframe and predict by SVM
"""

# the last digit of my BUID is 8, so I choose R = 2

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.svm import LinearSVC, SVC  # support vector classification
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix

file_name = "seeds_dataset.csv"
colnames=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'L']
#get data frame
df = pd.read_csv(file_name, names=colnames, sep="\t")
df = df.loc[df["L"] != 2]

train_0, test_0 = train_test_split(df, test_size=0.5, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :7], df.loc[:, "L"],
                     test_size=0.5, random_state=3)

'''
linear kernel SVM
'''
linear_svm = LinearSVC(C=10, loss="hinge")
X_scaled = StandardScaler().fit_transform(X_train)
X_scaled_test = StandardScaler().fit_transform(X_test)
linear_svm.fit(X_scaled, Y_train.values)
y_pred_lin = linear_svm.predict(X_scaled_test)

accuracy = accuracy_score(Y_test, y_pred_lin)
def lin_acc():
    print(accuracy)
    print(confusion_matrix(Y_test,y_pred_lin))

def lin_row():
    result = get_row("linear SVM", Y_test, y_pred_lin)
    return(result)
'''
Gaussian kernel SVM
'''
clf = SVC(kernel='rbf')
clf.fit(X_scaled, Y_train.values)
y_pred_gau = clf.predict(X_scaled_test)

accuracy = accuracy_score(Y_test, y_pred_gau)
def Gau_acc():
    print(accuracy)
    print(confusion_matrix(Y_test,y_pred_gau))

def Gau_row():
    result = get_row("Gaussian SVM", Y_test, y_pred_gau)
    return(result)
'''
polynomial kernel SVM of degree 3.
'''
poly_svm = Pipeline([('poly_feat',PolynomialFeatures(degree=3)),
                     ('scaler',StandardScaler()),
                     ('svm',LinearSVC(C=1,loss='hinge'))])
poly_svm.fit(X_scaled, Y_train.values)
y_pred_poly = poly_svm.predict(X_scaled_test)
accuracy = accuracy_score(Y_test, y_pred_poly)
def poly_acc():
    print(accuracy)
    print(confusion_matrix(Y_test,y_pred_poly))
def poly_row():
    result = get_row("polynomial SVM", Y_test, y_pred_poly)
    return(result)



def get_row(clf, cur_Y_test, cur_pred):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    true_label = cur_Y_test.values.tolist()
    for i in range(len(true_label)):
        cur_prdct = cur_pred[i]
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
    result_row = [clf, TP, FP, TN, FN, accuracy, TPR, TNR]
    return(result_row)