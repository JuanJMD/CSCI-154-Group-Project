# OBJECTIVES
# 1. Get growth rate
# Get max capacity 

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

# Obtains the Population Rate
def getRate(num, population):
    rates = []
    for i in range(len(num)):
        getBirth = num[i]
        getPopSize = population[i]

        rates.append(getBirth/getPopSize)

    averageRate = sum(rates)/len(num)
    return averageRate

# Creates Logistic Function
def logistic(rate):
    areaFresno=5958.4
    areaUS=3797000
    USCap = 807000000
    L = USCap*(areaFresno/areaUS)
    k = rate
    x = 0
    x0 = 0
    initPop = 828051
    inclPopulation = (L - initPop) / initPop
    
    container = []
    xRange = np.arange(0, 45, 1)

    for i in xRange:
        res = L/(1 + ((inclPopulation) * (math.e)**(-k * (i - x0))))
        container.append(res)
    return [container, xRange]

# Logistic Function with Human Population
def logisticsHumanPop(rate):
    # Calculates Logistic Equation
    [dataResults, xRange] = logistic(rate)

    return [dataResults, xRange]

def malthusianModel(rate):
    p_0 = 828051
    t = np.arange(0, 45, 1)
    y = p_0 * (math.e ** (rate * t))

    return [y, t]

def plotter(equation1, linps1, equation2, linps2, rawData):
    xEnd = 44

    # Plots the Malthusian Model
    fig1, ax1 = plt.subplots()
    ax1.plot(linps1, equation1, 'b')
    ax1.set_title("Malthusian Model")
    ax1.grid(True, linestyle=':')
    ax1.set_xlim([0, xEnd])
    ax1.set_xlabel("Years")
    ax1.set_ylabel("Population")
    ax1.set_xticks(np.linspace(0, xEnd, xEnd))
    ax1.set_xticklabels(np.linspace(2002, (2002 + xEnd), xEnd, dtype=int), rotation=45)

    # All combined Models
    fig2, ax2 = plt.subplots()
    ax2.plot(linps1, equation1, 'b', label='Malthusian Model')
    xPoints = list(range(len(rawData)))
    ax2.scatter(xPoints, rawData, label='Fresno County Annual Population Data')
    ax2.plot(linps2, equation2, 'r', label='Logistic Model')
    ax2.plot(41, equation1[41], 'o-b')
    ax2.plot(41, equation2[41], 'o-r')
    ax2.annotate(("Year " + str(2042) + " = " + str(format(equation1[41], '.1f'))), (41, equation1[41]),
                 xycoords='data', xytext=(20, 50), textcoords='offset points', arrowprops=dict(facecolor='black', shrink=0.05))
    ax2.annotate(("Year " + str(2042) + " = " + str(format(equation2[41], '.1f'))), (41, equation2[41]),
                 xycoords='data', xytext=(20, 50), textcoords='offset points', arrowprops=dict(facecolor='black', shrink=0.05))

    ax2.grid(True, linestyle=':')
    ax2.set_xlim([0, xEnd])
    ax2.set_xlabel("Years")
    ax2.set_ylabel("Population")

    ax2.set_xticks(np.linspace(0, xEnd, xEnd))
    ax2.set_xticklabels(np.linspace(2002, (2002 + xEnd), xEnd, dtype=int), rotation=45)
    ax2.legend()

    # Plots the Logistic Model
    fig3, ax3 = plt.subplots()
    ax3.plot(linps2, equation2, 'r')
    ax3.set_title("Logistic Model")
    ax3.grid(True, linestyle=':')
    ax3.set_xlim([0, xEnd])
    ax3.set_xlabel("Years")
    ax3.set_ylabel("Population")
    ax3.set_xticks(np.linspace(0, xEnd, xEnd))
    ax3.set_xticklabels(np.linspace(2002, (2002 + xEnd), xEnd, dtype=int), rotation=45)

    # Plots Chart
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    tableColNames = ['Years', 'Malthusian Model', 'Logistic Model', 'Raw Data', 'M - R Diff', 'L - R Diff']
    tData = []
    # Adds data to table
    for i in range(len(rawData)):
        rmDiff = format((float(format(rawData[i], '.1f')) -  float(format(equation1[i], '.1f'))), '.1f')
        rlDiff = format((float(format(rawData[i], '.1f')) -  float(format(equation2[i], '.1f'))), '.1f')
        tData.append([(2002 + i), format(equation1[i], '.1f'), format(equation2[i], '.1f'), format(rawData[i], '.1f'), rmDiff, rlDiff])

    table = ax4.table(cellText=tData, loc='center',
                      colLabels=tableColNames, cellLoc='center', fontsize='20')
    table.auto_set_font_size(False)
    ax4.axis('off')
    for j, col_label in enumerate(tData[0]):
        table[(0, j)].set_facecolor('lightblue')
    
    # Determines color depending on which value is closer to actual data
    for i in range(len(tData)):
        if float(tData[i][3]) < float(tData[i][4]):
            table[(i+1, 3)].set_facecolor('lightgreen')
        elif float(tData[i][3]) > float(tData[i][4]):
            table[(i+1, 4)].set_facecolor('lightgreen')
        elif float(tData[i][3]) == float(tData[i][4]):
            table[(i+1, 3)].set_facecolor('lightgreen')
            table[(i+1, 4)].set_facecolor('lightgreen')

    plt.show()


def main():
    # Reads Data in
    birthData = pd.read_csv('data/modified/Births.csv', parse_dates=['Year'])
    deathData = pd.read_csv('data/modified/Deaths.csv', parse_dates=['Year'])

    birthData = birthData[birthData['Year'].dt.year > 2001]
    deathData = deathData[deathData['Year'].dt.year > 2001]

    df = pd.read_csv('data/modified/Fresno County Annual Population data.csv', parse_dates=['DATE'])

    # Extracts it into lists
    [year, bCount, dCount] = [birthData['Year'].tolist(), birthData['Count'].tolist(), deathData['Count'].tolist()]

    popData = df[df['DATE'].dt.year > 2001]

    [populationDates, populationNums] = [popData['DATE'].tolist(), popData['CAFRES9POP'].tolist()]
    for i in range(len(populationNums)):
        populationNums[i] = "{0:.3f}".format(populationNums[i])

    popValues = [int(str(num).replace('.', '')) for num in populationNums]

    # Calculate Birth and Death Rate
    birthRate = getRate(bCount, popValues)
    deathRate = getRate(dCount, popValues)
    print(f"{birthRate=},{deathRate=}")

    # Calculates overall Rate
    rateVal = birthRate - deathRate
    print('rate:', rateVal)

    [l_eq, l_range] = logisticsHumanPop(rateVal)
    [m_eq, m_range] = malthusianModel(rateVal)

    plotter(m_eq, m_range, l_eq, l_range, popValues)


if __name__ == "__main__":
    main()
