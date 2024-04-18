from Car import Car

# garage path: /home/shika/code/python/Garage/garages

userInput = "" 
fileName = "empty"# current garage file
filePath = "/home/shika/code/python/Garage/garages/"
currentGarage = []# local instance of garage

testCar = Car(1970, "Chevy", "Chevelle")
currentGarage.append(testCar)

# creates menu with options text 
def genMenu():
    menuLine = "-------Garage Simulator-------"
    line1 = "------------------------"
    line2 = "========================"
    print(menuLine+"\nCurrent Garage: "+fileName+"\n"+line1+"""
Add car...........1
Remove Car........2
View Garage.......3
New Garage........4
Load Garage.......5
Save Garage.......6
"""+line2)


def carParse(read):
    car = read.split()
    car = Car(car[0], car[1], car[2])
    return car

#TODO: try/catch type for model and car, set bounds for cars to not
# exceed current year, other custom exceptions, create fileHandler .py files to 
# clean up code and hanle all file funcions oustide of this main file.

while True:
    genMenu()
    userInput = input("Choose and option: ")
    print()# new line for space
    if userInput == "1":# add car
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
        #print(car," has been created!\n")

    elif userInput == "2":# remove car
         pass
    
    elif userInput == "3":# view garage
        c = 1 #counts how many cars in garage
        if len(currentGarage) == 0:
            print("The current garage is empty!")
        else:
            for x in currentGarage:
                print(str(c)+"......",x)
                c+=1
            print()

    elif userInput == "5":# load garage
        fileInput = input("enter garage file name: ")
        if ".txt" not in fileInput:
            fileInput = fileInput + ".txt"

        # HERE, call the custom fileHandler and pass the file name with
        # load method

        file = filePath + fileInput
        print(file)
        f = open(file, "r")

        #print(f.readlines())
        currentGarage.clear()
        for x in f:
            tempCar = carParse(x)
            currentGarage.append(tempCar)

        f.close()
        fileName = fileInput

    elif userInput == "q" or userInput == "quit":# break progam
        print("closing program...")
        break