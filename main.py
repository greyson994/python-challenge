import os
import csv

#Import budget_data.csv
pybank_path = os.path.join("budget_data.csv")

#declare arrays
date = []
profit_loss = []
change_in_profit_loss = []

#extract data and calculate
with open (pybank_path, newline ="") as pybank_data:
    pybank_reader =csv.reader(pybank_data, delimiter=",")
    next(pybank_reader)
    for row in pybank_reader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

    for i in range(1,len(profit_loss)):
        change_in_profit_loss.append(int(profit_loss[i]) - int(profit_loss[i-1]))
        max_profit = max(change_in_profit_loss)
        max_loss = min(change_in_profit_loss)
        max_profit_loss_date = str(date[change_in_profit_loss.index(max(change_in_profit_loss))+1])
        min_profit_loss_date = str(date[change_in_profit_loss.index(min(change_in_profit_loss))+1])

#print to terminal and more calculations
print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months: {len(date)}")
print (f"Total: ${sum(profit_loss)}")
average_change = sum(change_in_profit_loss) / (len(date) -1)
print (f"Average change: ${average_change:.2f}")
print (f"Greatest Increase in Profits: {max_profit_loss_date} ${max_profit}")
print (f"Greatest Decrease in Profits: {min_profit_loss_date} ${max_loss}")

#print to text file and more calculations
print ("Financial Analysis", file=open("PyBank.txt", "a"))
print ("----------------------------", file=open("PyBank.txt", "a"))
print (f"Total Months: {len(date)}", file=open("PyBank.txt", "a"))
print (f"Total: ${sum(profit_loss)}", file=open("PyBank.txt", "a"))
average_change = sum(change_in_profit_loss) / (len(date) -1)
print (f"Average change: ${average_change:.2f}", file=open("PyBank.txt", "a"))
print (f"Greatest Increase in Profits: {max_profit_loss_date} ${max_profit}", file=open("PyBank.txt", "a"))
print (f"Greatest Decrease in Profits: {min_profit_loss_date} ${max_loss}", file=open("PyBank.txt", "a"))