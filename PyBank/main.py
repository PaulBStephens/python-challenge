# Create dependencies
import csv 

# file to load
file_to_load = "budget_data.csv"

# Read the csv and convert info into lists; the first and second columns are data given, the third to store data calculated from the second column 
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)
    
    # I used the 'next' function to skip first title row in csv file
    next(reader) 
    date = []
    revenue = []
    
    # defined revenue as a float of row 1, and date as row 0 
    for row in reader:
        revenue.append(float(row[1]))
        date.append(row[0])

        # printing info
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    sum_of_revenue = '{0:.0f}'.format(sum(revenue))
    print(f"Total Revenue: ${sum_of_revenue}")

    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

    print("Average Revenue Change: $", '{0:.2f}'.format(avg_rev_change))
    print("Greatest Increase in Revenue to the Next Month:", max_rev_change_date,"($", round(max_rev_change),")")
    print("Greatest Decrease in Revenue to the Next Month:", min_rev_change_date,"($", round(min_rev_change),")")
          
## now need to export the same info I printed to a text file
with open("outputPyBank.txt", "a") as f:
    print("Financial Analysis", file=f)
    print("-----------------------------------", file=f)
    print("Total Months:", len(date), file=f)
    print(f"Total Revenue: ${sum_of_revenue}", file=f)
    print("Average Revenue Change: $", '{0:.2f}'.format(avg_rev_change), file=f)
    print("Greatest Increase in Revenue to the Next Month:", max_rev_change_date,"($", round(max_rev_change),")", file=f)
    print("Greatest Decrease in Revenue to the Next Month:", min_rev_change_date,"($", round(min_rev_change),")", file=f)
