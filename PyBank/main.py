
import csv 



with open("BeatlesSimpleCSVfile.csv") as csvfile:
    read_csv = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(read_csv)
    for row in read_csv:
        count_members += 1
        
count_members
print(f"The number of band members is {count_members}")



