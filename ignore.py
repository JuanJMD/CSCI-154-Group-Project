def excludeUserDoor(userDoorVal):
    def filter_function(val):
        return val != userDoorVal
    return filter_function

d = filter(excludeUserDoor(3), range(1, 11))

for n in d:
    print(n)
