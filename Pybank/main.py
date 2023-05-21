from os import path
import csv


# if __name__ == "__main__":
    # pass

def main():
    csv_path = r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\Pybank\Resources\budget_data.csv"
    with open(csv_path) as budgetdatacsv:
        csv_reader = csv.reader(budgetdatacsv,delimiter = ",")
        number_of_months = 0
        total_profit_loss = 0
        max_increase = 0
        max_increase_date = ""
        max_decrease = 0
        max_decrease_date = ""
        current_average = 0
        
        for row in csv_reader:
            if(row[1] == 'Profit/Losses'): 
                continue
            profit_loss = int(row[1])
            number_of_months += 1
            total_profit_loss += profit_loss
            if(profit_loss > max_increase):
                max_increase = profit_loss
                max_increase_date = row[0]  
            elif (profit_loss < max_decrease):
                max_decrease = profit_loss
                max_decrease_date = row[0]
            current_average = current_average + (profit_loss-current_average)/number_of_months
            analysis_path = r"G:\CODE\Data Analytics Bootcamp\Data_Analytics\Class_Folder\M3_Python\chllenge\python-challenge\Pybank\analysis\finalAnalysis.txt"
        with open(analysis_path,"w") as new_text:
            analysis = f"""
Financial Analysis 
-------------------
Total Months: {number_of_months}
Total: ${total_profit_loss}
Average Change: ${current_average}
Greatest Increase in Profits: {max_increase_date} (${max_increase})
Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})
""" 
            print(analysis)
            new_text.write(analysis)

main()
