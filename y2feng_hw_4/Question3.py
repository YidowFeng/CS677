"""
Yiduo Feng
Class: CS 677
Date: 04/06/2022
Homework Problem: 3
Description of Problem (just a 1-2 line summary!):
get table and give summary

"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from prettytable import PrettyTable
import statistics
from prettytable import PrettyTable
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
        L_0 = L_0 + np.square(r_i)
    #print(L_0.tolist()[0])
    return(L_0[0])


SSE_0 = []
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 1-3degree linear
X_test_0 = sorted(X_test_0.values)
for degree in [1, 2, 3]:
    weight = np.polyfit(X_train_0['serum_sodium'].values, Y_train_0, degree)
    model = np.poly1d(weight)
    y_pred_0 = model(X_test_0)
    sse = SSE(Y_test_0, y_pred_0)
    rmse = np.square(mean_squared_error(Y_test_0, y_pred_0))
    SSE_0.append(sse)

# y = alogx + b
weight = np.polyfit(X_train_0['serum_sodium'].values, Y_train_0, 1)
model = np.poly1d(weight)
y_pred_0 = model(np.log(X_test_0))
sse = SSE(Y_test_0, y_pred_0)
rmse = np.square(mean_squared_error(Y_test_0, y_pred_0))
SSE_0.append(sse)

#logy = alogx + b
weight = np.polyfit(X_train_0['serum_sodium'].values, Y_train_0, 1)
model = np.poly1d(weight)
y_pred_0 = np.exp(model(np.log(X_test_0)))
sse = SSE(Y_test_0, y_pred_0)
rmse = np.square(mean_squared_error(Y_test_0, y_pred_0))
SSE_0.append(sse)
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''
get SSE for deceased patients
'''
train_1, test_1 = train_test_split(df_1, test_size=0.5, random_state=3)
X_train_1, X_test_1, Y_train_1, Y_test_1 = \
    train_test_split(df_1.iloc[:, :1], df_1.loc[:, "serum_creatinine"],
                     test_size=0.5, random_state=3)

SSE_1 = []
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 1-3degree linear
X_test_1 = sorted(X_test_1.values)
for degree in [1, 2, 3]:
    weight = np.polyfit(X_train_1['serum_sodium'].values, Y_train_1, degree)
    model = np.poly1d(weight)
    y_pred_1 = model(X_test_1)
    sse = SSE(Y_test_1, y_pred_1)
    rmse = np.square(mean_squared_error(Y_test_1, y_pred_1))
    SSE_1.append(sse)

# y = alogx + b
weight = np.polyfit(X_train_1['serum_sodium'].values, Y_train_1, 1)
model = np.poly1d(weight)
y_pred_1 = model(np.log(X_test_1))
sse = SSE(Y_test_1, y_pred_1)
rmse = np.square(mean_squared_error(Y_test_1, y_pred_1))
SSE_1.append(sse)

#logy = alogx + b
weight = np.polyfit(X_train_1['serum_sodium'].values, Y_train_1, 1)
model = np.poly1d(weight)
y_pred_1 = np.exp(model(np.log(X_test_1)))
sse = SSE(Y_test_1, y_pred_1)
rmse = np.square(mean_squared_error(Y_test_1, y_pred_1))
SSE_1.append(sse)
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


myTable = PrettyTable()
myTable.add_column('Model', ["y = ax + b", "y = ax2 + bx + c",
"y = ax3 + bx2 + cx + d", "y = a log x + b", "log y = a log x + b"])
myTable.add_column('SSE (death event=0)', SSE_0)
myTable.add_column('SSE (death event=1)', SSE_1)

def get_table():
    print(myTable)




