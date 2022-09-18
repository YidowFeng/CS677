"""
Yiduo Feng
Class: CS 677
Date: 04/27/2022

Description of Problem (just a 1-2 line summary!):
linear regression
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from prettytable import PrettyTable
import statistics

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from load_df import get_df

df = get_df()
df = df[['Source Port', 'Destination Port', 'Class_2']]

df_0 = df[df["Class_2"] == 0]
df_1 = df[df["Class_2"] == 1]
'''
get SSE for allow patients
'''
train_0, test_0 = train_test_split(df_0, test_size=0.5, random_state=3)
X_train_0, X_test_0, Y_train_0, Y_test_0 = \
    train_test_split(df_0.iloc[:, :1], df_0.loc[:, "Destination Port"],
                     test_size=0.5, random_state=3)



def SSE(Y_test, y_pred):
    #residuals
    r_0 = []
    # loss function (SSE sum of the squared of residuals)
    L_0 = 0
    for i in range(len(y_pred)):
        r_i = Y_test.values.tolist()[i] - y_pred[i]
        r_0.append(r_i)
        L_0 = L_0 + r_i**2

    print("SSE = ", L_0)



#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def get_graph_0():
    print("-----------------allow------------------------")
    # 1-3degree linear
    new_X_test_0 = sorted(X_test_0.values)
    for degree in [1, 2, 3]:
        weight = np.polyfit(X_train_0['Source Port'].values, Y_train_0, degree)
        print("weight = ", weight)
        model = np.poly1d(weight)
        print(model)
        y_pred_0 = model(new_X_test_0)
        SSE(Y_test_0, y_pred_0)
        rmse = np.square(mean_squared_error(Y_test_0, y_pred_0))
        print("rmes = ", rmse)
        plt.plot(new_X_test_0, Y_test_0.values.tolist(), "b.")
        plt.plot(new_X_test_0, y_pred_0, "k--")
        plt.xlabel("Predictor variable")
        plt.ylabel("Response Variable")
        titile = "Scatterplot with " + str(degree) + "deg Function"
        plt.title(titile)
        plt.show()


'''
get SSE for deny patients
'''
train_1, test_1 = train_test_split(df_1, test_size=0.5, random_state=3)
X_train_1, X_test_1, Y_train_1, Y_test_1 = \
    train_test_split(df_1.iloc[:, :1], df_1.loc[:, "Destination Port"],
                     test_size=0.5, random_state=3)

def get_graph_1():
    print("-----------------deny------------------------")
    #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # 1-3degree linear
    new_X_test_1 = sorted(X_test_1.values)
    for degree in [1, 2, 3]:
        weight = np.polyfit(X_train_1['Source Port'].values, Y_train_1, degree)
        print("weight = ", weight)
        model = np.poly1d(weight)
        print(model)
        y_pred_1 = model(new_X_test_1)
        SSE(Y_test_1, y_pred_1)
        rmse = np.square(mean_squared_error(Y_test_1, y_pred_1))
        print("rmes = ", rmse)
        plt.plot(new_X_test_1, Y_test_1.values.tolist(), "b.")
        plt.plot(new_X_test_1, y_pred_1, "k--")
        plt.xlabel("Predictor variable")
        plt.ylabel("Response Variable")
        titile = "Scatterplot with " + str(degree) + "deg Function"
        plt.title(titile)
        plt.show()


get_graph_0()
get_graph_1()



