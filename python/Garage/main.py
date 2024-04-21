from Car import Car

# garage folder path: /home/shika/code/python/Garage/garages

userInput = "" 
fileName = "empty"# current garage file
filePath = "/home/shika/code/python/Garage/garages/"
currentGarage = []# local instance of garage

#testCar = Car(1970, "Chevy", "Chevelle")
#currentGarage.append(testCar)# test adding car to garage.

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

# parses string to create and return a Car object
def carParse(read):
    car = read.split()
    car = Car(car[0], car[1], car[2])
    return car

# save current garage to current .txt file
def saveGarage():
    if fileName == "empty":
        return
    print("saving current garage...")
    file = filePath + fileName
    f = open(file, "w")
    for x in currentGarage:
        f.write(str(x)+"\n")
    f.close()
    print("Garage "+fileName+" has been saved!")

#TODO: try/catch type for model and car, set bounds for cars to not
# exceed current year(maybe), other custom exceptions, *create fileHandler .py files to 
# clean up code and handle all file funcions oustide of this main file?
# perhaps better to create file handler/load/save methods only, not new .py file
# to handle files?
# add option to remove garage files and view all garage files in directory

while True:
    genMenu()
    userInput = input("Choose an option: ")
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
        currentGarage.append(car)
        print(car," has been created!\n")

    elif userInput == "2":# remove car
        c = 1
        for x in currentGarage:
            print(str(c)+"......",x)
            c+=1
            print()
        try:
            carID = int(input("enter car index to delete: "))
            carID += -1
            if carID >= len(currentGarage) or carID < 0:
                print("car ID is out of bounds")
            else:
                print(currentGarage[carID],"has been removed!")
                currentGarage.pop(carID)
            print()
        except ValueError as e:
            print("Only integers are accepted!")
  
    elif userInput == "3":# view garage
        c = 1 #counts how many cars in garage
        if len(currentGarage) == 0:
            print("The current garage is empty!\n")
        else:
            for x in currentGarage:
                print(str(c)+"......",x)
                c+=1
            print()

    elif userInput == "4":# new garage
        newFile = input("Enter garage name: ")
        if ".txt" not in newFile:
            newFile = newFile + ".txt"
        nF = filePath + newFile 
        try:
            f = open(nF, "x")
            print(str(newFile)+" garage has been created!\n")
            fileName = newFile
        except FileExistsError as err:
            print(fileName+" already exists!\n")

    elif userInput == "5":# load garage
        fileInput = input("enter garage file name: ")
        if ".txt" not in fileInput:
            fileInput = fileInput + ".txt"

        # HERE, call the custom fileHandler and pass the file name with
        # load method

        file = filePath + fileInput
        try:
            f = open(file, "r")
            currentGarage.clear()
            for x in f:
                tempCar = carParse(x)
                currentGarage.append(tempCar)
            f.close()
            fileName = fileInput      
        except FileNotFoundError as e:
            print(fileInput+" does not exist.")

    elif userInput == "6":# save garage
        if fileName == "empty":
            print("There is no open Garage file to save to!\n")
        else:
            saveGarage()

    elif userInput == "q" or userInput == "quit":# break progam
        print("closing program...")
        saveGarage()            
        break