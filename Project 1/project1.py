import secrets
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import plotly.graph_objects as go
plt.style.use("fivethirtyeight")


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

def montyFall(numDoors, rule, trial):
    #Create a set of doors by using pre-set number of doors
    doors = [i for i in range (1,numDoors+1)]
    
    #Assign the car to a door
    car = secrets.choice(doors)

    #Guest first choice
    guest_1st_choice = secrets.choice(doors)

    #Host slips on banana peel so he can accidentally opens the door with the car
    host_can_open = set(doors) - set([guest_1st_choice])
   
    openlist=[]
    #Host opens all other doors and lefts only one door for the guest as the second choice.
    for y in range (numDoors-2):
        host_opens = secrets.choice(list(host_can_open -set(openlist)))
        #if the door of host accidentlly, the guest will lose
        if host_opens == car:
            return False
            break

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
    fileName = "Result.csv"
    data=[list1[:],list2[:],list3[:],list4[:]]
    label2=['Hall_Win_Switch','Fall_Win_Switch','Hall_Win_Stay','Fall_Win_Stay']

    with open(fileName, 'w') as csvfile:
        fieldNames.insert(0,'')
        writer = csv.writer(csvfile)
        writer.writerow(fieldNames)
        for i in data:
            newElement =label2[data.index(i)]
            i.insert(0,str(newElement))
            writer.writerow(i)
    plot_table("Result.csv")



#Create a bar chart by using the result
def barChart(list1,list2,list3, list4):
    fieldNames=['3 doors', '6 doors', '9 doors', '20 doors', '100 doors']
    width = 0.2
    x_list1 = [x-width for x in range(len(list1))]
    x_list2 = [x for x in range(len(list2))]
    x_list3 = [x+width for x in range (len(list3))]
    x_list4 = [x+width*2 for x in range (len(list4))]

    fig,ax = plt.subplots()
    bar1 = ax.bar(x_list1,list1,width,label='Hall_Win_Switch')
    bar2 = ax.bar(x_list2,list2,width,label='Fall_Win_Switch')
    bar3 = ax.bar(x_list3,list3,width,label='Hall_Win_Stay')
    bar4 = ax.bar(x_list4,list4,width,label='Fall_Win_Stay')
   


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
    ax.set_title(f'Monty Hall & Fall Swtiching and Staying Scenario Probability')
    plt.savefig(f'BarChart.png')

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

def plot_probability_distribution(module, trial_marks, win_probabilities, num_doors, strategy):
    # Create the figure object
    fig = go.Figure()

    last_known_value = 0  # Initialize a fallback last known value

    # Iterate over each door configuration and handle data filling
    for i, num in enumerate(num_doors):
        current_data = win_probabilities[i]

        if not current_data:  # If the list is empty
            if i == 0 or not any(win_probabilities[:i]):  # If it's the first list or all previous lists are empty
                current_data = [last_known_value] * len(trial_marks)  # Use the initial last known value (0 or updated)
                print(f"No initial data for {num} doors; using zero or last known non-zero values.")
            else:
                # Find the last non-empty list before the current one
                for prev_data in reversed(win_probabilities[:i]):
                    if prev_data:
                        last_known_value = prev_data[-1]
                        break
                current_data = [last_known_value] * len(trial_marks)  # Use last known value from the previous non-empty list
        else:
            # Update the last known value from the current non-empty list
            last_known_value = current_data[-1]
            # Ensure the list covers all trial marks by extending the last known value
            additional_length = len(trial_marks) - len(current_data)
            current_data.extend([last_known_value] * additional_length)

        # Add the trace with the adjusted or verified data
        fig.add_trace(go.Scatter(
            x=trial_marks, 
            y=current_data,
            mode='lines',  # Set mode to lines and markers
            name=f'{num} doors',
            #marker=dict(size=0.5, opacity=0.8)
        ))

    # Update the layout to add titles and axis labels
    fig.update_layout(
        title=f'{module} Win Probability Convergence Over Trials - {strategy} Strategy',
        xaxis_title='Number of Trials',
        yaxis_title='Win Probability',
        legend_title='Number of Doors',
        plot_bgcolor='white'  # Set background color to white for better visibility
    )
    
    # Check if any traces were added to figure
    if not fig.data:
        print("No data available to plot after processing.")
        return  # Exit if no data to plot
    
    # Show the figure
    fig.show()

def main():
    #Number of doors
    numDoors = [3,6,9,20,100]
    #simulation times
    trials = 100000
    #array for tracing
    trace1 =[[] for _ in numDoors]
    trace2 =[[] for _ in numDoors]
    trace3 =[[] for _ in numDoors]
    trace4 =[[] for _ in numDoors]
  
    trial_marks = list(range(1, trials + 1))

    #Monty Hall simulation 
    #Probabilities Holder Declaration
    #Swtich
    winProbability1=[]
    loseProbability1=[]
    #Stay 
    winProbability2=[]
    loseProbability2 =[]
    for index, val in enumerate(numDoors):
        print(f"Doors = {val}")
        countWin1 = 0
        countLose1 = 0
        #Always Switching Case:
        for x in range(trials):
            if (montyHall(val, 'switch', x)):
                countWin1 +=1
                current_probability = countWin1 / (x + 1)
                trace1[index].append(current_probability)
            else:
                countLose1 +=1
        
        winProbability1.append(round(countWin1/trials,2))
        loseProbability1.append(round(countLose1/trials,2))
 
        #Always Staying Case:
        countWin2 = 0
        countLose2 = 0
        for x in range(trials):
            if (montyHall(val,'stay',x)):
                countWin2 +=1
                current_probability = countWin2 / (x + 1)
                trace2[index].append(current_probability)
            else:
                countLose2 +=1
        
        winProbability2.append(round(countWin2/trials,2))
        loseProbability2.append(round(countLose2/trials,2))
    
    
    #Monty Fall simulation
    #Probabilities Holder Declaration
    #Switch
    winProbability3=[]
    loseProbability3 =[]
    #Stay
    winProbability4=[]
    loseProbability4 =[]
    for index2, val2 in enumerate(numDoors):
        print(f"Doors = {val2}")
        countWin3=0
        countLose3=0
        #Always Switching Case:
        for x in range(trials):
            if (montyFall(val2, 'switch', x)):
                countWin3 +=1
                current_probability = countWin3 / (x + 1)
                trace3[index2].append(current_probability)
            else:
                countLose3 +=1
        
        winProbability3.append(round(countWin3/trials,2))
        loseProbability3.append(round(countLose3/trials,2))

        #Always Staying Case:
        countWin4 = 0
        countLose4 = 0
        for x in range(trials):
            if (montyFall(val2,'stay',x)):
                countWin4 +=1
                current_probability = countWin4 / (x + 1)
                trace4[index2].append(current_probability)
            else:
                countLose4 +=1
        
        winProbability4.append(round(countWin4/trials,2))
        loseProbability4.append(round(countLose4/trials,2))
   

    #print the result
    print_Result(winProbability1,winProbability3,winProbability2,winProbability4)
    
    # print(f"{winProbability1=}")
    # print(f"{winProbability2=}")
    # print(f"{winProbability3=}")
    # print(f"{winProbability4=}")

    # plot_probability_distribution("Monty Hall",trial_marks,trace1,numDoors, 'Switch')
    # plot_probability_distribution("Monty Hall",trial_marks,trace2,numDoors, 'Stay')
    plot_probability_distribution("Monty Fall",trial_marks,trace3,numDoors, 'Switch')
    plot_probability_distribution("Monty Fall",trial_marks,trace4,numDoors, 'Stay')
if __name__ == "__main__":
    main()