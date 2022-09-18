"""
Yiduo Feng
Class: CS 677
Date: 04/15/2022
Homework Problem: 5
Description of Problem (just a 1-2 line summary!):
get summary
"""
from Question2 import get_summary_2
from Question3 import get_summary_3
from Question4 import get_summary_4
from prettytable import PrettyTable
#print the table
table = PrettyTable()
table.field_names = ["Model", "TP", "FP", "TN", "FN", "accuracy", "TPR", "TNR"]

table.add_row(get_summary_2())
table.add_row(get_summary_3())
table.add_row(get_summary_4())
def get_table():
    print(table)

get_table()