"""
Yiduo Feng
Class: CS 677
Date: 04/06/2022
Homework Problem: 2
Description of Problem (just a 1-2 line summary!):
compare a number of different models using linear systems
look for the best model (from the list below) that
best explains the relationship for surviving and deceased patients.
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

file = "heart_failure_clinical_records_dataset.csv"
#read file
df = pd.read_csv(file)
df = pd.DataFrame(df, columns=["serum_sodium", "serum_creatinine",
                               "DEATH_EVENT"])
#get surviving and deceased

df_0 = df[df["DEATH_EVENT"] == 0]
df_1 = df[df["DEATH_EVENT"] == 1]
'''
get SSE for surviving patients
'''
train_0, test_0 = train_test_split(df_0, test_size=0.5, random_state=3)
X_train_0, X_test_0, Y_train_0, Y_test_0 = \
    train_test_split(df_0.iloc[:, :1], df_0.loc[:, "serum_creatinine"],
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
    print("-----------------surviving------------------------")
    # 1-3degree linear
    new_X_test_0 = sorted(X_test_0.values)
    for degree in [1, 2, 3]:
        weight = np.polyfit(X_train_0['serum_sodium'].values, Y_train_0, degree)
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

    # y = alogx + b
    weight = np.polyfit(X_train_0['serum_sodium'].values, Y_train_0, 1)
    print("weight = ", weight)
    model = np.poly1d(weight)
    print(model)
    y_pred_0 = model(np.log(new_X_test_0))
    SSE(Y_test_0, y_pred_0)
    rmse = np.square(mean_squared_error(Y_test_0, y_pred_0))
    print("rmes = ", rmse)
    plt.plot(new_X_test_0, Y_test_0.values.tolist(), "b.")
    plt.plot(new_X_test_0, y_pred_0, "k--")
    plt.xlabel("Predictor variable")
    plt.ylabel("Response Variable")
    plt.title("GLM - generalized linear model")
    plt.show()

    #logy = alogx + b
    weight = np.polyfit(X_train_0['serum_sodium'].values, Y_train_0, 1)
    print("weight = ", weight)
    model = np.poly1d(weight)
    print(model)
    y_pred_0 = np.exp(model(np.log(new_X_test_0)))
    SSE(Y_test_0, y_pred_0)
    rmse = np.square(mean_squared_error(Y_test_0, y_pred_0))
    print("rmes = ", rmse)
    plt.plot(new_X_test_0, Y_test_0.values.tolist(), "b.")
    plt.plot(new_X_test_0, y_pred_0, "k--")
    plt.xlabel("Predictor variable")
    plt.ylabel("Response Variable")
    plt.title("GLM - generalized linear model(log y)")
    plt.show()
    #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''












'''
get SSE for deceased patients
'''
train_1, test_1 = train_test_split(df_1, test_size=0.5, random_state=3)
X_train_1, X_test_1, Y_train_1, Y_test_1 = \
    train_test_split(df_1.iloc[:, :1], df_1.loc[:, "serum_creatinine"],
                     test_size=0.5, random_state=3)

def get_graph_1():
    print("-----------------deceased------------------------")
    #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # 1-3degree linear
    new_X_test_1 = sorted(X_test_1.values)
    for degree in [1, 2, 3]:
        weight = np.polyfit(X_train_1['serum_sodium'].values, Y_train_1, degree)
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

    # y = alogx + b
    weight = np.polyfit(X_train_1['serum_sodium'].values, Y_train_1, 1)
    print("weight = ", weight)
    model = np.poly1d(weight)
    print(model)
    y_pred_1 = model(np.log(new_X_test_1))
    SSE(Y_test_1, y_pred_1)
    rmse = np.square(mean_squared_error(Y_test_1, y_pred_1))
    print("rmes = ", rmse)
    plt.plot(new_X_test_1, Y_test_1.values.tolist(), "b.")
    plt.plot(new_X_test_1, y_pred_1, "k--")
    plt.xlabel("Predictor variable")
    plt.ylabel("Response Variable")
    plt.title("GLM - generalized linear model")
    plt.show()

    #logy = alogx + b
    weight = np.polyfit(X_train_1['serum_sodium'].values, Y_train_1, 1)
    print("weight = ", weight)
    model = np.poly1d(weight)
    print(model)
    y_pred_1 = np.exp(model(np.log(new_X_test_1)))
    SSE(Y_test_1, y_pred_1)
    rmse = np.square(mean_squared_error(Y_test_1, y_pred_1))
    print("rmes = ", rmse)
    plt.plot(new_X_test_1, Y_test_1.values.tolist(), "b.")
    plt.plot(new_X_test_1, y_pred_1, "k--")
    plt.xlabel("Predictor variable")
    plt.ylabel("Response Variable")
    plt.title("GLM - generalized linear model(log y)")
    plt.show()
    #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



get_graph_0()
get_graph_1()



