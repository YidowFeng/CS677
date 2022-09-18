"""
Yiduo Feng
Class: CS 677
Date: 03/30/2022
Homework Problem: 4
Description of Problem (just a 1-2 line summary!): Bult the tables and
remove the feature and predict by k-NN
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
def three_featrue(feature):
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


    df = df.drop(columns=feature, axis=1)

    train, test = train_test_split(df, test_size=0.5, random_state=3)
    X_train, X_test, Y_train, Y_test = \
        train_test_split(df.iloc[:, :3], df.loc[:, "class"],
                         test_size=0.5, random_state=3)

    X_train_1 = X_train[train["class"] == 1]
    X_train_0 = X_train[train["class"] == 0]

    sc_X = StandardScaler()
    X_train_sc = sc_X.fit_transform(X_train)
    X_test_sc = sc_X.transform(X_test)

    classifier = KNeighborsClassifier(n_neighbors=3, p=2, metric='euclidean')
    classifier.fit(X_train_sc, Y_train)
    Y_pred = classifier.predict(X_test_sc)

    print(accuracy_score(Y_test, Y_pred))

def print_result_4():
    print("When missing f1")
    three_featrue('f1')
    print("When missing f2")
    three_featrue('f2')
    print("When missing f3")
    three_featrue('f3')
    print("When missing f4")
    three_featrue('f4')