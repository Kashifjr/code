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
characters = list(string.ascii_letters)
digits = list(string.digits)
specialChar = list(string.punctuation)

password = ""

print("||||||Password Generator||||||")
length = input("How many characters would you like the password to have?: ")
length = int(length)

#characters
for x in range(length - 3):
    randNum = random.randint(0, 51)
    getChar = characters[randNum]
    password = password + (getChar)

#special characters
for x in range(2):
    randNum = random.randint(0, 31)
    getSpec = specialChar[randNum]
    password = password + (getSpec)

#digits
randNum = random.randint(0, 9)
getDig = digits[randNum]
password = password + (getDig)


#random.shuffle(password)



print("Generated: "+password+"\n")