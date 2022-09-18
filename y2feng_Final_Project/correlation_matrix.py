"""
Yiduo Feng
Class: CS 677
Date: 04/27/2022

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
from load_df import get_df

# def get_frames():
df = get_df()
df = df.drop(columns=["Action", "Class_2"])
#get surviving and deceased

df_0 = df[df["Class_1"] == 0]
df_1 = df[df["Class_1"] == 1]
df_2 = df[df["Class_1"] == 2]
df_3 = df[df["Class_1"] == 3]
# def show_df():
#     print("df_0")
#     print(df_0)
#     print("df_1")
#     print(df_1)
# corr_0 = df_0.corr()
# M0 = plt.matshow(corr_0)
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
corr_0 = df_0.corr()
# Visualize correlation matrix
M_0 = plt.figure()
axes_0 = M_0.add_subplot(111)

# using the matshow() function
ax_0 = axes_0.matshow(df_0.corr(),
                  interpolation='nearest')
# will do an example with more features
M_0.colorbar(ax_0)
# save plot as pdf
# plt.savefig('M_0.pdf')
def get_M0():
    print(corr_0)
    plt.show()
get_M0()
df_0.corr()

#print(corr_0)
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
# plt.savefig('M_1.pdf')
def get_M1():
    print(corr_1)
    plt.show()
get_M1()
df_1.corr()
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
corr_2 = df_2.corr()
# M2 = plt.matshow(corr_2)

# Visualize correlation matrix
M_2 = plt.figure()
axes_2 = M_2.add_subplot(111)

# using the matshow() function
ax_2 = axes_2.matshow(df_2.corr(), interpolation='nearest')
# will do an example with more features
M_2.colorbar(ax_2)
# save plot as pdf
# plt.savefig('M_2.pdf')
def get_M2():
    print(corr_2)
    plt.show()
get_M2()
df_2.corr()
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
corr_3 = df_3.corr()
# M3 = plt.matshow(corr_3)

# Visualize correlation matrix
M_3 = plt.figure()
axes_3 = M_3.add_subplot(111)

# using the matshow() function
ax_3 = axes_3.matshow(df_3.corr(), interpolation='nearest')
# will do an example with more features
M_3.colorbar(ax_3)
# save plot as pdf
# plt.savefig('M_3.pdf')
def get_M3():
    print(corr_3)
    plt.show()
get_M3()
df_3.corr()