import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

# imports pandas and matplotlib modules

def Googler(date):
    return (str(date) + " fire Louisville Kentucky")

def visualizer(x, y):
    plt.plot(x, y, marker = "^")
    plt.show()

# Google Search concatenator that creates efficient Google search to learn more about a specific incident through local media

def main():
    dataframe = pd.read_csv("Louisville_Metro_KY_-_Civilian_Fire_Injuries.csv")
    Injury_Date = pd.to_datetime(dataframe["Injury_Date"], errors = "coerce")
    Total_Injuries = dataframe["Total_Injuries"]

    visualizer(Injury_Date, Total_Injuries)

    count = 0
    for line in Total_Injuries:
        if Total_Injuries[count] > 1:
            search = Googler(Injury_Date[count])
            print(search)
    count += 1

main()