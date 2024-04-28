from Room import Room

# ----ROOMS LAYOUT-----
#   C0   -  C1   -  C2
#                   |
#           B1   -  B2
#                   |
#   A0   -  A1   -  A2
#           |
#         cell
# ---------------------
# Play: the player must find the key, a weapon and Amor to defeat
# the main boss and escape the dungeon. monsters can only be defeated
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
# is there a way to return a functino with a function? i desire to 
# always return to the main func to immediately go to the room
# func that the previous one returned...

inventory = []# player inventory
cell_Locked = True
line = "------------------------------------------------"

def nothing():# nowhre to go func.
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

# start of game room.
def dungeonCell(directions):
    print(line)
    print("""Filthy cell you are held captive in. A dirty 
mattress is on the floor,a bucket filled with something 
horrendous and smells the same. The bars to yourcell are 
strong and impassable.""")
    print(line+"\n")
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
               print(line)
               print("""You cannot get passed the locked cell door. But it seems you may be
able to unlock the cell if you can find something small enought to jiggle the keyhole with...""")
               print(line+"\n")
            elif userInput == "forward" or "door" in userInput and "nail" in inventory:
                print(line)
                print("""You play the nail around in the cell keyhole until you hear a loud *clank*.
Cell door swings open and you can now explore the dungeon!""")
                print(line+"\n")
                cell_Locked = False
                return roomA1(directions)
            elif "bucket" in userInput and "nail" not in inventory:
                print(line)
                print("""Defying every fiber in your being, you pludge your hand int the bucket. Fishing
around in the cold muck, you find a long rusty nail.""")
                print(line+"\n")
                inventory.append("nail")

        elif cell_Locked == False:
            if userInput not in directions:
                print("\ninvalid action, try again!\n")
            elif userInput == "left":
                nothing()
            elif userInput == "right":
                nothing()
            elif userInput == "back":
                nothing()
            elif userInput == "forward":
                return roomA1(directions)

# hidden sword when mentioning anything about the papers
def roomA0(directions):
    print(line)
    print("""A tiny supply closet with a metal bucket and
small stack of papers on a shelf 
above your head.""")
    print(line+"\n")
    while True:
        userInput = input("Type an action: ")
        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return
        
        if "papers" in userInput and "sword" not in inventory:
            print(line)
            print("""Your curiousity has led you to find a switch hidden behind
the papers! A small trap door reveals a magic sword you can now
use to defend yourself!\nObtained: Sword""")
            print(line+"\n")
            inventory.append("sword")# the sword has been found and added to inventory!
            continue
        elif "papers" in userInput and "sword" in inventory:
            print(line)
            print("""There is nothing else notable about the stack of papers.""")
            print(line+"\n")
        if userInput not in directions:
            print("\ninvalid action, try again!\n")
        elif userInput == "left":
            nothing()
        elif userInput == "right":
            return roomA1(directions)
        elif userInput == "back":
            nothing()
        elif userInput == "forward":
            nothing()

def roomA1(directions):
    print(line)
    print("""\nA small corridor. There is a small closet to your LEFT and 
a door to your RIGHT.""")
    print(line+"\n")
    while True:
        userInput = input("Type an action: ")
        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            quit()

        if userInput not in directions:
            print("invalid action, try again!\n")
        elif userInput == "left":
            return roomA0(directions)
        elif userInput == "right":
            return roomA2(directions)
        elif userInput == "back":
            return dungeonCell(directions)
        elif userInput == "forward":
            nothing()

def roomA2(directions):
    print(line)
    print("""A small corridor connecting two rooms. You can 
go FORWARD or LEFT.""")
    print(line+"\n")
    while True:
        userInput = input("Type an action: ")

        if userInput == "inventory":
            showInventory()
        elif userInput == "q" or userInput == "quit":
            return
    
        if userInput not in directions:
            print("\ninvalid action, try again!\n")
        elif userInput == "left":
            return roomA1(directions)
        elif userInput == "right":
            nothing()
        elif userInput == "back":
            nothing()
        elif userInput == "forward":
            return roomB2(directions)

# final boss and escape room.
def roomB1(directions):
    if "armor" not in inventory:
        print(line)
        print("""You've made it to the boss room! There is a great foe that towers over
you with blood lust in its eyes! You try your best to defeat the monster but you can't
withstand the single blow it manages to deal to you. Your fragile body explodes with 
the emense force and your great escape ends rather brutally. Game Over...""")
        print(line+"\n")
        quit()
    elif "armor" in inventory:
        print(line)
        print("""You've made it to the boss room! There is a great foe that towers over
you with blood lust in its eyes! Your battle is fierce and long but with the masterly 
forged sword and beautifully crafted set of armor, you are able to trade blows with the
beast until you land the final and fatal strike! The beast has been defeated!""")
        print("""You pass the corpse of the beast and make your way to the ouside world,
reclaiming your freedom!\nYou Win!!!""")
        print(line+"\n")
        quit()# close prpgram...
    
