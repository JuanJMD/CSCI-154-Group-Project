import secrets
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

def montyHall(numDoors, rule, trial):
    #Create a set of doors by using pre-set number of doors
    doors = []
    for x in range(numDoors+1):
        doors.append(x)
    
    #Assign the car to a door
    car = secrets.choice(doors)

    #Guest first choice
    guest_1st_choice = secrets.choice(doors)

    #The doors that host can open, which can only be the goat doors.
    host_can_open = set(doors) - set([car,guest_1st_choice])
    openlist=[]
    #Host opens all other doors and lefts only one door for the guest as the second choice.
    for y in range (numDoors-1):
        host_opens = secrets.choice(list(host_can_open -set(openlist)))
        openlist.append(host_opens)
    
    guest_2nd_choice = min(set(doors)-set(openlist + [guest_1st_choice]))
    
    if trial<=5:
        print(f"First choice: {guest_1st_choice}, Second choice: {guest_2nd_choice}, Car: {car} ")
    
    #Guest Strategies 
    if rule== 'switch':
        if car == guest_2nd_choice:
            result = True
        else:
            result = False

    if rule== 'stay':
        if guest_1st_choice == car:
            result = True
        else:
            result = False
    
    return result

#Write the result into a csv file and plot a table
def write_and_plot(list1,list2,list3,list4):
    fieldNames=['3 doors', '6 doors', '9 doors', '20 doors', '100 doors']
    fileName = "MontyHallResult.csv"
    data=[list1[:],list2[:],list3[:],list4[:]]
    label2=['Win_Switch','Lose_Switch','Win_Stay','Lose_Stay']

    with open(fileName, 'w') as csvfile:
        fieldNames.insert(0,'')
        writer = csv.writer(csvfile)
        writer.writerow(fieldNames)
        for i in data:
            newElement =label2[data.index(i)]
            i.insert(0,str(newElement))
            writer.writerow(i)
    plot_table("MontyHallResult.csv")



#Create a bar chart by using the result
def barChart(list1,list2,list3,list4):
    fieldNames=['3 doors', '6 doors', '9 doors', '20 doors', '100 doors']
    width = 0.2
    x_list1 = [x-width for x in range(len(list1))]
    x_list2 = [x for x in range(len(list2))]
    x_list3 = [x+width for x in range (len(list3))]
    x_list4 = [x+width*2 for x in range (len(list4))]

    fig,ax = plt.subplots()
    bar1 = ax.bar(x_list1,list1,width,label='Win_Switch')
    bar2 = ax.bar(x_list2,list2,width,label='Lose_Switch')
    bar3 = ax.bar(x_list3,list3,width,label='Win_Stay')
    bar4 = ax.bar(x_list4,list4,width,label='Lose_Stay')    


    def autolabel(bars, data):
        for bar, value in zip (bars, data):
            height = bar.get_height()
            ax.annotate('{}'.format(value),xy=(bar.get_x()+bar.get_width()/2,height),xytext=(0,2), textcoords ="offset points", ha='center',va='bottom')
    
    #label the bar
    autolabel(bar1,list1)
    autolabel(bar2,list2)
    autolabel(bar3,list3)
    autolabel(bar4,list4)

    x = np.arange(len(fieldNames))
    ax.set_xticks(x)
    ax.set_xticklabels(fieldNames)
    ax.legend()
    ax.set_xlabel('Door Secanrio')
    ax.set_ylabel('Probability of 100000 times')
    ax.set_title('Monty Hall Swtiching and Staying Scenario Probability')
    plt.savefig('BarChart.png')

#create table function
def plot_table(fileName):
    data= pd.read_csv(fileName)
    fig,ax=plt.subplots()
    ax.axis('off')
    table = plt.table(cellText = data.values, colLabels=data.columns,cellLoc='center',loc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1,1.5)
    plt.savefig("ResultTable.png")

def print_Result(list1,list2,list3,list4):
    write_and_plot(list1,list2,list3,list4)
    barChart(list1,list2,list3,list4)
    plt.show()


def main():
    #Number of doors
    numDoors = [3,6,9,20,100]
    #simulation times
    trials = 100000
    #alway switch probaility
    winProbability1=[]
    loseProbability1=[]
    #always Stay probability
    winProbability2=[]
    loseProbability2 =[]

    for n in numDoors:
        print(f"Doors = {n}")
        countWin1 = 0
        countLose1 = 0
        #Always Switching Case:
        for x in range(trials):
            if (montyHall(n, 'switch', x)):
                #print("Switch")
                countWin1 +=1
            else:
                countLose1 +=1
        
        winProbability1.append(round(countWin1/trials,3))
        loseProbability1.append(round(countLose1/trials,3))
        # print("Door number: ", n)
        # print("Win: ", countWin1)
        # print("Lose: ", countLose1)
        # print("Always Switching Win probability: ", countWin1/times)


        #Always Staying Case:
        countWin2 = 0
        countLose2 = 0
        for x in range(trials):
            if (montyHall(n,'stay',x)):
                countWin2 +=1
            else:
                countLose2 +=1
        winProbability2.append(round(countWin2/trials,3))
        loseProbability2.append(round(countLose2/trials,3))
        # print("Door number: ", n)
        # print("Win: ", countWin2)
        # print("Lose: ", countLose2)
        # print("Always Staying Win probability: ", countWin2/times)
        # winProbability2.append( countWin2/times)
        # loseProbability2.append(countLose2/times)
    
    print(f"{winProbability1=}")
    print(f"{loseProbability1=}")
    print(f"{winProbability2=}")
    print(f"{loseProbability2=}")

    #print the result
    print_Result(winProbability1,loseProbability1,winProbability2,loseProbability2)

if __name__ == "__main__":
    main()