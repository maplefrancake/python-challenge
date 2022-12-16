#PyBank script
import os
import csv

#we'll need our two filepaths- one for the input csv and one for the output txt
csvpath=os.path.join("Resources","budget_data.csv")
outputpath=os.path.join("analysis","pybank.txt")

#initiate our variables to calculate what we need to know
netProfit=0
totalMonths = 0
changeAvg = 0
previousProfit=0
changeList=[]
maxIncrease=-99999
maxIncreaseMonth=""
maxDecrease=99999
maxDecreaseMonth=""

#open up the file and start reading all the data
with open(csvpath) as pybank:
    csvreader = csv.DictReader(pybank)

    #for each row in the csv file, we'll want to add the net profits/losses together
    # so we can get a total over the amount of time we've measured
    for row in csvreader:
        netProfit += int(row["Profit/Losses"])
        totalMonths += 1

        #calculate change from previous month's profit/loss
        #add the change's value to a list, which can be used later on in the average calculation
        changeList.append(int(row["Profit/Losses"]) - previousProfit)
        previousProfit = int(row["Profit/Losses"])

        #check to see if this row is a larger increase/decrease than the current max profit/loss
        if int(row["Profit/Losses"]) > maxIncrease:
            maxIncrease = int(row["Profit/Losses"])
            maxIncreaseMonth = row["Date"]
        if int(row["Profit/Losses"]) < maxDecrease:
            maxDecrease = int(row["Profit/Losses"])
            maxDecreaseMonth = row["Date"]

    #calculate the total change and average
    #I'm removing the first change value, since this corresponds
    # to the first entry in the list and there shouldn't be a change to include
    changeList.remove(changeList[0])
    changeAvg = sum(changeList)/(totalMonths-1)

#print out data to the terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netProfit}")
print(f"Average Change: ${changeAvg:.2f}")
print(f"Greatest Increase in Profits: {maxIncreaseMonth} (${maxIncrease})")
print(f"Greatest Decrease in Profits: {maxDecreaseMonth} (${maxDecrease})")

#print data to our txt file
with open(outputpath, 'w') as pybankoutput:
    pybankoutput.write("Financial Analysis")
    pybankoutput.write("\n------------------------")
    pybankoutput.write(f"\nTotal Months: {totalMonths}")
    pybankoutput.write(f"\nTotal: ${netProfit}")
    pybankoutput.write(f"\nAverage Change: ${changeAvg:.2f}")
    pybankoutput.write(f"\nGreatest Increase in Profits: {maxIncreaseMonth} (${maxIncrease})")
    pybankoutput.write(f"\nGreatest Decrease in Profits: {maxDecreaseMonth} (${maxDecrease})")
