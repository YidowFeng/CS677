# -*- coding: utf-8 -*-
"""
Yiduo Feng
Class: CS 677
Date: 03/15/2022
Homework Problem: 3
Description of Problem (just a 1-2 line summary!): Compute the aggregate table
 across all 5 years,one table for both your stock and one table
 for S&P-500 (using data for ”spy”).
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

"""
Help function for calculate the mean and standard deviation
"""
def find_mean_sd(all_R_set, negative_R_set, nonnegative_R_set):
    mean_all_R = sum(all_R_set) / len(all_R_set)
    mean_negative_R = sum(negative_R_set) / len(negative_R_set)
    mean_nonnegative_R = sum(nonnegative_R_set) / len(nonnegative_R_set)
    sd_all_R = (sum([((x - mean_all_R) ** 2) for x in all_R_set])
                / len(all_R_set)) ** 0.5
    sd_negative_R = (sum([((x - mean_negative_R) ** 2) for x in
                          negative_R_set]) / len(negative_R_set)) ** 0.5
    sd_nonnegative_R = (sum([((x - mean_nonnegative_R) ** 2) for x in
                    nonnegative_R_set]) / len(nonnegative_R_set)) ** 0.5
    return [mean_all_R, sd_all_R, len(negative_R_set), mean_negative_R,
    sd_negative_R, len(nonnegative_R_set), mean_nonnegative_R, sd_nonnegative_R]

def get_return_sets(ticker_file, ticker):

    try:
        with open(ticker_file) as f:
            lines = f.read().splitlines()
        print('opened file for ticker: ', ticker)
        """    your code for assignment 1 goes here
        """
        #buld the lists
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
        #read the data lione by line
        for line in lines[1:len(lines)]:
            current_r = float(line.split(',')[-3])
            current_date = line.split(',')[4]
            # put the data into the lists
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
        # return all lists
        return([all_R_set, negative_R_set, nonnegative_R_set,
                mon, ng_mon, non_mon, tue, ng_tue, non_tue, wed, ng_wed,
                non_wed, thu, ng_thu, non_thu, fri, ng_fri, non_fri
                ])



    except Exception as e:
        print(e)
        print('failed to read stock data for ticker: ', ticker)

#print the table
def get_table(mon, ng_mon, non_mon, tue, ng_tue, non_tue, wed, ng_wed, non_wed,
              thu, ng_thu, non_thu, fri, ng_fri, non_fri):
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
    return([mon_mean_sd, tus_mean_sd, wed_mean_sd, thu_mean_sd, fri_mean_sd])


print("The table of FAAAX")
r_faaax = get_return_sets(ticker_file_FAAAX, ticker_FAAAX)
mean_sd_faaax = get_table(r_faaax[3], r_faaax[4], r_faaax[5], r_faaax[6],
    r_faaax[7], r_faaax[8], r_faaax[9], r_faaax[10], r_faaax[11], r_faaax[12],
          r_faaax[13], r_faaax[14], r_faaax[15], r_faaax[16], r_faaax[17])
print("The table of SPY")
r_spy = get_return_sets(ticker_file_SPY, ticker_SPY)
mean_sd_spy = get_table(r_spy[3], r_spy[4], r_spy[5], r_spy[6], r_spy[7],
        r_spy[8], r_spy[9], r_spy[10], r_spy[11], r_spy[12],
          r_spy[13], r_spy[14], r_spy[15], r_spy[16], r_spy[17])

r_mean_faaax = []
r_mean_spy = []
max_day_faaax = 0
min_day_faaax = 0
max_day_spy = 0
min_day_spy = 0
inx_max_day_faaax = 0
inx_min_day_faaax  = 0
inx_max_day_spy = 0
inx_min_day_spy = 0
for i in range(5):
    if mean_sd_faaax[i][1] > max_day_faaax:
        max_day_faaax = mean_sd_faaax[i][1]
        inx_max_day_faaax = i
    if mean_sd_spy[i][1] > max_day_spy:
        max_day_spy = mean_sd_spy[i][1]
        inx_max_day_spy = i
    if mean_sd_faaax[i][1] < min_day_faaax:
        min_day_faaax = mean_sd_faaax[i][1]
        inx_min_day_faaax = i
    if mean_sd_spy[i][1] < min_day_spy:
        min_day_spy = mean_sd_spy[i][1]
        inx_min_day_spy = i
    # r_mean_faaax.append(mean_sd_faaax[i][1])
    # r_mean_spy.append(mean_sd_spy[i][1])

#get the best day of week
match inx_max_day_faaax:
    case 0:
        print("The best day of FAAAX is Monday.")
    case 1:
        print("The best day of FAAAX is Monday.")
    case 2:
        print("The best day of FAAAX is Wednesday.")
    case 3:
        print("The best day of FAAAX is Monday.")
    case 4:
        print("The best day of FAAAX is Monday.")
        
match inx_min_day_faaax:
    case 0:
        print("The worst day of faaax is Monday.")
    case 1:
        print("The worst day of faaax is Monday.")
    case 2:
        print("The worst day of faaax is Wednesday.")
    case 3:
        print("The worst day of faaax is Monday.")
    case 4:
        print("The worst day of faaax is Monday.")

match inx_max_day_spy:
    case 0:
        print("The best day of spy is Monday.")
    case 1:
        print("The best day of spy is Monday.")
    case 2:
        print("The best day of spy is Wednesday.")
    case 3:
        print("The best day of spy is Monday.")
    case 4:
        print("The best day of spy is Monday.")
        
match inx_min_day_spy:
    case 0:
        print("The worst day of spy is Monday.")
    case 1:
        print("The worst day of spy is Monday.")
    case 2:
        print("The worst day of spy is Wednesday.")
    case 3:
        print("The worst day of spy is Monday.")
    case 4:
        print("The worst day of spy is Monday.")
# check if they are same
if inx_max_day_faaax == inx_max_day_spy and \
        inx_min_day_spy == inx_min_day_faaax:
    print("These days are the same for my stock as they are for S&P-500")
# print("The best day of FAAAX", max(r_mean_faaax))
# print("The best day of SPY", max(r_mean_spy))