# player must have weapon to defeat enemy.
def roomB2(directions):
    monster_Dead = False
    if "monster1" in inventory:
        monster_Dead = True

    while True:
        if monster_Dead == False:
            print(line)
            print("""There is a muscular monster that stands before you. You may have
a chance to flee if you think fast or you can take you chances and challenge the beast.\n""")
            print(line+"\n")
            userInput = input("Fight or flee?: ")
            if userInput == "fight":
                if "sword" in inventory:
                    print(line)
                    print("""With sword in hand, you and the monster duke it out breifly. The monster
    is very powerful but slow. You manage to slip the cold steel between its ribs with
    quick joust! The beast falls as all life escapse its body.""")
                    print(line+"\n")
                    monster_Dead = True
                    # banndaid to add monster to inventory to make sure it is still dead when reloading room
                    inventory.append("monster1")
                else:
                    print(line)
                    print("""You have faith in your two fists and try to vanquish the monster. 
The monster let's out a demeaning grunt and promptly squashes your delicate human body
into a bloody mush of gore and bone.\nYou Died. Game Over.""")
                    print(line+"\n")
                    quit()
            elif userInput == "flee":
                roomA2(directions)
        elif monster_Dead == True:
            print(line)
            print("""The mangled corpse of the monster lies on the floor. You really did 
did a number on this one...""")
            print(line+"\n")
            userInput = input("Type an action: ")
            if userInput not in directions:
                print("\ninvalid action, try again!\n")
            elif userInput == "left":
                if "key" in inventory:
                    roomB1(directions)
                else: 
                    print(line)
                    print("""You have found the boos room! But you don't 
    possess the key to enter! You must continue searching
    in order to escape!""")
                    print(line)
            elif userInput == "right":
                nothing()
            elif userInput == "back":
                return roomA2(directions)
            elif userInput == "forward":
                return roomC2(directions)

# final boss key located in this room.
def roomC0(directions):
    print(line)
    print("""This is a very large room. There is a desk with various papers. The right 
wall has a shelf that has a few ruined books. One of them looks odd. There is a chest
at the left side of the room. In front of you, there is the door you entered. The back
of the room has a small bed with no pillow or blankets.""")
    print(line+"\n")
    while True:
        userInput = input("Type an action: ")
        if "book" in userInput or "shelf" in userInput and "key" not in inventory:
            print(line)
            print("""Looking at the books more closely, you find that the most of them are
badly burned and usless. But the last one is in good condition and has a key hidden between
the pages! You now have the Boss Room key!""")
            print(line+"\n")
            inventory.append("key")
        
        if userInput not in directions:
            print("invalid action, try again!\n")
        elif userInput == "left":
            nothing()
        elif userInput == "right":
            return roomC1(directions)
        elif userInput == "back":
            nothing()
        elif userInput == "forward":
            nothing()

# armor is located in ths room.
def roomC1(directions):
    print(line)
    print("""This room doen't seem to have much of importance in here. There is
a large rug in the middle of room, and along both sides of the walls,
there are armor stands but none of them are showcasing any armor.""")
    print(line+"\n")
    while True:
        userInput = input("Type an action: ")
        if "rug" in userInput and "armor" not in inventory:
            print(line)
            print("""The rug is large and heavy. But you find that there is a hidden
door underneath it! You upen the dusty door and find a crumpled set of rusty armor!
This will hopefully allow you to defeat stronger enemies!""")
            print(line+"\n")
            inventory.append("armor")
        elif userInput not in directions:
            print("invalid action, try again!\n")
        elif userInput == "left":
            return roomC0(directions)
        elif userInput == "right":
            return roomC2(directions)
        elif userInput == "back":
            nothing()
        elif userInput == "forward":
            nothing()

def roomC2(directions):
    print(line)
    print("""A small corridor connecting a room to your LEFT and a
room BEHIND you.""")
    print(line+"\n")
    while True:
        userInput = input("Type an action: ")
        if userInput not in directions:
            print("invalid action, try again!\n")
        elif userInput == "left":
            roomC1(directions)
        elif userInput == "right":
            nothing()
        elif userInput == "back":
            roomB2(directions)
        elif userInput == "forward":
            nothing()

# main function
def main():
    directions = ["left", "right", "forward", "back"]
    introScene()
    dungeonCell(directions)

    print("\nThanks for playing!!!")


    return 1

main()