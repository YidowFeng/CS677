# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/22/2022
Homework Problem: 1
Description of Problem (just a 1-2 line summary!):
Read the csv files into dataframe and then find the probabilities of the
cases question given
"""

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

    print(df_faaax)
    print(df_spy)
    return(df_faaax, df_spy)

tmp = get_frames()
df_faaax = tmp[0]
df_spy = tmp[1]
'''
part 2
'''
df_faaax_3year = df_faaax[df_faaax["Year"] < 2019]
df_spy_3year = df_spy[df_spy['Year'] < 2019]

L_faaax = 0
L_spy = 0
L_positive_faaax = 0
L_positive_spy = 0
L_negative_faaax = 0
L_negative_spy = 0
#get the L number
def prob_up():
    L_faaax = len(df_faaax_3year['Return'].values)
    L_spy = len(df_spy_3year['Return'].values)
    L_positive_faaax = len(df_faaax_3year[df_faaax_3year["True Label"] == '+'])
    L_positive_spy = len(df_spy_3year[df_spy_3year["True Label"] == '+'])
    L_negative_faaax = len(df_faaax_3year[df_faaax_3year["True Label"] == '-'])
    L_negative_spy = len(df_spy_3year[df_spy_3year["True Label"] == '-'])

    print("L for FAAAX stock is ", L_faaax, ". L+ is ", L_positive_faaax,
          ". L- is ", L_negative_faaax)
    print("L for SPY stock is ", L_spy, ". L+ is ", L_positive_spy,
          ". L- is ", L_negative_spy)

    print("The FAAAX default probability p∗ that the next day is an ”up” day"
          " is ", L_positive_faaax/L_faaax)
    print("The SPY default probability p∗ that the next day is an ”up” day"
          " is ", L_positive_spy / L_spy)

prob_up()

'''
part 3
'''
label_faaax_3y = []
label_spy_3y = []

def consecutive_down():
    print("Compute the probability that after seeing k consecutive ”down days”, "
          "the next day is an ”up day”")
    label_faaax_3y = df_faaax_3year["True Label"].values
    label_spy_3y = df_spy_3year["True Label"].values
    # When k = 1
    #convert the list to string and then split the string by the sequence so
    #that we can get the number of sequence
    up_faaax = len((''.join(label_faaax_3y)).split('-+')) - 1
    up_spy = len((''.join(label_spy_3y)).split('-+')) - 1
    total_faaax = len((''.join(label_faaax_3y)).split('--')) - 1 + up_faaax
    total_spy = len((''.join(label_spy_3y)).split('--')) - 1 + up_spy
    print("When k = 1")
    print("The probability of FAAAX is", up_faaax/total_faaax)
    print("The probability of SPY is", up_spy/total_spy)
    # When k = 2
    up_faaax = len((''.join(label_faaax_3y)).split('--+')) - 1
    up_spy = len((''.join(label_spy_3y)).split('--+')) - 1
    total_faaax = len((''.join(label_faaax_3y)).split('---')) - 1 + up_faaax
    total_spy = len((''.join(label_spy_3y)).split('---')) - 1 + up_spy
    print("When k = 2")
    print("The probability of FAAAX is", up_faaax / total_faaax)
    print("The probability of SPY is", up_spy / total_spy)
    # When k = 3
    up_faaax = len((''.join(label_faaax_3y)).split('---+')) - 1
    up_spy = len((''.join(label_spy_3y)).split('---+')) - 1
    total_faaax = len((''.join(label_faaax_3y)).split('----')) - 1 + up_faaax
    total_spy = len((''.join(label_spy_3y)).split('----')) - 1 + up_spy
    print("When k = 3")
    print("The probability of FAAAX is", up_faaax / total_faaax)
    print("The probability of SPY is", up_spy / total_spy)

consecutive_down()

'''
part 4
'''

def consecutive_up():
    print("Compute the probability that after seeing k consecutive ”up days”, "
          "the next day is still an ”up day”")
    label_faaax_3y = df_faaax_3year["True Label"].values
    label_spy_3y = df_spy_3year["True Label"].values
    # When k = 1
    up_faaax = len((''.join(label_faaax_3y)).split('++')) - 1
    up_spy = len((''.join(label_spy_3y)).split('++')) - 1
    total_faaax = len((''.join(label_faaax_3y)).split('+-')) - 1 + up_faaax
    total_spy = len((''.join(label_spy_3y)).split('+-')) - 1 + up_spy
    print("When k = 1")
    print("The probability of FAAAX is", up_faaax/total_faaax)
    print("The probability of SPY is", up_spy/total_spy)
    # When k = 2
    up_faaax = len((''.join(label_faaax_3y)).split('+++')) - 1
    up_spy = len((''.join(label_spy_3y)).split('+++')) - 1
    total_faaax = len((''.join(label_faaax_3y)).split('++-')) - 1 + up_faaax
    total_spy = len((''.join(label_spy_3y)).split('++-')) - 1 + up_spy
    print("When k = 2")
    print("The probability of FAAAX is", up_faaax / total_faaax)
    print("The probability of SPY is", up_spy / total_spy)
    # When k = 3
    up_faaax = len((''.join(label_faaax_3y)).split('++++')) - 1
    up_spy = len((''.join(label_spy_3y)).split('++++')) - 1
    total_faaax = len((''.join(label_faaax_3y)).split('+++-')) - 1 + up_faaax
    total_spy = len((''.join(label_spy_3y)).split('+++-')) - 1 + up_spy
    print("When k = 3")
    print("The probability of FAAAX is", up_faaax / total_faaax)
    print("The probability of SPY is", up_spy / total_spy)

consecutive_up()