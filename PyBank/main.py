import csv
csvpath = "./Resources/budget_data.csv"
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_months = 0
    profit_losses = 0

    last_profit= 0

    changes = []
    month_changes = []

    for row in csvreader:
        total_months += 1
        # print(row)
        # print("==============================")
       
        profit_losses = profit_losses + int(row[1])
 
        if (total_months == 1):
            last_profit = int(row[1])
        else:
            change = int(row[1]) - last_profit
            changes.append(change)
            month_changes.append(row[0])

            last_profit = int(row[1])

    print(total_months)
    print(profit_losses)
   

    # Calculate the average change
    average_change = sum(changes) / len(changes)
    print(average_change)

    max_change = max(changes)
    max_month_indx = changes.index(max_change)
    max_month = month_changes[max_month_indx]

    print(max_change)
    print(max_month)
    
    min_change = min(changes)
    min_month_indx = changes.index(min_change)
    min_month = month_changes[min_month_indx]   
    output = (
        F"Financial Analysis\n"
        f"----------------------\n"
        f"total months : {total_months}\n"
        f"total : {profit_losses}\n"
        f"maximum change : {max_change}\n"
        f"max month : {max_month}\n"
        f"average change : {average_change}\n"
        f"minimum change : {min_change}\n"
        f" min month : {min_month}"
    )
    
    print(output)
with open("./analysis/ouput.txt", "w") as output_file:
    output_file.write(output)