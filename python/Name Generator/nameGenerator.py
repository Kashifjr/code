import os
import string
import random

##TODO: need to buffer files to get rid of new line character \n
## as current printing/formating is odd.
##     need ot seperate into methods/functions and other .py
##     files ot keep all code clean.

random.seed()
s = ""
firstNames = []
lastNames = []
n = 100

file1 = open("/home/shika/code/python/Name Generator/firstNames.txt", "r")
file2 = open("/home/shika/code/python/Name Generator/lastNames.txt", "r")

#reads files and populate first/last name arrays
for x in file1:
    s = file1.readline()
    firstNames.append(s)
for x in file2:
    s = file2.readline()
    lastNames.append(s)
#    print(s)

file1.close()
file2.close()

#get length of first/last name arrays
fNameLen = len(firstNames) -1
lNameLen = len(lastNames) -1

ranNum0 = random.randint(0,fNameLen)
random.seed()
ranNum1 = random.randint(0,lNameLen)

print(str(ranNum0) +" "+ str(ranNum1))

for x in range(n): #shuffle arrays n times
    random.shuffle(firstNames)
    random.shuffle(lastNames)

name = firstNames[ranNum0].capitalize() + lastNames[ranNum1].capitalize()

print("Random generated name is: \n" + name)