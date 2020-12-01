import os
import csv

budget_csvpath = os.path.join('Resources', 'budget_data.csv')

with open(budget_csvpath, newline='') as budget_csvfile:

	budget_csvreader = csv.reader(budget_csvfile, delimiter=',')

	budget_list = list(budget_csvreader)
	head_budget_list = budget_list[0]
	data_budget_list = budget_list[1:]

	months_total = len(data_budget_list)

	net_total = 0
	change = 0
	

   
  
    
    

    

