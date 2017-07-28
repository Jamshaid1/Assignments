#!/usr/bin/python
import sys
import argparse
import csv

month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
high_temp=[]
low_temp=[]
humid=[]
max_temp_date=[]
min_temp_date=[]
most_humid_date=[]


    

def given_year(year, path):
        'display the highest temperature and day, lowest temperature and day for given year '

        for month_Name in month:
	    file_name  ="%s/lahore_weather_%s_%s.txt" %(path, year, month_Name)
            input_file = open(file_name, "r")
            input_file.next()
            
            max_temp = []
            min_temp = []
            mean_humid = []
            date = []
            
            
            for row in csv.DictReader(input_file):
                # Get max temp from given file
                if str(row['Max TemperatureC']).isdigit():
                    max_temp.append(int(row['Max TemperatureC']))
                    date.append(row['PKT'])
                # Get min temp from given file
                if str(row['Min TemperatureC']).isdigit():
                    min_temp.append(int(row['Min TemperatureC']))
                # Get most humidity
                if str(row[' Mean Humidity']).isdigit():
                    mean_humid.append(int(row[' Mean Humidity']))

            if max_temp:
                max_temp_date.append(date[max_temp.index(max(max_temp))])
            if min_temp:
                min_temp_date.append(date[min_temp.index(min(min_temp))])
            if mean_humid:
                most_humid_date.append(date[mean_humid.index(max(mean_humid))])
            if max_temp:  
                high_temp.append(int(max(max_temp)))
            if min_temp:
                low_temp.append(int(min(min_temp)))
            if mean_humid:
                humid.append(int(max(mean_humid)))
            
                
        # Get position
        high_temp_date = max_temp_date[high_temp.index(max(high_temp))]
        low_temp_date  = min_temp_date[low_temp.index(min(low_temp))]
        humid_date     = most_humid_date[humid.index(max(humid))]
        print "Highest:", str(max(high_temp)) + "C",high_temp_date
        print "Lowest:",  str(min(low_temp)) + "C", low_temp_date 
        print "Humid:",   str(max(humid)) + "%",humid_date   






def given_month(year,month,path):
    'display the average highest temperature, average lowest temperature, average humidity '
    file_name  ="%s/lahore_weather_%s_%s.txt" %(path, year, month)
    input_file = open(file_name, "r")
    input_file.next()
    weather = []
    max_temp = []
    min_temp = []
    mean_humid = []

    for row in csv.DictReader(input_file):
          # Get max temp from given file
          if str(row['Max TemperatureC']).isdigit():
              max_temp.append(int(row['Max TemperatureC']))
          # Get min temp from given file
          if str(row['Min TemperatureC']).isdigit():
              min_temp.append(int(row['Min TemperatureC']))
          # Get most humidity
          if str(row[' Mean Humidity']).isdigit():
              mean_humid.append(int(row[' Mean Humidity']))

    avg_h_temmp=sum(max_temp)/len(max_temp)
    avg_l_temmp = sum(min_temp) / len(min_temp)
    avg_humid = sum(mean_humid) / len(mean_humid)

    print "Highest Average:",str(avg_h_temmp)+'C'
    print "Lowest Average:",str(avg_l_temmp)+'C'
    print "Average Humidity:",str(avg_humid)+'%'

def bar_chart(year,month,path):
    'draw two horizontal bar charts on the console for the highest and lowest temperature'
    file_name  ="%s/lahore_weather_%s_%s.txt" %(path, year, month)
    input_file = open(file_name, "r")
    input_file.next()
    max_temp = []
    min_temp = []
    blue_sign="\033[1;34;0m+"
    red_sign="\033[1;31;0m+"
    end = "\033[0;0m" # end color effect

    print month,year
    for row in csv.DictReader(input_file):
          # Get max temp from given file
          if str(row['Max TemperatureC']).isdigit():
              max_temp.append(int(row['Max TemperatureC']))
          else:
              max_temp.append('') 
          # Get min temp from given file
          if str(row['Min TemperatureC']).isdigit():
              min_temp.append(int(row['Min TemperatureC']))
          else:
              min_temp.append('')
    
    for i in range(0,len(max_temp)):
       if i<9:
           day='0'+str(i+1)
       else:
           day=str(i+1)
       if max_temp[i]=='' or min_temp[i]=='':
           print "none"
       else:
           print day + " " + red_sign * max_temp[i]+end, str(max_temp[i]) + 'C'
           print day + " " + blue_sign * min_temp[i]+end, str(min_temp[i]) + 'C'


def single_bar(year,month,path):
    'draw one horizontal bar chart on the console for the highest and lowest temperature on each day'
    file_name  ="%s/lahore_weather_%s_%s.txt" %(path, year, month)
    input_file = open(file_name, "r")
    input_file.next()
    max_temp = []
    min_temp = []
    blue_sign="\033[1;34;0m+"
    red_sign="\033[1;31;0m+"
    end = "\033[0;0m" # end color effect

    print month,year

    for row in csv.DictReader(input_file):
          # Get max temp from given file
          if str(row['Max TemperatureC']).isdigit():
              max_temp.append(int(row['Max TemperatureC']))
          else:
              max_temp.append('') 
          # Get min temp from given file
          if str(row['Min TemperatureC']).isdigit():
              min_temp.append(int(row['Min TemperatureC']))
          else:
              min_temp.append('')
   


    for i in range(0,len(max_temp)):
       if i<9:
           day='0'+str(i+1)
       else:
           day=str(i+1)
       if max_temp[i]=='' or min_temp[i]=='':
           print "none"
       else:
           print day + " " + blue_sign * min_temp[i]+end+ red_sign * max_temp[i]+end, str(min_temp[i]) + 'C',"-",str(max_temp[i]) + 'C'


def test1():
     parser = argparse.ArgumentParser(description='weather report')
     parser.add_argument("year", help="display the highest temperature and day, lowest temperature and day for given year",type=str)
     parser.add_argument("path", help="Path of weather data files",type=str)
     args = parser.parse_args()
     given_year(args.year,args.path)
    
def test2():
     parser = argparse.ArgumentParser(description='weather report')
     parser.add_argument("year",type=str)
     parser.add_argument("month", help="month name Example:Jan",type=str)
     parser.add_argument("path", help="Path of weather data files",type=str)
     args = parser.parse_args()
     given_month(args.year,args.month,args.path)
        
def test3():
     parser = argparse.ArgumentParser(description='weather report')
     parser.add_argument("year",type=str)
     parser.add_argument("month", help="month name Example:Jan",type=str)
     parser.add_argument("path", help="Path of weather data files",type=str)
     args = parser.parse_args()
     bar_chart(args.year,args.month,args.path)
     single_bar(args.year,args.month,args.path)


if __name__ == "__main__":

     
    #test1()
    #test2()
    test3()
