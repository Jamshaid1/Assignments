#!/usr/bin/python
import sys

month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
high_temp=[]
low_temp=[]
humid=[]
max_temp_date=[]
min_temp_date=[]
humid_date=[]


def given_year(year,path):
   'display the highest temperature and day, lowest temperature and day for given year '

   for month_Name in month:
       file_name = path+"/lahore_weather_"+ year +"_"+ month_Name +".txt"
       input_file = open( file_name, "r" )

       weather = []
       max_temp = []
       min_temp = []
       mean_humid = []

       for line in input_file:
           if line[:4] == year:
               weather.append(line.split(','))

       for i in range (0,len(weather)):
            # Get max temp from given file
            if weather[i][1] == "":
                max_temp.append("-7")  # add garbage value
            else:
                max_temp.append(weather[i][1])
            # Get min temp from given file
            if weather[i][3]=="":
                min_temp.append("77")  # add garbage value
            else:
                min_temp.append(weather[i][3])

            # Get most humidity
            if weather[i][8] == "":
                mean_humid.append(0)  # add garbage value
            else:
                mean_humid.append(weather[i][8])
       
       max_temp_date.append(max_temp.index(max(max_temp)) + 1)
       min_temp_date.append(min_temp.index(min(min_temp)) + 1)
       humid_date.append(mean_humid.index(max(mean_humid))+1)


       high_temp.append(int(max(max_temp)))
       low_temp.append(int(min(min_temp)))
       humid.append(max(mean_humid))

   # Get position
   high_temp_pos=high_temp.index(max(high_temp))
   low_temp_pos = low_temp.index(min(low_temp))
   humid_pos=humid.index(max(humid))


   print "Highest:",str(max(high_temp))+"C",month[high_temp_pos],max_temp_date[high_temp_pos]
   print "Lowest:", str(min(low_temp)) + "C", month[low_temp_pos],min_temp_date[low_temp_pos]
   print "Humid:",str(max(humid))+"%",month[humid_pos],humid_date[humid_pos]


def given_month(year,month,path):
    'display the average highest temperature, average lowest temperature, average humidity '
    file_name = path+"lahore_weather_" + year + "_" + month + ".txt"
    input_file = open(file_name, "r")
    weather = []
    max_temp = []
    min_temp = []
    mean_humid = []

    for line in input_file:
        if line[:4] == year:
            weather.append(line.split(','))

    for i in range(0, len(weather)):
        # Get max temp from given file
        if weather[i][1] == "":
            max_temp.append(0)  # add garbage value
        else:
            max_temp.append(int(weather[i][1]))
        # Get min temp from given file
        if weather[i][3] == "":
            min_temp.append(0)  # add garbage value
        else:
            min_temp.append(int(weather[i][3]))
        
        # Get most humidity
        if weather[i][8] == "":
            mean_humid.append(0)  # add garbage value
        else:
            mean_humid.append(int(weather[i][8]))

    avg_h_temmp=sum(max_temp)/len(max_temp)
    avg_l_temmp = sum(min_temp) / len(min_temp)
    avg_humid = sum(mean_humid) / len(mean_humid)

    print "Highest Average:",str(avg_h_temmp)+'C'
    print "Lowest Average:",str(avg_l_temmp)+'C'
    print "Average Humidity:",str(avg_humid)+'%'

def bar_chart(year,month,path):
    'draw two horizontal bar charts on the console for the highest and lowest temperature'
    file_name = path+"lahore_weather_" + year + "_" + month + ".txt"
    input_file = open(file_name, "r")
    weather = []
    max_temp = []
    min_temp = []
    blue_sign="\033[1;34;0m+"
    red_sign="\033[1;31;0m+"
    end = "\033[0;0m" # end color effect

    print month,year

    for line in input_file:
        if line[:4] == year:
            weather.append(line.split(','))

    for line in input_file:
        if line[:4] == year:
            weather.append(line.split(','))

    for i in range(0, len(weather)):
        # Get max temp from given file
        if weather[i][1] == "":
            max_temp.append(-7)  # add garbage value
        else:
            max_temp.append(int(weather[i][1]))
        # Get min temp from given file
        if weather[i][3] == "":
            min_temp.append(77)  # add garbage value
        else:
            min_temp.append(int(weather[i][3]))



    for i in range(0,len(max_temp)):
     if i<9:
         day='0'+str(i+1)
     else:
         day=str(i+1)
     if max_temp[i]==-7 or min_temp[i]==77:
      print "none"
     else:
      print day + " " + red_sign * max_temp[i]+end, str(max_temp[i]) + 'C'
      print day + " " + blue_sign * min_temp[i]+end, str(min_temp[i]) + 'C'


def single_bar(year,month,path):
    'draw one horizontal bar chart on the console for the highest and lowest temperature on each day'
    file_name = path+"lahore_weather_" + year + "_" + month + ".txt"
    input_file = open(file_name, "r")
    weather = []
    max_temp = []
    min_temp = []
    blue_sign="\033[1;34;0m+"
    red_sign="\033[1;31;0m+"
    end = "\033[0;0m" # end color effect

    print month,year

    for line in input_file:
        if line[:4] == year:
            weather.append(line.split(','))

    for line in input_file:
        if line[:4] == year:
            weather.append(line.split(','))

    for i in range(0, len(weather)):
        # Get max temp from given file
        if weather[i][1] == "":
            max_temp.append(-7)  # add garbage value
        else:
            max_temp.append(int(weather[i][1]))
        # Get min temp from given file
        if weather[i][3] == "":
            min_temp.append(77)  # add garbage value
        else:
            min_temp.append(int(weather[i][3]))



    for i in range(0,len(max_temp)):
     if i<9:
         day='0'+str(i+1)
     else:
         day=str(i+1)
     if max_temp[i]==-7 or min_temp[i]==77:
      print "none"
     else:
      #print day + " " + red_sign * max_temp[i]+end, str(max_temp[i]) + 'C'
      print day + " " + blue_sign * min_temp[i]+end+ red_sign * max_temp[i]+end, str(min_temp[i]) + 'C',"-",str(max_temp[i]) + 'C'



def main ():
    'Main entry for user interface'


    command = sys.argv[1]



    if command=="-e":
        year = sys.argv[2]
        path = sys.argv[3]
        given_year(year,path)
    elif command=="-a":
        year = sys.argv[2]
        month= sys.argv[3]
        path=sys.argv[4]
        given_month(year,month,path)
    elif command=="-c":
        year = sys.argv[2]
        month = sys.argv[3]
        path = sys.argv[4]
        bar_chart(year, month,path)
        single_bar(year, month,path)

    else:
        print "Invalid command"








if __name__ == "__main__":
    main()
