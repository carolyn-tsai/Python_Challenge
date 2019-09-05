# Import dependencies: 
    # os – Operating system interface.
    # csv – Comma Separated Values: This will allow me to import and export format for spreadsheets and databases. It will allow me to read and write CSV files.
    # operator – Standard operators as functions: I needed the sub() to find the profit/losses changes by each month. The sub() is found in the operator so I need to import operator in order to use sub(). Since I am only using sub(), I only imported that function from operator.
    # statistics – Mathematical statistics functions: Since part of the PyBank task was to find the average of the changes, I wanted to use mean() which means I need to import statistics. Since I am only using mean(), I only imported that function from statistics.

import os
import csv
from operator import sub
from statistics import mean

# Create path to collect data from the PyBank folder:

csvpath = os.path.join("..","PyBank","budget_data.csv")

# Open the CSV file:

with open(csvpath, newline="") as csvfile:

    # Split the data on commas:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header:

    header = next(csvreader)
    
    # Create empty lists for months and profit/losses:
    
    months = []
    profit_losses = []

    # Loop through rows in the “budget_data.csv” file to obtain months and profit/losses. I want to add each month or value into the appropriate list. 

    for row in csvreader:

        # To add the months into the months list, I used append() to add each item in column [0] of the file (which are the months).
        
        months.append(row[0])

       # To add the profit/losses values into the empty profit_losses list, I used append() to add each value in column[1] of the file (which are the profit/losses values). I set it to int because I will be working with the values as integers later.

        profit_losses.append(int(row[1]))

    # To get the total number of months in the file, I used len() to count the number of items in the months list.

    month_total = len(months)

    # To get the total profit amount, I used sum() to add up all the values in the profit_losses list.

    total_profit = sum(profit_losses)

    # To get a list of each change for the profit/losses, I made a list using map() and sub(). According to GeeksforGeeks, the map() function returns a list of the results after applying the given function to each item of a given iterable. In this case, I used map() on the sub() for the list of values in profit_losses. Because I do not want to use the first number in the list as there is no number to subtract it from, I am using index 1 (or second value in the list) for the start. I want the difference all the way until the last number, which will be index -1. I used list() because I will be finding max() and min() later. In order to avoid the value error of "max() arg is an empty sequence" I used list().

    pl_changes = list(map(sub, profit_losses[1:], profit_losses[:-1]))

    # To get the average changes, I used the mean function on the list of numbers found previously of the profit/losses changes. Using “f-string” formatting, I want my number to display up to 2 decimal points to match the example given in the PyBank README. I found the “f-string” formatting online and know that it is a new formatting added to Python 3.6. It is equivalent to “%.2f” in previous versions.    

    avg_changes = "{:0.2f}".format(mean(pl_changes))

    # To find the greatest increase in profits and the greatest decrease in profits, I used max() and min(), respectively, to find the largest and smallest number in the pl_changes list.

    greatest_inc_profits = max(pl_changes)
    greatest_dec_losses = min(pl_changes)

    # To get the month associated with the largest increase in profits and the month for the greatest decrease in profits, I need to first get the index numbers for each of those values in the pl_changes list.

    index_greatest_inc = pl_changes.index(greatest_inc_profits)
    index_greatest_dec = pl_changes.index(greatest_dec_losses)
    
    # From the month list, I can use the indexes found earlier to get the month associated with the greatest increase and the month associated with the greatest decrease. I need to add 1 to the index because the pl_changes list took out the initial value. I need to add that value back in to get the correct month.

    month_great_inc = months[(index_greatest_inc +1)]
    month_great_dec = months[(index_greatest_dec +1)]

    # To get all the data into the correct format, I created a variable "analysis" to hold all the information. I used “f-strings.”

    analysis = (
        f"Financial Analysis\n"
        f"-----------------------------\n"
        f"Total Months: {str(month_total)}\n"
        f"Total: ${str(total_profit)}\n"
        f"Average Change: ${avg_changes}\n"
        f"Greatest Increase in Profits: {month_great_inc} (${greatest_inc_profits})\n"
        f"Greatest Decrease in Profits: {month_great_dec} (${greatest_dec_losses})"
        )

    # Print the results to the terminal:

    print(analysis)

    # To create a new text file called “PyBank_Analysis,” I need to open the file using “write” mode.

    with open("PyBank_Analysis.txt","w") as text_file:

            # Because I was able to store all my data in the variable analysis, I can just write that variable into the new text file and all my data should be transcribed there in the correct formatting.
            
            text_file.write(analysis)
