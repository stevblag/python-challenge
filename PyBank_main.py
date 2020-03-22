import os
import csv
from pathlib import Path 

input_file = Path("python-challenge", "PyBank", "budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv
with open(input_file,newline="", encoding="utf-8") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip header & iterate
    header = next(csvreader)  

    # Iterate rows in csv
    for row in csvreader: 

        # Append total months & total profit
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate profits to get the monthly change
    for i in range(len(total_profit)-1):
        
        # Take the difference between months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain max & min of montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max & min to proper month via month list & index
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = Path("python-challenge", "PyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


