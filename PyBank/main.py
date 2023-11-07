import csv

filein = "/Users/elizabethdworkin/Desktop/Data Analytics/Challenge III/python-challenge/PyBank/Resources/budget_data.csv"
fileout = "/Users/elizabethdworkin/Desktop/Data Analytics/Challenge III/python-challenge/PyBank/Analysis/Analysis of PyBank"

# read data
with open(filein) as f:
    reader = csv.reader(f)
    data = list(reader)

# clean data    
data = data[1:] # starts from index 1 - all the way to end 
for row in data:
    row[1] = int(row[1])

    

# Total number of months
total_months = len(data)

#Net total amount of "Profit/Losses" over the entire period 
    #Should read: "Total: $22564198" (can I format this to include commas?)

total = 0
for month, amount in data:
  total = total + amount
    

#Changes in "Profit/Losses" over the entire period, and then the average of those changes
    #Should read: "Average Change: $-8311.11" column is named "Profit/Losses"

total_diff = 0
for i in range(1, len(data)):
  diff = data[i][1] - data[i-1][1]
  total_diff = total_diff + diff
average_change = round(total_diff / (total_months - 1), 2)

  
#Greatest increase in profits (date and amount) over the entire period 
    #Should read: "Greatest Increase in Profits: Aug-16 ($1862002)"

max_diff_month = None
max_diff = None
for i in range(1, len(data)):
  diff = data[i][1] - data[i-1][1]
  if max_diff is None or diff > max_diff:
    max_diff = diff
    max_diff_month = data[i][0]

#Greatest decrease in profits (date and amount) over the entire period
    #Should read: "Greatest Decrease in Profits: Feb-14 ($-1825558)"

min_diff_month = None
min_diff = None
for i in range(1, len(data)):
  diff = data[i][1] - data[i-1][1]
  if min_diff is None or diff < min_diff:
    min_diff = diff
    min_diff_month = data[i][0]

  
#Your final script should both print the analysis to the terminal AND export a text file with the results.

output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total}
Average Change: ${average_change}
Greatest Increase in Profits: {max_diff_month} (${max_diff})
Greatest Decrease in Profits: {min_diff_month} (${min_diff})"""


print(output)

with open(fileout, "w") as f:
  f.write(output)
