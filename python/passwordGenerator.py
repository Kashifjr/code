import random
import string

#Not a very strong password generator. creates list containing all letters, uppercase and
#lowercase, special characters and digits. 
#listCHar has 94 entires
#random.seed is needed to initialize the rand. num gen.

#TODO:
#strengthen randomness with shuffle, use methods, custom python classes, fix 25 length issue,
#add constraitns of at least 1 special, 1 number and at least 8 characters long, error parsing,
#try and catch

random.seed()
listChar = list(string.ascii_letters)
tempList = list(string.digits)
listChar.extend(tempList)
tempList = list(string.punctuation)
listChar.extend(tempList)

password = ""

print("||||||Password Generator||||||")
length = input("How many characters would you like the password to have?: ")
length = int(length)

for x in range(length):
    randNum = random.randint(0, 94)
    getChar = listChar[randNum]
    password = password + (getChar)
    


print("Generated: "+password+"\n")
