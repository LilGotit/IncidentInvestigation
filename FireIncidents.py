import pandas as pd
import matplotlib.pyplot as plt

# imports pandas and matplotlib modules

def Googler(date):
    return (str(date) + " fire Louisville Kentucky\n")

def visualizer(x, y):
    plt.plot(x, y, marker = "^")
    plt.show()

# Google Search concatenator that creates efficient Google search to learn more about a specific incident through local media

def main():
    df = pd.read_csv("assets/fireInjuries.csv")
    Injury_Date = pd.to_datetime(df["Injury_Date"], errors = "coerce")
    Total_Injuries = df["Total_Injuries"]

    w = open("GoogleSearches.txt", "w")
    count = 0
    for line in Injury_Date:
        if df["Total_Injuries"][count] > 1:
            print(Googler(line.strftime("%Y-%m-%d")))
            w.writelines(Googler(line.strftime("%Y-%m-%d")))
        count += 1
    w.close()

    visualizer(Injury_Date, Total_Injuries)

main()