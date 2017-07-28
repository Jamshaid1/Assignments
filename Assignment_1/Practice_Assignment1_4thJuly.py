#!/usr/bin/python
# solved By Jamshaid Ahmed Ghauri
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates. 
#
import calendar

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
        #number of Days in each month in a year
        number_Of_Days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        days=0
        #Age in years
        years=year2-year1;
        
        #there are 365 days in a year
        days=(365*years)
        
        #Convert Months into days
        if month1 != month2:  
         days=days+(number_Of_Days_in_month[month1-1]-day1)+(day2)
        #Add leap days
        days=days+calendar.leapdays(year1,year2+1)       
             
        #decrement in days if the current month is feb 
        if month2 <= 2:
           days=days-1
        #Convert months into days
        if month2-month1 > 1:
         break_1st_time=0

         for month in range(month1,month2):

               if break_1st_time==1:
                days=days+(number_Of_Days_in_month[month-1])

               break_1st_time=1
 

        if month1-month2 > 1:
         start_from_next_month=0

         for month in range(month1,month2):

               if start_from_next_month==1:
                days=days+(number_Of_Days_in_month[month-1])

               start_from_next_month=1


        return days 


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,18), 48), 
                  ((1995,1,26,2017,7,4), 8195),
                  ((2011,6,30,2012,6,30), 366),
                  ((1980,12,16,2017,7,4), 13534),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")


test()

