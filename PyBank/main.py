

import csv 

total_months = 0

with open("budget_data") as csvfile:
    read_csv = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(read_csv)
    for row in read_csv:
        total_months += 1
        
total_months

print(f"The number included in the dataset is {total_months}")



