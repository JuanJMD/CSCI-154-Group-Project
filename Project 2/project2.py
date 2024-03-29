# OBJECTIVES
# 1. Get growth rate
# Get max capacity 

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

def rateCalc(lst):
    storage = []
    for i in range(len(lst) - 1):
        diff = (lst[i + 1] / lst[i]) - 1
        storage.append(diff)

    summation = 0
    for i in storage:
        summation += i
    
    rateValue = summation/len(storage)

    return rateValue

# logistic function has DUMMY values, not actual values
def logistic(rate):
    l = 2000000
    k = rate
    x = 0
    x0 = 0
    initPop = 789405
    inclPopulation = (l - initPop) / initPop
    
    container = []
    xRange = np.arange(-500, 501, 1)


    for i in xRange:
        res = l/(1 + ((inclPopulation) * (math.e)**(-k * (i - x0))))
        container.append(res)
        print(i, res)
    return [container, xRange]

### MAIN ###
        
# Reads Data in
birthData = pd.read_csv('data/modified/Births.csv')
deathData = pd.read_csv('data/modified/Deaths.csv')

# Extracts it into lists
[year, bCount, dCount] = [birthData['Year'].tolist(), birthData['Count'].tolist(), deathData['Count'].tolist()]

print(len(bCount))

# Calculates birth & death rate
birthRate = rateCalc(bCount)
deathRate = rateCalc(dCount)

print(f"The birth Rate: {birthRate}")
print(f"The death Rate: {deathRate}")

[dataRes, xDeathRange] = logistic(deathRate)

plt.plot(xDeathRange, dataRes)
plt.yticks(np.arange(1, 2000001, step=500000))
plt.show()