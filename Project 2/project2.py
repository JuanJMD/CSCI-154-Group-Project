# OBJECTIVES
# 1. Get growth rate
# Get max capacity 

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

def getRate(num, population):
    rates = []
    for i in range(len(num)):
        getBirth = num[i]
        getPopSize = population[i]

        print(f"{getBirth}/{getPopSize}")

        rates.append(getBirth/getPopSize)

    averageRate = sum(rates)/len(num)

    print("== == ==")

    return averageRate



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
    initPop = 1015190
    inclPopulation = (l - initPop) / initPop
    
    container = []
    xRange = np.arange(-500, 501, 1)


    for i in xRange:
        res = l/(1 + ((inclPopulation) * (math.e)**(-k * (i - x0))))
        container.append(res)
    return [container, xRange]

### MAIN ###
        
# Reads Data in
birthData = pd.read_csv('data/modified/Births.csv')
deathData = pd.read_csv('data/modified/Deaths.csv')

df = pd.read_csv('data/modified/Fresno County Annual Population data.csv', parse_dates=['DATE'])

# Extracts it into lists
[year, bCount, dCount] = [birthData['Year'].tolist(), birthData['Count'].tolist(), deathData['Count'].tolist()]

popData = df[df['DATE'].dt.year > 1998]

[populationDates, populationNums] = [popData['DATE'].tolist(), popData['CAFRES9POP'].tolist()]
popValues = [int(str(num).replace('.', '')) for num in populationNums]


birthRate = getRate(bCount, popValues)
deathRate = getRate(dCount, popValues)
# Calculates birth & death rate
#birthRate = rateCalc(bCount)
#deathRate = rateCalc(dCount)

print(f"The birth Rate: {birthRate}")
print(f"The death Rate: {deathRate}")

rateVal = birthRate - deathRate

print(f"RATE VAL = {rateVal}")


[dataResults, xRange] = logistic(rateVal)

plt.plot(xRange, dataResults)
plt.yticks(np.arange(1, 2000001, step=500000))
plt.show()

# Death Graph
#[death_data_results, xDeathRange] = logistic(deathRate)

#plt.plot(xDeathRange, death_data_results)
#plt.yticks(np.arange(1, 2000001, step=500000))
#plt.show()

# Birth Graph
#[birth_data_results, xBirthRange] = logistic(birthRate)

#plt.plot(xBirthRange, birth_data_results)
#plt.yticks(np.arange(1, 2000001, step=500000))
#plt.show()