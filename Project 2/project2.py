# OBJECTIVES
# 1. Get growth rate
# Get max capacity 

import pandas as pd
import math

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
    l = 5000
    k = rate
    x = 0
    x0 = 0
    equation = l/(1 + (math.e)**(-k * (x - x0)))

    for i in range(60):
        res = l/(1 + (math.e)**(-k * (i - x0)))
        print(res)

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

logistic(birthRate)