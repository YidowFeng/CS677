"""
Yiduo Feng
Class: CS 677
Date: 04/15/2022
Homework Problem: 1
Description of Problem (just a 1-2 line summary!):
get dataframe
"""
import pandas as pd

file_name = "CTG.xls"
sheet = "Raw Data"
#get data frame
df = pd.read_excel(io=file_name, sheet_name=sheet)
df = pd.DataFrame(df, columns=["MSTV", "Width", "Mode", "Variance", "NSP"])
nsp_2 = []
for i in df['NSP'].values:
    if i == 1:
        nsp_2.append(1)
    else:
        nsp_2.append(0)
#create new column
df['NSP_2'] = nsp_2
df = df.drop([0, len(df)-1, len(df)-2, len(df)-3])
def get_df():
    print(df)

