# Begin by importing pandas and matplotlib modules for Dataframe calculations and visualization

import pandas as pd
import matplotlib.pyplot as plt

# Using formatted date, concatenates Google search for news article

def googler(date):
    return (str(date) + " fire Louisville Kentucky")

# Visualizer plotting injury count over injury dates, setting up labels, creating two
# visualizations as required (4)

def visualizer(x, y):
    plt.plot(x, y, marker = "^", linestyle = "None")
    plt.xlabel("Date of Incident")
    plt.ylabel("Fire Injuries per Incident")
    plt.title("Documented Fire Incidents in Louisville, Kentucky from 2005 to 2016")
    plt.grid(True)
    plt.show()

    plt.hist(y)
    plt.xlabel("Amount of Fire Injuries per Incident")
    plt.ylabel("Number of Incidents")
    plt.title("Documented Fire Incidents in Louisville, Kentucky from 2005 to 2016")
    plt.show()

# Reads in CSV (1), converts injuryDate to datetime (2), concatenates dates for Google searches
# into written text file, only selecting incidents involving more than one fire injury (3), then
# calls visualizer

def main():
    df = pd.read_csv("assets/fireInjuries.csv")
    injuryDate = pd.to_datetime(df["Injury_Date"], errors = "coerce")
    totalInjuries = df["Total_Injuries"]

    searches = open("googleSearches.txt", "w")
    count = 0
    for line in injuryDate:
        if df["Total_Injuries"][count] > 1:
            searches.writelines(googler(line.strftime("%Y-%m-%d")))
        count += 1
    searches.close()

    visualizer(injuryDate, totalInjuries)

# Calls the main program into existence

main()

# The visualizations offer a touch of insight into the 300 datapoints at hand. The bulk of the
# incidents were solo affairs. Fire spreads, but thankfully, the likelihood of fire injury does
# not. 

# Despite my initial presumptions about high incidents in July - as the first full month of summer,
# with weeks of fireworks surrounding - the data did not reflect that.

# What was revealed was a sobering reality: a cold, dangerous winter. Another interesting datapoint
# came from the absence of one: specifically, there was no data point for an incident involving two
# or more fire injuries in the month of March. This interpretation of results concludes my project
# (5). Thank you for your time.