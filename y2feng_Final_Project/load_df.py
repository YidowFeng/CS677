"""
Yiduo Feng
Class: CS 677
Date: 04/27/2022

Description of Problem (just a 1-2 line summary!):
get dataframe
"""
import pandas as pd

file_name = "log2.csv"
sheet = "Raw Data"
#get data frame
df = pd.read_csv(file_name)
df = pd.DataFrame(df)
#labels 1 is class for all action
labels_1 = []
#labels 2 is check if allow
labels_2 = []
for i in df['Action'].values:
    if i == "allow":
        labels_1.append(0)
        labels_2.append(0)
    elif i == "deny":
        labels_1.append(1)
        labels_2.append(1)
    elif i == "drop":
        labels_1.append(2)
        labels_2.append(1)
    elif i == "reset-both":
        labels_1.append(3)
        labels_2.append(1)

#create new column
df['Class_1'] = labels_1
df['Class_2'] = labels_2

def print_df():
    print(df)

def get_df():
    return(df)

