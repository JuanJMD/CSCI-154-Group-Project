import secrets

class door:
    doorID = 0
    hasGoat = False
    car = False
    
#empty door array
doorMatrix = []

# Creates n-amount of doors
def doorCreation(numDoors):
    for row in range(1, numDoors + 1):
        dummyDoor = door()
        dummyDoor.doorID = row
        dummyDoor.hasGoat = True
        doorMatrix.append(dummyDoor)
    return doorMatrix

# Places Car randomly
def placeCar(doorMatrix):
    carDoor = secrets.choice(doorMatrix)
    carDoor.hasGoat = False
    carDoor.car = True
    return carDoor.doorID

def userFirstChoice(doorMatrix):
    #using random number to simulate user choice
    userDoor = secrets.choice(doorMatrix)
    return userDoor.doorID

#If user always switches the door, we only need to consider if user's first choice contains a car 
#If yes, switching always win
#Otherwise, switching always lose
def alwaysSwitch(userDoor,carDoor):
    if(userDoor == carDoor):
        return False
    else:
        return True

#If user always stays and the first choice contains a car, the user wins. Otherwise, the user loses
def alwaysStay(userDoor, carDoor):
    if(userDoor == carDoor):
        return True
    else:
        return False

def montyHall(numDoors, rule):
    if not numDoors:
        return
    
    #game initializaton
    doorMatrix=doorCreation(numDoors)

    #get the cardoor
    carDoor = placeCar(doorMatrix)

    # User's first choice
    userDoor = userFirstChoice(doorMatrix)

    #Update rule choices
    if rule==1:
        result = alwaysSwitch(userDoor,carDoor)
    else:
        result = alwaysStay(userDoor,carDoor)
    
    return result

numDoors = int(input("How many doors for the game: "))
times = int(input("Simulation times: "))

countWin1 = 0
countLose1 = 0
#Always Switching Case:
for x in range(times+1):
    if (montyHall(numDoors, 1)):
        countWin1 +=1
    else:
        countLose1 +=1

print("Win: ", countWin1)
print("Lose: ", countLose1)
print("Always Switching Win probability: ", countWin1/times)

#Always Staying Case:
countWin2 = 0
countLose2 = 0
for x in range(times+1):
    if (montyHall(numDoors,2)):
        countWin2 +=1
    else:
        countLose2 +=1

print("Win: ", countWin2)
print("Lose: ", countLose2)
print("Always Staying Win probability: ", countWin2/times)
