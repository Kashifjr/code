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
# check inventory at any moment? current implementations calls
# redoing much of the "directions" implemention each func. has as
# an attribute..

inventory = []# global player inventory
cell_Locked = True

def noWhere():# nowhre to go func.
    print("There is no where to go or nothing to do.")

def showInventory():
    print(inventory)

def introScene():# title card
    print("""
=============================================
        Welcome to Kat's Dungeon!
---------------------------------------------
In order leave, you'll need to locate the key
and find the final room! But be careful, as
there are monsters whom haven't been fed in 
centuries! Good luck...
---------------------------------------------
You have four movement options:
    (forward | backward | left | right)
Typing 'inv' or 'inventory' shows all items
you currently have.
Try "interacting" with items you see in the 
room...
=============================================
""")

def dungeonCell(directions):
    print("""Filthy cell you are held captive in. A dirty 
mattress is on the floor,a bucket filled with something 
horrendous and smells the same. The bars to yourcell are 
strong and impassable.""")
    cell_Locked = True
    if "nail" in inventory:
        cell_Locked = False

    while True:
        userInput = input("Type an action: ")
        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return
        if cell_Locked == True:
            if (userInput == "forward" or "door" in userInput) and "nail" not in inventory:
               print("""You cannot get passed the locked cell door. But it seems you may be
able to unlock the cell if you can find something small enought to jiggle the keyhole with...""")
            elif userInput == "forward" or "door" in userInput and "nail" in inventory:
                print("""You play the nail around in the cell keyhole until you hear a loud *clank*.
Cell door swings open and you can now explore the dungeon!""")
                cell_Locked = False
                return roomA1(directions)
            elif "bucket" in userInput and "nail" not in inventory:
                print("""Defying every fiber in your being, you pludge your hand int the bucket. Fishing
around in the cold muck, you find a long rusty nail.""")
                inventory.append("nail")

        elif cell_Locked == False:
            if userInput not in directions:
                print("invalid action, try again!")
            elif userInput == "left":
                noWhere()
            elif userInput == "right":
                noWhere()
            elif userInput == "back":
                noWhere()
            elif userInput == "forward":
                return roomA1(directions)

# hidden sword when performing action at south
def roomA0(directions):
    
    print("""roomA0
tiny supply closet with a metal bucket and
small stack of papers on a shelf 
above your head.""")
    while True:
        userInput = input("Type an action: ")
        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return
        
        if "papers" in userInput and "sword" not in inventory:
            print("""Your curiousity has led you to find a switch hidden behind
the papers! A small trap door reveals a magic sword you can now
use to defend yourself!""")
            inventory.append("sword")# the sword has been found and added to inventory!
            continue
        elif "papers" in userInput and "sword" in inventory:
            print("""There is nothing else notable about the stack of papers.""")
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

        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return

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

        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return
    
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
    print("""This is a very large room. There is a desk with various papers. The right 
wall has a shelf that has a few ruined books. One of them looks odd. There is a chest
at the left side of the room. In front of you, there is the door you entered. The back
of the room has a small bed with no pillow or blankets.""")
    while True:
        userInput = input("Type an action: ")

        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return

        if "book" in userInput or "shelf" in userInput and "key" not in inventory:
            print("""Looking at the books more closely, you find that the most of them are
badly burned and usless. But the last one is in good condition and has a key hidden between
the pages! You now have the Boss Room key!""")
            inventory.append("key")
        
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
    if "armor" not in inventory:
        print("""You've made it to the boss room! There is a great foe that towers over
you with blood lust in its eyes! You try your best to defeat the monster but you can't
withstand the single blow it manages to deal to you. Your fragile body explodes with 
the emense force and your great escape ends rather brutally. Game Over...""")
    elif "armor" in inventory:
        print("""You've made it to the boss room! There is a great foe that towers over
you with blood lust in its eyes! Your battle is fierce and long but with the masterly 
forged sword and beautifully crafted set of armor, you are able to trade blows with the
beast until you land the final and fatal strike! The beast has been defeated!""")
        print("""You pass the corpse of the beast and make your way to the ouside world,
reclaiming your freedom!\nYou Win!!!""")
        return
    while True:
        userInput = input("Type an action: ")

        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return

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
    monster_Dead = False

    while True:
        if monster_Dead == False:
            print("""There is a muscular monster that stands before you. You may have
a chance to flee if you think fast or you can take you chances and challenge the beast.""")
            userInput = input("Fight or flee?: ")
            if userInput == "fight" and "sword" in inventory:
                print("""With sword in hand, you and the monster duke it out breifly. The monster
is very powerful but slow. You manage to slip the cold steel between its ribs with
quick joust! The beast falls as all life escapse its body.""")
                monster_Dead = True
            elif userInput == "flee":
                roomA2(directions)

        elif monster_Dead == True:
            print("""The mangled corpse of the monster lies on the floor. You really did 
did a number on this one...""")
            userInput = input("Type an action: ")
            if userInput not in directions:
                print("invalid action, try again!")
            elif userInput == "left":
                if "key" in inventory:
                    roomB1(directions)
                else: 
                    print("""You have found the boos room! But you don't 
    possess the key to enter! You must continue searching
    in order to escape!""")
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

        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return

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

    print("\nThanks for playing!!!")


    return 1

main()