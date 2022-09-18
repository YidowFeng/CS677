# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/22/2022
Homework Problem: 3
Description of Problem (just a 1-2 line summary!):
predict the labels by ensemble
"""
import collections
import os
import pandas as pd
import numpy as np


file_FAAAX ='FAAAX.csv'
file_SPY = 'SPY.csv'

'''
part 1
'''

def get_frames():
    label_faaax = []
    label_spy = []
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

tmp = get_frames()
df_faaax = tmp[0]
df_spy = tmp[1]

df_faaax_3year = df_faaax[df_faaax["Year"] < 2019]
df_spy_3year = df_spy[df_spy['Year'] < 2019]
df_faaax_2year = df_faaax[df_faaax["Year"] >= 2019].copy()
df_spy_2year = df_spy[df_spy['Year'] >= 2019].copy()
# df_faaax_last2_nolabel \
#     = pd.read_csv(file_FAAAX)[pd.read_csv(file_FAAAX)["Year"] >= 2019]
# df_spy_last2_nolabel \
#     = pd.read_csv(file_SPY)[pd.read_csv(file_SPY)['Year'] >= 2019]


L_faaax = len(df_faaax_3year['Return'].values)
L_spy = len(df_spy_3year['Return'].values)
L_positive_faaax = len(df_faaax_3year[df_faaax_3year["True Label"] == '+'])
L_positive_spy = len(df_spy_3year[df_spy_3year["True Label"] == '+'])
L_negative_faaax = len(df_faaax_3year[df_faaax_3year["True Label"] == '-'])
L_negative_spy = len(df_spy_3year[df_spy_3year["True Label"] == '-'])


# L_faaax_2y = len(df_faaax['Return'].values) - L_faaax
# L_spy_2y = len(df_spy['Return'].values) - L_spy
label_faaax_3y = df_faaax_3year["True Label"].values
label_spy_3y = df_spy_3year["True Label"].values
# label_faaax_2y = []
# label_spy_2y = []

default_up_faaax = L_positive_faaax/L_faaax
default_up_spy = L_positive_spy / L_spy
default_down_faaax = L_negative_faaax/L_faaax
default_down_spy = L_negative_spy / L_spy

'''
part 1
'''

def predict_by_w(W):
    # print("When W = ", W)
    tmp_faaax = label_faaax_3y.tolist()
    while len(tmp_faaax) != len(df_faaax['Return'].values):
        # convert the list to string and get the last w returns
        current_seq = ''.join(tmp_faaax[len(tmp_faaax) - W:len(tmp_faaax)])
        #get the number of up day and down day
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
    df_faaax_2year['Predicting label'] = predict_label_faaax
    # df_faaax_2year.loc[:, 'Predicting Label'] = predict_label_faaax

    tmp_spy = label_spy_3y.tolist()
    while len(tmp_spy) != len(df_spy['Return'].values):
        current_seq = ''.join(tmp_spy[len(tmp_spy) - W:len(tmp_spy)])
        up = len((''.join(tmp_spy)).split(current_seq + '+')) - 1
        down = len((''.join(tmp_spy)).split(current_seq + '-')) - 1
        if up > down:
            tmp_spy.append('+')
        elif up < down:
            tmp_spy.append('-')
        else:
            tmp_spy.append('+') if default_up_spy > default_down_spy \
                else tmp_spy.append('-')
    predict_label_spy = tmp_spy[len(label_spy_3y):len(tmp_spy)]
    df_spy_2year['Predicting Label'] = predict_label_spy
    return(predict_label_faaax, predict_label_spy,df_faaax_2year, df_spy_2year)

W_2 = predict_by_w(2)
W_2_faaax = W_2[0]
W_2_spy = W_2[1]
W_3 = predict_by_w(3)
W_3_faaax = W_3[0]
W_3_spy = W_3[1]
W_4 = predict_by_w(4)
W_4_faaax = W_4[0]
W_4_spy = W_4[1]

def ensemble():
    label_faaax = []
    label_spy = []

    for i in range(len(W_2_faaax)):
        list_3_faaax = [W_2_faaax[i], W_3_faaax[i], W_4_faaax[i]]
        list_3_spy = [W_2_spy[i], W_3_spy[i], W_4_spy[i]]
        cur_label_faaax = max(set(list_3_faaax), key=list_3_faaax.count)
        cur_label_spy = max(set(list_3_spy), key=list_3_spy.count)
        label_faaax.append(cur_label_faaax)
        label_spy.append(cur_label_spy)

    df_faaax_2year['Ensemble Label'] = label_faaax
    df_spy_2year['Ensemble Label'] = label_spy
    print('FAAAX Stock')
    print(df_faaax_2year)
    print('SPY Stock')
    print(df_spy_2year)
    return(df_faaax_2year, df_spy_2year)

ensemble()
'''
part 2
'''

def predict_percent_3(df_faaax_2year, df_spy_2year):
    true = df_faaax_2year['True Label'].values.tolist()
    predict = df_faaax_2year['Ensemble Label'].values.tolist()
    same = 0
    same_p = 0
    same_n = 0
    for i in range(len(true)):
        if true[i] == predict[i]:
            same = same + 1
        if true[i] == predict[i] and true[i] == '+':
            same_p = same_p + 1
        if true[i] == predict[i] and true[i] == '-':
            same_n = same_n + 1

    percent_faaax = same / len(true)
    percent_faaax_p = same_p / collections.Counter(true)['+']
    percent_faaax_n = same_n / collections.Counter(true)['-']
    print(percent_faaax, "of true labels (both positive and negative) I "
                         "have predicted correctly for FAAAX.")
    print(percent_faaax_p, "of '+' true labels I have predicted "
                         "correctly for FAAAX.")
    print(percent_faaax_n, "of '-' true labels I have predicted "
                         "correctly for FAAAX.")

    true = df_spy_2year['True Label'].values.tolist()
    predict = df_spy_2year['Ensemble Label'].values.tolist()
    same = 0
    same_p = 0
    same_n = 0
    for i in range(len(true)):
        if true[i] == predict[i]:
            same = same + 1
        if true[i] == predict[i] and true[i] == '+':
            same_p = same_p + 1
        if true[i] == predict[i] and true[i] == '-':
            same_n = same_n + 1

    percent_spy = same / len(true)
    percent_spy_p = same_p / collections.Counter(true)['+']
    percent_spy_n = same_n / collections.Counter(true)['-']
    print(percent_spy, "of true labels (both positive and negative) I "
                         "have predicted correctly for SPY.")
    print(percent_spy_p, "of '+' true labels I have predicted "
                           "correctly for SPY.")
    print(percent_spy_n, "of '-' true labels I have predicted "
                           "correctly for SPY.")



'''
part 3
'''
df_faaax_2year = ensemble()[0]
df_spy_2year = ensemble()[1]
def get_result_3():
    print("For ensemble")
    predict_percent_3(df_faaax_2year, df_spy_2year)



get_result_3()