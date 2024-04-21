from Room import Room

# ----ROOMS LAYOUT-----
#   C0   -  C1   -  C2
#   |               |
#   B0      B1   -  B2
#                   |
#   A0   -  A1   -  A2
#           |
#         cell
# ---------------------
# Play: the player must find the key AND weapon to defeat the 
# main boss and escape the dungeon. monsters can only be defeated
# if player has enough health and has the weapon. ** monsters
# have a chance to be asleep and player can insta kill or sneak
# past without having to kill them. some rooms have secret rooms*
# or options to find hidden items. i.e. false walls, ojects hiding
# collectables and health*. 
#
# should make Room class? or contiue as is?



inventory = []# global player inventory

def noWhere():# nowhre to go func.
    print("There is no where to go or nothing to do.")

def introScene():# title card
    print("""
=============================================
        Welcome to Kat's Dungeon!
---------------------------------------------
In order leave, you'll need to locate the key
and find the final room! But be careful, as
there are monsters whom haven't been fed in 
centuries! Good luck...
=============================================
""")

def dungeonCell(directions):
    print("Filthy cell you are held captive in.")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            noWhere()
        elif userInput == "right":
            noWhere()
        elif userInput == "back":
            noWhere()
        elif userInput == "forward":
            roomA1(directions)

# hidden sword when performing action at south
def roomA0(directions):
    print("""roomA0
tiny supply closet with a metal bucket and
small stack of papers on a shelf 
above your head.""")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            noWhere()
        elif userInput == "right":
            roomA1(directions)
        elif userInput == "back":
            noWhere()
        elif userInput == "forward":
            noWhere()

def roomA1(directions):
    print("roomA1")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            roomA0(directions)
        elif userInput == "right":
            roomA2(directions)
        elif userInput == "back":
            dungeonCell(directions)
        elif userInput == "forward":
            noWhere()

def roomA2(directions):
    print("roomA2")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            roomA1(directions)
        elif userInput == "right":
            noWhere()
        elif userInput == "back":
            noWhere()
        elif userInput == "forward":
            roomB2(directions)

# final boss key located in this room.
def roomB0(directions):
    print("roomB0")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            noWhere()
        elif userInput == "right":
            noWhere()
        elif userInput == "back":
            noWhere()
        elif userInput == "forward":
            roomC0(directions)

# final boss and escape room.roomA0
def roomB1(directions):
    print("roomB1")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            noWhere()
        elif userInput == "right":
            roomB2(directions)
        elif userInput == "back":
            noWhere()
        elif userInput == "forward":
            noWhere()

# player must have weapon to defeat enemy.
def roomB2(directions):
    print("roomB2")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            roomB1(directions)
        elif userInput == "right":
            noWhere()
        elif userInput == "back":
            roomA2(directions)
        elif userInput == "forward":
            roomC2(directions)

# player must have enemy AND plus 1 health to defeat enemy
def roomC0(directions):
    print("roomC0")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            noWhere()
        elif userInput == "right":
            roomC1(directions)
        elif userInput == "back":
            roomB0(directions)
        elif userInput == "forward":
            noWhere()

def roomC1(directions):
    print("roomC1")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            roomC0(directions)
        elif userInput == "right":
            roomC2(directions)
        elif userInput == "back":
            noWhere()
        elif userInput == "forward":
            noWhere()

def roomC2(directions):
    print("roomC2")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!")
        elif userInput == "left":
            roomC1(directions)
        elif userInput == "right":
            noWhere()
        elif userInput == "back":
            roomB2(directions)
        elif userInput == "forward":
            noWhere()

    

# main function
def main():
    directions = ["left", "right", "forward", "back"]
    introScene()

    dungeonCell(directions)


    return 1

main()