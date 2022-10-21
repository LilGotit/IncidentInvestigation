def concatenator(d):
    return (str(d) + "fire in Louisville")

def main():
    f = open("Louisville_Metro_KY_-_Civilian_Fire_Injuries.txt", "r")

    for line in f:
        ID, injuryDate, totalInjuries, OBJECTID = line.split(",")
        
        search = concatenator(injuryDate)
        
# if condition goes here

        print(ID, injuryDate, totalInjuries)
        print(search)
    
    f.close()

main()