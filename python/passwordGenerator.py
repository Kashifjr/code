import random
import string

#Not a very strong password generator. creates list containing all letters, uppercase and
#lowercase, special characters and digits. 
#random.seed is needed to initialize the rand. num gen.

#TODO:
#strengthen randomness with shuffle, use methods, custom python classes, fix 25 length issue,
#add constraitns of at least 1 special, 1 number and at least 8 characters long, error parsing,
#try and catch

random.seed()
characters = list(string.ascii_letters)
random.shuffle(characters)

digits = list(string.digits)
random.shuffle(digits)

specialChar = list(string.punctuation)
random.shuffle(specialChar)

password = ""

print("||||||Password Generator||||||")
while(True):

    print("Passwords must be at least 8 characters long and will contain 2\nspecial character and 1 digit.")
    length = input("How many characters would you like the password to have?: ")
    try:
        length = int(length)
        if(length<8):
            print("Sorry, no numbers less than 8. Try again!\n")
        else:
            break
    except ValueError:
        print("You must input a number!\n")
    


#characters 52 entries
for x in range(length - 3):
    randNum = random.randint(0, 51)
    getChar = characters[randNum]
    password = password + (getChar)

#special characters 32 entries
for x in range(2):
    randNum = random.randint(0, 31)
    getSpec = specialChar[randNum]
    password = password + (getSpec)

#digits 10 entries
randNum = random.randint(0, 9)
getDig = digits[randNum]
password = password + (getDig)

#converts password string(array) to list to shuffle
#then converts back to string(array)
p = list(password)
password = list(p)
random.shuffle(p)
result = ''.join(p)



print("Generated: "+result+"\n")