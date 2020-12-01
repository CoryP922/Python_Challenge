import os
import csv
with open(csvpath) as csvfile: 

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
csvpath = os.path.join("..", "Resources", "budget_data.csv")

