# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/15/2022
Homework Problem: 5
Description of Problem (just a 1-2 line summary!): Consider ”buy-and-hold”
strategy: i buy on the first trading day and sell on the last day. So i do
not listen to my oracle at all. As before, assume that i start with $100
for both my stock and ”spy”.
"""

"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os


ticker_FAAAX ='FAAAX'
ticker_SPY = 'SPY'
input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
# input_dir = ''
ticker_file_FAAAX = os.path.join(input_dir, ticker_FAAAX + '.csv')
ticker_file_SPY = os.path.join(input_dir, ticker_SPY + '.csv')


try:
    with open(ticker_file_FAAAX) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker_FAAAX)
    """    your code for assignment 1 goes here
    """
    # find result for my stock
    money = 100
    for line in lines[1:len(lines)]:
        current_r = float(line.split(',')[-3])
        money = money * (1+current_r)

    print("For", ticker_FAAAX, "I will have", money,
          "on the last trading day of 2020")
    # find result for spy
    with open(ticker_file_SPY) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker_SPY)

    money = 100
    for line in lines[1:len(lines)]:
        current_r = float(line.split(',')[-3])

        money = money * (1+current_r)

    print("For", ticker_SPY, "I will have", money,
          "on the last trading day of 2020")


except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker_SPY,
          "or", ticker_FAAAX)


