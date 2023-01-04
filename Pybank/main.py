from os import path
import csv


# if __name__ == "__main__":
    # pass

def main():
    print("nasty")
    
    csvpath = r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\Pybank\Resources\budget_data.csv"
    with open(csvpath) as budgetdatacsv:
        csvRdr = csv.reader(budgetdatacsv,delimiter = ",")
        numOfMonths = 0
        totalPL = 0
        maxIncrease = 0
        maxIncDate = ""
        maxDecrease = 0
        maxDecDate = ""
        curAvg = 0
        
        for row in csvRdr:
            if(row[1] == 'Profit/Losses'): 
                continue
            profitLoss = int(row[1])
            numOfMonths += 1
            totalPL += profitLoss
            if(profitLoss > maxIncrease):
                maxIncrease = profitLoss
                maxIncDate = row[0]  
            elif (profitLoss < maxDecrease):
                maxDecrease = profitLoss
                maxDecDate = row[0]
            curAvg = curAvg + (profitLoss-curAvg)/numOfMonths
            analysisPath = r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\Pybank\analysis\finalAnalysis.txt"
        with open(analysisPath,"w") as newText:
            analysis = f"""
Financial Analysis 
-------------------
Total Months: {numOfMonths}
Total: ${totalPL}
Average Change: ${curAvg}
Greatest Increase in Profits: {maxIncDate} (${maxIncrease})
Greatest Decrease in Profits: {maxDecDate} (${maxDecrease})
"""
            print(analysis)
            newText.write(analysis)

main()
