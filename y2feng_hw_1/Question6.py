# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/15/2022
Homework Problem: 6
Description of Problem (just a 1-2 line summary!): folloe the 3 cases in the
question and find the result, then compare with Q 4 and Q 5.
"""

"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os

from prettytable import PrettyTable

ticker_FAAAX ='FAAAX'
ticker_SPY = 'SPY'
input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
# input_dir = ''
ticker_file_FAAAX = os.path.join(input_dir, ticker_FAAAX + '.csv')
ticker_file_SPY = os.path.join(input_dir, ticker_SPY + '.csv')

returns_faaax = []
returns_spy = []
sort_return_faaax = []
worst_ten_faaax = []
sort_re_return_faaax = []
best_ten_faaax = []
sort_return_spy = []
worst_ten_spy = []
sort_re_return_spy = []
best_ten_spy = []

try:

    ## Open faaax stock and put the return in a list
    with open(ticker_file_FAAAX) as f:
        lines_faaax = f.read().splitlines()
    print('opened file for ticker: ', ticker_FAAAX)
    """    your code for assignment 1 goes here
    """
    returns = []
    for line in lines_faaax[1:len(lines_faaax)]:
        returns.append(float(line.split(',')[-3]))
    ## get best ten and worst ten days
    returns_faaax = returns
    returns_faaax.sort()
    sort_return_faaax = returns
    worst_ten_faaax = sort_return_faaax[0:10]
    returns_faaax.sort(reverse=True)
    sort_re_return_faaax = returns
    best_ten_faaax = sort_re_return_faaax[0:10]

    ## Open spy stock and put the return in a list
    with open(ticker_file_SPY) as f:
        lines_spy = f.read().splitlines()
    print('opened file for ticker: ', ticker_SPY)
    returns = []
    for line in lines_spy[1:len(lines_spy)]:
        returns.append(float(line.split(',')[-3]))
    ## get best ten and worst ten days
    returns_spy = returns
    returns_spy.sort()
    sort_return_spy = returns
    worst_ten_spy = sort_return_spy[0:10]
    returns_spy.sort(reverse=True)
    sort_re_return_spy = returns
    best_ten_spy = sort_re_return_spy[0:10]

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker_FAAAX,
          "or", ticker_SPY)

# 1,(a)
print("The case that I missed the best ten days")
money = 100
for current_r in returns_faaax[1:len(returns_faaax)]:
    if current_r >= 0 and current_r not in best_ten_faaax:
        money = money * (1 + current_r)

print("(a)", ticker_FAAAX, "I will have", money,
      "on the last trading day of 2020")


money = 100
for current_r in returns_spy[1:len(returns_spy)]:
    if current_r >= 0 and current_r not in best_ten_spy:
        money = money * (1+current_r)

print("(a)", ticker_SPY, "I will have", money,
      "on the last trading day of 2020")

# 1,(b)
print("The case that I missed the worst ten days")
money = 100
for current_r in returns_faaax[1:len(returns_faaax)]:
    if current_r >= 0 or current_r in worst_ten_faaax:
        money = money * (1 + current_r)

print("(b)", ticker_FAAAX, "I will have", money,
      "on the last trading day of 2020")

money = 100
for current_r in returns_spy[1:len(returns_spy)]:
    if current_r >= 0 or current_r in worst_ten_spy:
        money = money * (1 + current_r)

print("(b)", ticker_SPY, "I will have", money,
      "on the last trading day of 2020")

# 1,(c)
print("The case that I missed the worst 5 days and best 5 days")
money = 100
for current_r in returns_faaax[1:len(returns_faaax)]:
    if (current_r >= 0 or current_r in worst_ten_faaax[0:5]) \
            and current_r not in best_ten_faaax[0:5]:
        money = money * (1 + current_r)

print("(c)", ticker_FAAAX, "I will have", money,
      "on the last trading day of 2020")

money = 100
for current_r in returns_spy[1:len(returns_spy)]:
    if (current_r >= 0 or current_r in worst_ten_spy[0:5]) \
            and current_r not in best_ten_spy[0:5]:
        money = money * (1 + current_r)

print("(c)", ticker_SPY, "I will have", money,
      "on the last trading day of 2020")




