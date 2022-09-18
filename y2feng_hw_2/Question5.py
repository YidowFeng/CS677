# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/22/2022
Homework Problem: 5
Description of Problem (just a 1-2 line summary!):
get the graph for best W, ensemble, and the true labels
"""



import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


from prettytable import PrettyTable

file_FAAAX ='FAAAX.csv'
file_SPY = 'SPY.csv'

'''
part 1
'''
# get frame
def get_frames():
    label_faaax = []
    label_spy = []
    #read the files
    df_faaax = pd.read_csv(file_FAAAX)
    df_spy = pd.read_csv(file_SPY)
    for r in df_faaax['Return'].values:
        if r >= 0:
            label_faaax.append('+')
        else:
            label_faaax.append('-')
    for r in df_spy['Return'].values:
        if r >= 0:
            label_spy.append('+')
        else:
            label_spy.append('-')

    df_faaax['True Label'] = label_faaax
    df_spy['True Label'] = label_spy

    return(df_faaax, df_spy)

# save the variables
tmp = get_frames()
df_faaax = tmp[0]
df_spy = tmp[1]

df_faaax_3year = df_faaax[df_faaax["Year"] < 2019]
df_spy_3year = df_spy[df_spy['Year'] < 2019]
df_faaax_2year = df_faaax[df_faaax["Year"] >= 2019].copy()
df_spy_2year = df_spy[df_spy['Year'] >= 2019].copy()

L_faaax = len(df_faaax_3year['Return'].values)
L_spy = len(df_spy_3year['Return'].values)
L_positive_faaax = len(df_faaax_3year[df_faaax_3year["True Label"] == '+'])
L_positive_spy = len(df_spy_3year[df_spy_3year["True Label"] == '+'])
L_negative_faaax = len(df_faaax_3year[df_faaax_3year["True Label"] == '-'])
L_negative_spy = len(df_spy_3year[df_spy_3year["True Label"] == '-'])


label_faaax_3y = df_faaax_3year["True Label"].values
label_spy_3y = df_spy_3year["True Label"].values


default_up_faaax = L_positive_faaax/L_faaax
default_up_spy = L_positive_spy / L_spy
default_down_faaax = L_negative_faaax/L_faaax
default_down_spy = L_negative_spy / L_spy


#same as Q2
def predict_by_w(W):
    # print("When W = ", W)
    tmp_faaax = label_faaax_3y.tolist()
    while len(tmp_faaax) != len(df_faaax['Return'].values):
        current_seq = ''.join(tmp_faaax[len(tmp_faaax) - W:len(tmp_faaax)])
        up = len((''.join(tmp_faaax)).split(current_seq + '+')) - 1
        down = len((''.join(tmp_faaax)).split(current_seq +'-')) - 1
        if up > down :
            tmp_faaax.append('+')
        elif up < down:
            tmp_faaax.append('-')
        else:
            tmp_faaax.append('+') if default_up_faaax > default_down_faaax\
                else tmp_faaax.append('-')
    predict_label_faaax = tmp_faaax[len(label_faaax_3y):len(tmp_faaax)]
    # df_faaax_2year['Predicting label'] = predict_label_faaax
    # df_faaax_2year.loc[:, 'Predicting Label'] = predict_label_faaax


    return(predict_label_faaax)

W_2_faaax = predict_by_w(2)
W_3_faaax = predict_by_w(3)
W_4_faaax = predict_by_w(4)

#same as Q3
def ensemble():
    label_faaax = []
    label_spy = []

    for i in range(len(W_2_faaax)):
        list_3_faaax = [W_2_faaax[i], W_3_faaax[i], W_4_faaax[i]]
        cur_label_faaax = max(set(list_3_faaax), key=list_3_faaax.count)
        label_faaax.append(cur_label_faaax)
    return(label_faaax)

ensemble_faaax = ensemble()
true = df_faaax_2year['True Label'].values.tolist()
R_true = df_faaax_2year['Return'].values.tolist()
'''
compute the return for plot
'''
def get_return_plot(W, ensemble):
    r_W = []
    r_esbl = []
    value_W = []
    value_esbl = []
    value_true = []
    money_W = 100
    money_esbl = 100
    money_true = 100
    for i in range(len(R_true)):
        if W[i] == '+':
            r_W.append(R_true[i])
        else:
            r_W.append(0.0)
        if ensemble[i] == '+':
            r_esbl.append(R_true[i])
        else:
            r_esbl.append(0.0)

        money_W = money_W * (1 + r_W[i])
        value_W.append(money_W)
        money_esbl = money_esbl * (1 + r_esbl[i])
        value_esbl.append(money_esbl)
        money_true = money_true * (1 + R_true[i])
        value_true.append(money_true)


    return(value_W, value_esbl, value_true)

money_plot = get_return_plot(W_4_faaax, ensemble_faaax)
value_W = money_plot[0]
# print(value_W)
value_esbl = money_plot[1]
value_true = money_plot[2]
# print(value_true)
'''
draw the plot
'''
def get_plot():
    plot_line = pd.DataFrame({'W2': value_W, 'ensemble': value_esbl, 'true':
                              value_true})

    plot_line.plot()

    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.show()



