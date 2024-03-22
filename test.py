import random


class door:
    doorID = 0
    goat = False
    car = False
    isOpen = False

doorMatrix = []

for row in range(10):
    for d in range(3):
        dummyDoor = door()
        dummyDoor.doorID = random.randint(1,3)
        doorMatrix.append(dummyDoor)



for i in doorMatrix:
    print(i.doorID)