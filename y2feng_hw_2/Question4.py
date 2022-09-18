# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/22/2022
Homework Problem: 4
Description of Problem (just a 1-2 line summary!):
get the table for accuracy
"""



import pandas as pd

from prettytable import PrettyTable

file_FAAAX ='FAAAX.csv'
file_SPY = 'SPY.csv'

'''
part 1
'''
#get the frame
def get_frames():
    label_faaax = []
    label_spy = []
    #read files
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

# set the variable for using in functions
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

'''
part 1
'''
#same as question 2
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
    # df_spy_2year['Predicting Label'] = predict_label_spy
    return(predict_label_faaax, predict_label_spy)

W_2 = predict_by_w(2)
W_2_faaax = W_2[0]
W_2_spy = W_2[1]
W_3 = predict_by_w(3)
W_3_faaax = W_3[0]
W_3_spy = W_3[1]
W_4 = predict_by_w(4)
W_4_faaax = W_4[0]
W_4_spy = W_4[1]
#same as question 3
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
    # print(df_faaax_2year)
    # print(df_spy_2year)
    return(df_faaax_2year, df_spy_2year)



# calculate the rate and print
def get_TF(W, ticker, true_label, prdct_label):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for i in range(len(true_label)):
        cur_prdct = prdct_label[i]
        cur_true = true_label[i]
        if cur_prdct == '+' and cur_prdct == cur_true:
            TP = TP + 1
        elif cur_prdct == '+' and cur_prdct != cur_true:
            FP = FP + 1
        elif cur_prdct == '-' and cur_prdct == cur_true:
            TN = TN + 1
        elif cur_prdct == '-' and cur_prdct != cur_true:
            FN = FN + 1
    accuracy = (TP + TN)/len(true_label)
    TPR = TP/(TP + FN)
    TNR = TN / (TN + FP)
    result_row = [W, ticker, TP, FP, TN, FN, accuracy, TPR, TNR]
    return(result_row)

def get_result_4():
    #create table
    table = PrettyTable(
        ["W", "ticker", "TP", "FP", "TN", "FN",
         "accuracy", "TPR", "TNR"])
    #build table
    true = df_faaax_2year['True Label'].values.tolist()
    ensemble_faaax = ensemble()[0]['Ensemble Label'].values.tolist()
    ensemble_spy = ensemble()[1]['Ensemble Label'].values.tolist()
    table.add_row(get_TF(2, "S&P-500", true, W_2_spy))
    table.add_row(get_TF(3, "S&P-500", true, W_3_spy))
    table.add_row(get_TF(4, "S&P-500", true, W_4_spy))
    table.add_row(get_TF("ensemble", "S&P-500", true, ensemble_spy))
    table.add_row(get_TF(2, "FAAAX", true, W_2_faaax))
    table.add_row(get_TF(3, "FAAAX", true, W_3_faaax))
    table.add_row(get_TF(4, "FAAAX", true, W_4_faaax))
    table.add_row(get_TF("ensemble", "FAAAX", true, ensemble_faaax))
    #print the table
    print(table)