from Car import Car

# garage path: /home/shika/code/python/Garage/garages

userInput = "" 
file = "empty"# current garage file
currentGarage = []# local instance of garage

testCar = Car(1970, "Chevy", "Chevelle")
currentGarage.append(testCar)

def genMenu():
    menuLine = "-------Garage Simulator-------"
    line1 = "------------------------"
    line2 = "========================"
    print(menuLine+"\nCurrent Garage: "+file+"\n"+line1+"""
Add car...........1
Remove Car........2
View Garage.......3
New Garage........4
Load Garage.......5
Save Garage.......6
"""+line2)

#TODO: try/catch type for model and car, set bounds for cars to not
# exceed current year, other custom exceptions

while True:
    genMenu()
    userInput = input("Choose and option: ")
    print()# new line for space
    if userInput == "1":
        carInput = input("Enter year, make and model of new car: ")
        carInput = carInput.split() #converts string into an array
        if len(carInput) < 3 or len(carInput) > 3:
            print("input is too short or too long, try again!")
            break # make custom exception to throw
        try:
            int(carInput[0])
        except ValueError as e:
            print(str(e) +" is not an integer!")
        
        car = Car(carInput[0], carInput[1].capitalize(), carInput[2].capitalize())
        print(car," has been created!\n")

        currentGarage.append(car)
    if userInput == "3":
        c = 1
        for x in currentGarage:
            print(str(c)+"......",x)
            c+=1
        print()
    # break loop to close program
    elif userInput == "q" or userInput == "quit":
        print("closing program...")
        break