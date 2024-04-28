


def start():
    return roomA1()

def roomA1():
    print("ROOM A1\n")
    player = input()

    if player == "go":
        return "A2"

def roomA2():
    print("ROOM A2\n")
    player = input()

    if player == "go":
        return "A1"


def main():
    room = start()
    while True:
        if room == "A1":
            room = roomA1()
        elif room == "A2":
            room = roomA2()

main()