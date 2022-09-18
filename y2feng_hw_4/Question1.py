"""
Yiduo Feng
Class: CS 677
Date: 04/06/2022
Homework Problem: 1
Description of Problem (just a 1-2 line summary!):
 construct the visual representations of
correponding correlation matrices

"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import statistics

file = "heart_failure_clinical_records_dataset.csv"
#read file
df = pd.read_csv(file)
df = pd.DataFrame(df, columns=["creatinine_phosphokinase", "serum_creatinine",
                               "serum_sodium", "platelets", "DEATH_EVENT"])
#get surviving and deceased

df_0 = df[df["DEATH_EVENT"] == 0]
df_1 = df[df["DEATH_EVENT"] == 1]
def show_df():
    print("df_0")
    print(df_0)
    print("df_1")
    print(df_1)
corr_0 = df_0.corr()
# M0 = plt.matshow(corr_0)

# Visualize correlation matrix
M_0 = plt.figure()
axes_0 = M_0.add_subplot(111)

# using the matshow() function
ax_0 = axes_0.matshow(df_0.corr(),
                  interpolation='nearest')
# will do an example with more features
M_0.colorbar(ax_0)
# save plot as pdf
plt.savefig('M_0.pdf')
def get_M0():
    print(corr_0)
    plt.show()
get_M0()
df_0.corr()

#print(corr_0)

corr_1 = df_1.corr()
# M1 = plt.matshow(corr_1)

# Visualize correlation matrix
M_1 = plt.figure()
axes_1 = M_1.add_subplot(111)

# using the matshow() function
ax_1 = axes_1.matshow(df_1.corr(),
                  interpolation='nearest')
# will do an example with more features
M_1.colorbar(ax_1)
# save plot as pdf
plt.savefig('M_1.pdf')
def get_M1():
    print(corr_1)
    plt.show()
get_M1()
df_1.corr()