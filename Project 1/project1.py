import random

class door:
    doorID = 0
    hasGoat = False
    car = False
    isOpen = False

numDoors = int(input("How many doors: "))
doorMatrix = []

# Creates n-amount of doors
for row in range(1, numDoors + 1):
    dummyDoor = door()
    dummyDoor.doorID = row
    dummyDoor.goat = True
    doorMatrix.append(dummyDoor)

# Places Car randomly
getDoor = random.choice(doorMatrix)
getDoor.goat = False
getDoor.car = True

def userChoosen(numDoors):
    cDoor = int(input(f"Choose a door number from 1 - {numDoors}: "))
    return cDoor

# Function for filter in hostChooses Function
def excludeUserDoor(userDoorVal):
    def filter_function(val):
        return val != userDoorVal
    return filter_function

def hostChooses(numDoors, doorMatrix, userDoor):
    chosen = False
    iterator = 0

    # Host knows everything, therefore check what the user
    # has behind their door.
    isCarChosen = False
    if userDoor.car == True:
        isCarChosen = True

    # New list created with user's door removed
    filteredDoors = list(filter(excludeUserDoor(userDoor.doorID), doorMatrix))

    # If the car door was chosen by the user
    if isCarChosen:
        # Choose a door from the filtered doors
        generatedDoor = random.choice(filteredDoors)
    else:
        # If car door was not chosen, find it and choose it
        i = 0
        while i < len(filteredDoors) and not isCarChosen:
            if filteredDoors[i].car == True:
                generatedDoor = filteredDoors[i]
            i += 1

    return generatedDoor

def montyHall(numDoors, m):
    # Gets the User's chosen door
    userDoor_value = userChoosen(numDoors)
    userDoor = m[userDoor_value - 1]

    # Gets the game host's chosen door
    hostDoor = hostChooses(numDoors, doorMatrix, userDoor)

    counter = 0
    # Swap to other door
    # STILL IN THE WORKS
    for i in range(numDoors + 1):

        hostDoor = hostChooses(numDoors, doorMatrix, userDoor)
        if hostDoor.car == True:
            counter += 1

    print(counter)

montyHall(numDoors, doorMatrix)