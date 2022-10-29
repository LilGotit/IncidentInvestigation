import csv
import datetime
from time import strftime

# imports CSV and datetime modules

def concatenator(date):
    return (str(date) + " fire Louisville Kentucky")

# Google Search concatenator that creates efficient Google search to learn more about a specific incident through local media

def main():
    f = open("Louisville_Metro_KY_-_Civilian_Fire_Injuries.csv", "r")
    count = 0

    # main function begins by opening CSV file

    next(f)

    # the CSV header information is discarded
    
    for line in f:
        id, injuryDate, totalInjuries, objectid = line.split(",")
        totalInjuries = int(totalInjuries)

        # if condition goes here

        if totalInjuries > 1:
            search = concatenator(injuryDate)
            print(id, injuryDate, totalInjuries, objectid)
            print(search)
            count += 1

    print(count)
    
    f.close()

main()