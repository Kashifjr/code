##this is a demo of various searching alorithms

#-----linear search-----
# big O notation: O(N)
# the pointer will iterate each element in the list. if the 
# has not been found, verialbe found will remain False. if 
# found, it will change to True
demoList = ["apple", "banana", "orange", "cherry", "peach"]

searching = "kiwi"

found = False
for x in demoList:
    if searching == x:
        found = True

#print("The element has been FOUUND: "+ str(found))


#-----binary search-----
# big O notation: O(logN)
# designed for sorted data structures, it will split the
# searchable data to reduce time without searching in 
# parts where the is not residing in.

found = False
sortedList = [1,45,67,34,8,7,25,79,83,2,5]
print(sortedList.sort())

# searching for digit key
key = 0
l = 0
r = len(sortedList)-1

while l <= r:
    m = l + (r - 1) // 2
    if key == sortedList[m]:
        found = True
    elif key > sortedList[m]:
        l = m + 1
    else:
        r = m - 1

#print(found)