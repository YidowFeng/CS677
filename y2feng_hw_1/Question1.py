# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/15/2022
Homework Problem: 1
Description of Problem (just a 1-2 line summary!): Bult the tables and
find the mean and sd for returns
"""

"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os

from prettytable import PrettyTable

ticker='FAAAX'
input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
# input_dir = ''
ticker_file = os.path.join(input_dir, ticker + '.csv')

"""
Help function for calculate the mean and standard deviation
"""
def find_mean_sd(all_R_set, negative_R_set, nonnegative_R_set):
    # Use formular to find the mean
    mean_all_R = sum(all_R_set) / len(all_R_set)
    mean_negative_R = sum(negative_R_set) / len(negative_R_set)
    mean_nonnegative_R = sum(nonnegative_R_set) / len(nonnegative_R_set)

    # Use formular to find the sd
    sd_all_R = (sum([((x - mean_all_R) ** 2) for x in all_R_set])
                / len(all_R_set)) ** 0.5
    sd_negative_R = (sum([((x - mean_negative_R) ** 2) for x in
                          negative_R_set]) / len(negative_R_set)) ** 0.5
    sd_nonnegative_R = (sum([((x - mean_nonnegative_R) ** 2) for x in
                    nonnegative_R_set]) / len(nonnegative_R_set)) ** 0.5
    #return the result
    return [mean_all_R, sd_all_R, len(negative_R_set), mean_negative_R,
    sd_negative_R, len(nonnegative_R_set), mean_nonnegative_R, sd_nonnegative_R]

try:
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    """    your code for assignment 1 goes here
    """
    # buld the lists
    all_R_set = []
    negative_R_set = []
    nonnegative_R_set = []
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    ng_mon = []
    ng_tue = []
    ng_wed = []
    ng_thu = []
    ng_fri = []
    non_mon = []
    non_tue = []
    non_wed = []
    non_thu = []
    non_fri = []
    #read line by line and put the returns into lists
    for line in lines[1:len(lines)]:
        current_r = float(line.split(',')[-3])
        current_date = line.split(',')[4]
        all_R_set.append(current_r)
        match current_date:
            case 'Monday':
                mon.append(current_r)
            case 'Tuesday':
                tue.append(current_r)
            case 'Wednesday':
                wed.append(current_r)
            case 'Thursday':
                thu.append(current_r)
            case 'Friday':
                fri.append(current_r)
        if current_r < 0:
            negative_R_set.append(current_r)
            match current_date:
                case 'Monday':
                    ng_mon.append(current_r)
                case 'Tuesday':
                    ng_tue.append(current_r)
                case 'Wednesday':
                    ng_wed.append(current_r)
                case 'Thursday':
                    ng_thu.append(current_r)
                case 'Friday':
                    ng_fri.append(current_r)
        else:
            nonnegative_R_set.append(current_r)
            match current_date:
                case 'Monday':
                    non_mon.append(current_r)
                case 'Tuesday':
                    non_tue.append(current_r)
                case 'Wednesday':
                    non_wed.append(current_r)
                case 'Thursday':
                    non_thu.append(current_r)
                case 'Friday':
                    non_fri.append(current_r)

        #current_day = line.split(',')[0]
        current_year = line.split(',')[1]
        if lines.index(line)+1 != len(lines):
            next_year = lines[lines.index(line) + 1].split(',')[1]
        else:
            next_year = -1
        # print the tables for each years
        if next_year != current_year or next_year == -1:

            mon_mean_sd = find_mean_sd(mon, ng_mon, non_mon)
            tus_mean_sd = find_mean_sd(tue, ng_tue, non_tue)
            wed_mean_sd = find_mean_sd(wed, ng_wed, non_wed)
            thu_mean_sd = find_mean_sd(thu, ng_thu, non_thu)
            fri_mean_sd = find_mean_sd(fri, ng_fri, non_fri)
            mon_mean_sd.insert(0, "Monday")
            tus_mean_sd.insert(0, "Tuesday")
            wed_mean_sd.insert(0, "Wednesday")
            thu_mean_sd.insert(0, "Thusday")
            fri_mean_sd.insert(0, "Friday")
            print('\n')
            print(current_year, "summary")
            table = PrettyTable(
                ["Day", "µ(R)", "σ(R)", "|R−|", "µ(R-)", "σ(R-)",
                 "|R+|", "µ(R+)", "σ(R+)"])

            # Add rows
            table.add_row(mon_mean_sd)
            table.add_row(tus_mean_sd)
            table.add_row(wed_mean_sd)
            table.add_row(thu_mean_sd)
            table.add_row(fri_mean_sd)


            print(table)
            # compare the number of days with negative and non-negative returns

            mean_sd = find_mean_sd(all_R_set, negative_R_set, nonnegative_R_set)
            print("The number of negative days is ", mean_sd[2])
            print("The number of non-negative days is ", mean_sd[5])
            if mean_sd[2] > mean_sd[5]:
                print("There are more negative days.")
            elif mean_sd[5] > mean_sd[2]:
                print("There are more non-negative days.")
            else:
                print(
                "The numbers of negative days and non-negative days are same.")


            if abs(mean_sd[3]) > mean_sd[6]:
                print("The average losing on a down day is ", mean_sd[3],
                      ", and the average gaining on a down day is ", mean_sd[6])
                print( "so my stock lose more on a ”down” day "
                      "than it gains on an ”up” days")
            else:
                print("The average losing on a down day is ", mean_sd[3],
                      ", and the average gaining on a down day is ", mean_sd[6])
                print( "so my stock gains more on an ”up” day "
                      "than it lose on a ”down” days")

            # initial all sets
            all_R_set = []
            negative_R_set = []
            nonnegative_R_set = []
            mon = []
            tue = []
            wed = []
            thu = []
            fri = []
            ng_mon = []
            ng_tue = []
            ng_wed = []
            ng_thu = []
            ng_fri = []
            non_mon = []
            non_tue = []
            non_wed = []
            non_thu = []
            non_fri = []

    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)












