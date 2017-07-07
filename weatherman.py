#!/usr/bin/python

#For a given year display the highest temperature and day, lowest temperature and day,

month_list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

high_temp_list=[]

low_temp_list=[]

max_temp_date=[]

min_temp_date=[]


def input_year(year):
   'display the highest temperature and day, lowest temperature and day form input_year '

   for month in month_list:
    file_name = "Weatherman_Assignment/weatherdata/lahore_weather_"+ year +"_"+ month +".txt"
    input_file = open( file_name, "r" )

    weather=[]
    max_temp=[]
    min_temp=[]

    for line in input_file:
       if line[:4] == year:
         weather.append(line.split(','))

    for i in range (0,len(weather)):
     # Get max temp from given file

     max_temp.append(weather[i][1])
     # Get min temp from given file
     if weather[i][3]=="":
      min_temp.append("77")
     else:
       min_temp.append(weather[i][3])




    max_temp_date.append(max_temp.index(max(max_temp)) + 1)
    min_temp_date.append(min_temp.index(min(min_temp)) + 1)

    high_temp_list.append(max(max_temp))
    low_temp_list.append(min(min_temp))

   # Get position
    high_temp_pos=high_temp_list.index(max(high_temp_list))
    low_temp_pos = low_temp_list.index(min(low_temp_list))

   print "Highest:",max(high_temp_list)+"C",month_list[high_temp_pos],max_temp_date[high_temp_pos]
   print "Lowest:", min(low_temp_list) + "C", month_list[low_temp_pos], \
   min_temp_date[low_temp_pos]


input_year("1999")
