import os
import csv

budget_data_csv = '/Users/ayokunleoluwole/Desktop/python-challenge/PyBank/Resources/budget_data.csv'
#output = '/Users/ayokunleoluwole/Desktop/python-challenge/PyBank/analysis/result.txt'

#the total number of months included in the dataset

#print(budget_data_csv)

#budget_data_csv = os.path.join('..', '..','Resources', 'budget_data.csv')

profit_loss = []
total_months = 0  
month_count = []
difference = []
total_profit_loss = 0 
greatest_increase = [] 
greatest_decrease = [] 
total_ave_change = 0
profit = 0


#for row in csv_reader:
        #total_months.append(row[0]) 

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #skip header row
   #print(f"Header: {csv_header}")

    for row in csv_reader:

#* The total number of months included in the dataset
        total_months = total_months +  1 
        #print (row[0])

#The net total amount of "Profit/Losses" over the entire period
        total_profit_loss = total_profit_loss + int(row[1])

#The changes in "Profit/Losses" over the entire period, 
# and then the average of those changes
        total_ave_change = int(row[1]) 

        profit_loss.append(int(row[1]))

    for i in range(1,len(profit_loss)):
        difference.append(profit_loss[i]- profit_loss[i-1])
        
        average = sum(difference) / len(difference)
    #print(profit_loss)
    #print(average)
    
    maxValue = max(row[1])

    print(maxValue)
    
    
    

    print("Financial Analysis")
    print ("----------------------------")
    print("Total Months: " + str(total_months))
    print(f"Total Profit/Losess: ${total_profit_loss}\n")
    print(f"Average Change: ${average}\n")
    
    