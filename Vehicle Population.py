#Project for Vehicle population 

import csv   #Importing csv module
import numpy #Importing numpy module
import matplotlib.pyplot as plt


Month = []                      #Use to store month name (Single array)
V_Type_Population=[]            #Use to store population number depend on car(Double)

#Function1
def Menu():
    Accept_Array = ["0","1","2","3","4","5","6","7","8","9"]
    print("1.Vehicle population for Taxi for all months in 2012")
    print("2.Selected vehicle code to display means of second half and list of exceed mean")
    print("3.Selected vehicle code to show month which exceed 3% of previous month")
    print("4.Drawing plot for car population")
    print("5.Quit")
    Set_Spacer()
    User_Input = ""
    # while User_Input not in Accept_Array:
    #     User_Input = input("Please select the vehicle code (1-4) and 5 for Quit:")
    User_Input = input("Please select the vehicle code (1-4) and 5 for Quit:")
    if(User_Input not in Accept_Array):
        User_Input=10
        
    return int(User_Input)

def Set_Spacer():
    print(20*"=")
    print(20*"=")
    
#Function2    
def Show_Car_Type(Array):
    Accept_Array = ["0","1","2","3","4","5","6","7","8","9"]
    for i in range(len(Array)):
        print(f"{i+1}.{Array[i][0]}")
    Choice = ""
    
    # while Choice not in Accept_Array:
    #     Choice = input("Select the type of car: ")
    
    Choice = input("Select the type of car: ")
    if(Choice not in Accept_Array):
        Choice=10
    return int(Choice)

    
    
        
#Firstly open csv file to read data


def Read_Data_CSV():
    Data=[]
    File = open("mvehpop_dataset.csv",'r')
    File_Reader = csv.reader(File)
    for i in File_Reader:
        Data.append(i)
    File.close()
    return Data



#function for choice 1
def Choice_1(): 
    #While1
    Data = Read_Data_CSV()
    Month=Data[0]
    V_Type_Population = Data[1:]
    for i in range(0,len(Month)):
            print(f"Vehicle calculation of Tax for {Month[i]} in 2012 is {V_Type_Population[5][i]}.")
            

    
def Choice_2():
    Data = Read_Data_CSV()
    Month=Data[0]
    V_Type_Population = Data[1:]
    User_Choice=Show_Car_Type(V_Type_Population)
    if(User_Choice > 6 or User_Choice < 1):
        Set_Spacer()
        print("Invilid option")
    else:
        Mean_Array=[]
        for i in V_Type_Population[User_Choice-1][7:12]:
            Mean_Array.append(int(i))
        Mean_Calculation = numpy.average(Mean_Array)
        print(f"The list which exceed mean value {Mean_Calculation} in population {V_Type_Population[User_Choice-1][0]}.")
        for i in range(7,13):
            if(int(V_Type_Population[User_Choice-1][i]) > Mean_Calculation): #Check the mean value is exceed or not
                print(f"{Month[i]} population is {V_Type_Population[User_Choice-1][i]}")
    
        
    
def Choice_3():
    Data = Read_Data_CSV()
    Month=Data[0]
    V_Type_Population = Data[1:]
    User_Choice=Show_Car_Type(V_Type_Population)
    if(User_Choice > 6 or User_Choice < 1):
        Set_Spacer()
        print("Invilid option")
    else:
        for i in range(2,len(Month)): #Error code for i in range(2,len(V_Type_Population))
            if(int(V_Type_Population[User_Choice-1][i]) >= int(V_Type_Population[User_Choice-1][i-1])+int(V_Type_Population[User_Choice-1][i-1])*0.03):
                print(f"{Month[i]} population is {V_Type_Population[User_Choice-1][i]}")
    
    
def Choice_4():
    Data = Read_Data_CSV()
    Month=Data[0]
    V_Type_Population = Data[1:]
    
    Temp_List=[]
    for i in range(1,len(Month)):
        Temp_List.append(int(V_Type_Population[1][i]) + int(V_Type_Population[4][i]))
    #Drawing line plot
    default_x_ticks = range(len(Month[1:]))
    plt.figure(1)
   # plt.subplot(1,2,1) #Modified code
    plt.plot(default_x_ticks,Temp_List,marker="*")
    plt.xticks(default_x_ticks,Month[1:])
    plt.xlabel("Month")
    plt.ylabel("Sum of Car and Rental Car population")
    plt.grid()
    plt.show()
    #Set width for bar 
    Width=0.3       
    default_x_ticks = range(len(Month[1:]))
    Bus_Bar = numpy.arange(len(Month[1:]))
    Taxi_Bar = [x + Width for x in Bus_Bar]
    
    plt.figure(2)
   # plt.subplot(1,2,2)
    plt.xlabel("Car type")
    plt.ylabel("Population of car")
    plt.xticks([i +Width for i in range(len(Month[1:]))],Month[1:])
    
    Temp_list = []
    for i in V_Type_Population[2][1:]:
        Temp_list.append(int(i))
    plt.bar(Bus_Bar,Temp_list,color='b',width=Width,label="Bus")
    
    
    Temp_list = []
    for i in V_Type_Population[3][1:]:
        Temp_list.append(int(i))
        
    plt.bar(Taxi_Bar,Temp_list,color='r',width=Width,label="Taxi")
    plt.legend(loc="lower right")
    plt.title("BarGraph")
    
    plt.show()
    
    






while(1):
    Set_Spacer()
    User_Choice = Menu()
    Set_Spacer()
    
    #Get the user input
  

    
    if(User_Choice == 1): #Vehicle population for Taxi for all months in 2012
    #Vehicle population of Taxi for month in 2012 is population
       Choice_1()


    elif(User_Choice ==2):
        Choice_2()
        
    elif(User_Choice ==3):
        Choice_3()
        
    elif(User_Choice ==4):
        Choice_4()
        
    elif(User_Choice ==5):
        print("Thanks for using our program")
        break
    else:
        
        print("Please try again")
    

