# import csv module
import csv

# Google Search concatenator that creates efficient Google search to learn more about a specific incident through local media

def concatenator(d):
    return (str(d) + "fire in Louisville")

# the main function which opens the CSV file, unpacks each line into a variable

def main():
    f = open("Louisville_Metro_KY_-_Civilian_Fire_Injuries.csv", "r")

    for line in f:
        id, injuryDate, totalInjuries, objectid = line.split(",")
        
        search = concatenator(injuryDate)
        
# if condition goes here

        print(id, injuryDate, totalInjuries)
        print(search)
    
    f.close()

main()