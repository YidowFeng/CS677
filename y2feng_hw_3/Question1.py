"""
Yiduo Feng
Class: CS 677
Date: 03/30/2022
Homework Problem: 1
Description of Problem (just a 1-2 line summary!):
Built the dataframe and get table

"""
import os
import pandas as pd
import numpy as np
from prettytable import PrettyTable
import statistics

file = "data_banknote_authentication.txt"
'''
f1 - variance of wavelet transformed image
f2 - skewness of wavelet transformed image
f3 - curtosis of wavelet transformed image
f4 - entropy of image
'''
# def get_frames():

#read files
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

def get_df():
    print(df)


def find_mean_sd(df):
    # Use formular to find the mean
    mean_f1 = round(statistics.mean(df['f1'].values), 2)
    mean_f2 = round(statistics.mean(df['f2'].values), 2)
    mean_f3 = '%.2f'%statistics.mean(df['f3'].values)
    mean_f4 = round(statistics.mean(df['f4'].values), 2)


    # Use formular to find the sd
    sd_f1 = round(statistics.stdev(df['f1'].values), 2)
    sd_f2 = round(statistics.stdev(df['f2'].values), 2)
    sd_f3 = round(statistics.stdev(df['f3'].values), 2)
    sd_f4 = round(statistics.stdev(df['f4'].values), 2)

    return([mean_f1, sd_f1, mean_f2, sd_f2, mean_f3, sd_f3, mean_f4, sd_f4])

def get_table_1():
    table = PrettyTable(
        ["Class", "µ(f1)", "σ(f1)", "µ(f2)", "σ(f2)", "µ(f3)",
         "σ(f3)", "µ(f4)", "σ(f4)"])

    row_0 = find_mean_sd(df_green)
    row_1 = find_mean_sd(df_red)
    row_all = find_mean_sd(df)
    row_0.insert(0, "0")
    row_1.insert(0, "1")
    row_all.insert(0, "all")

    # Add rows
    table.add_row(row_0)
    table.add_row(row_1)
    table.add_row(row_all)

    print(table)

get_table_1()
