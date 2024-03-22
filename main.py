import random


class door:
    doorID = 0
    goat = False
    car = False
    isOpen = False
    isHostChosen = False


numDoors = int(input("How many doors:"))

doorMatrix = []

for row in range(1, 101):
    dummyDoor = door()
    dummyDoor.doorID = row
    doorMatrix.append(dummyDoor)


def hostChooses(numDoors):
    hostChosenDoor = random.randint(1, numDoors)
    return hostChosenDoor
def montyHall(numDoors, m):
    hChosen = hostChooses(numDoors)

    # 


    m[hChosen].isHostChosen = True








for i in doorMatrix:
    print(i.doorID)