#!/usr/bin/python

#Use of List
list=['Jamshaid',21,5.67]
print "Name: ",list[0]
print "Age: ",list[1]
print "Height: ",list[2]
print calendar.leapdays(2012,2012)
print "I have following items"
list=['bag','pen','laptop']
print "1-",list[0]
print "2-",list[1]
print "3-",list[2]


#Use of dictionary
dictionary={'University':"University Of Gujrat",'City':'Gujrat','Contact':"0307-7268875",'Department':'IT'}


print "Department: ",dictionary['Department']
print "City: ",dictionary['City']
print "University: ",dictionary['University']
print "Contact: ",dictionary['Contact']

#define a funtion that take a string as input and print it
def printString( string ):
  print string;
  return

printString("Alhamdulilah I m doing well")

#define a function that take a list as input and print it
def printList(list):
       list.append('last Element')
       print list
       return


list=[2000,2001,2002,2003,2004]
printList(list)
print list

