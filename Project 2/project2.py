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

        rates.append(getBirth/getPopSize)

    averageRate = sum(rates)/len(num)
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
    L = 2000000
    k = rate
    x = 0
    x0 = 0
    initPop = 1015190
    inclPopulation = (L - initPop) / initPop
    
    container = []
    xRange = np.arange(-500, 501, 1)


    for i in xRange:
        res = L/(1 + ((inclPopulation) * (math.e)**(-k * (i - x0))))
        container.append(res)
    return [container, xRange]

# Logistic Function with Human Population
def logisticsHumanPop(rate):
    # Calculates Logistic Equation
    [dataResults, xRange] = logistic(rate)

    # Graphs Data
    # plt.plot(xRange, dataResults)
    # plt.yticks(np.arange(1, 2000001, step=500000))
    # plt.show()
    
    return [dataResults, xRange]

def malthusianModel(rate):
    p_0 = 1015190
    t = np.linspace(-1, 400, 10000000)
    y = p_0 * (math.e ** (rate * t))

    return [y, t]


def plotter(equation1, linps1, equation2, linps2):
    
    xStart = -100
    xEnd = 100
    
    figure, axis = plt.subplots(1, 3)

    axis[0].plot(linps1, equation1, 'b')
    axis[0].set_title("Malthsian Model")
    
    axis[1].plot(linps1, equation1, 'b', label = 'Malthusian Model')
    axis[1].plot(linps2, equation2, 'r', label = 'Logistic Model')
    axis[1].set_xlim([0, xEnd])
    axis[1].set_ylim([0, 3050000])
    axis[1].legend()
    
    # axis[1].relim([xStart, xEnd])
    # axis[1].relim([1000000, 3050000])
    # axis[1].xticks(np.arange(xStart, xEnd, step=25))


    axis[2].plot(linps2, equation2, 'r')
    axis[2].set_title("Logistic Model")
    
    
    #plt.plot(linps1, equation1, 'b', label = 'Malthusian Model')
    #plt.plot(linps2, equation2, 'r', label = 'Logistic Model')
    
    plt.legend()
    plt.grid(True, linestyle =':')

    plt.xlabel('Years')
    plt.ylabel('Population')

    plt.show()


def main():
    # Reads Data in
    birthData = pd.read_csv('data/modified/Births.csv')
    deathData = pd.read_csv('data/modified/Deaths.csv')

    df = pd.read_csv('data/modified/Fresno County Annual Population data.csv', parse_dates=['DATE'])

    # Extracts it into lists
    [year, bCount, dCount] = [birthData['Year'].tolist(), birthData['Count'].tolist(), deathData['Count'].tolist()]

    popData = df[df['DATE'].dt.year > 1998]

    [populationDates, populationNums] = [popData['DATE'].tolist(), popData['CAFRES9POP'].tolist()]
    popValues = [int(str(num).replace('.', '')) for num in populationNums]

    # Calculate Birth and Death Rate
    birthRate = getRate(bCount, popValues)
    deathRate = getRate(dCount, popValues)

    # Calculates overall Rate
    rateVal = birthRate - deathRate

    print(f"The birth Rate: {birthRate}")
    print(f"The death Rate: {deathRate}")
    print(f"RATE VAL = {rateVal}")


    [l_eq, l_range] = logisticsHumanPop(rateVal)
    [m_eq, m_range] = malthusianModel(rateVal)

    plotter(m_eq, m_range, l_eq, l_range)

if __name__ == "__main__":
    main()
