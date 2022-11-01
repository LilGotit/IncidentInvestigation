import pandas as pd
import matplotlib.pyplot as plt

# imports pandas and matplotlib modules

def Googler(date):
    return (str(date) + " fire Louisville Kentucky\n")

# concatenates Google search for news article, calculated from formatted date

def visualizer(x, y):
    plt.plot(x, y, marker = "^", linestyle = "None")
    plt.xlabel("Date of Incident")
    plt.ylabel("Fire Injuries per Incident")
    plt.title("Documented Fire Incidents in Louisville, Kentucky from 2005 to 2016")
    plt.grid(True)
    plt.show()

# visualizer setup; plot and label injury count versus injury dates

def main():
    df = pd.read_csv("assets/fireInjuries.csv")
    Injury_Date = pd.to_datetime(df["Injury_Date"], errors = "coerce")
    Total_Injuries = df["Total_Injuries"]

# read in CSV file, convert Injury_Date from object to datetime

    w = open("GoogleSearches.txt", "w")
    count = 0
    for line in Injury_Date:
        if df["Total_Injuries"][count] > 1:
            print(Googler(line.strftime("%Y-%m-%d")))
            w.writelines(Googler(line.strftime("%Y-%m-%d")))
        count += 1
    w.close()

# creates text file with concatenated dates for Google searches, only selects dates involving 2 or more injuries, creates visualization

    visualizer(Injury_Date, Total_Injuries)

main()