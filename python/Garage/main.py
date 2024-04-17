from Car import Car

myCar = Car(1970, "Chevy", "Chevelle")

print(myCar.model)
print(myCar)
myCar.printCar()

player = ""

while player != "q":
    player = input("Choose and option: ")


    if player == "q":
        print("Closing program...")
        break
    else:
        carInput = input("Enter year, make and model: ")
        print(carInput)
    
   