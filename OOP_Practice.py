#!/usr/bin/python
print "OOP practice program \n"

class human:
    'Base class of Student and Employee'
    def setAttributes(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayAttribute(self):
        print "Name:", self.name, " Age:", self.age
        print "Gender:", self.gender

#Use inheritance
class Student(human):
    stdCount=0

    def __init__(self, university):
     self.university=university
     Student.stdCount+=1

    def NumberOfStudents(self):
     print "Number Of Students",Student.stdCount

    def universityName(self):
        print "University: ",self.university,'\n'


#Use inheritance
class Employee(human):
    empCount=0

    def __init__(self, organization):
     self.organization=organization
     Employee.empCount+=1


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
#operator Overloading
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1=Vector(2,8)
v2=Vector(7,2)
v3=Vector(3,9)

print v1 + v2 + v3,'\n'
print v1 * v2 * v3,'\n'

std1=Student("University Of Gujrat")

std2=Student("University Of Lahore")

std3=Student("PUCIT")

std1.setAttributes("Junaid",24,'Male')
std2.setAttributes("Zuhaib",20,'Male')
std3.setAttributes("Iqra",18,'Female')

std1.displayAttribute()
std1.universityName()

std2.displayAttribute()
std2.universityName()

std3.displayAttribute()
std3.universityName()

#use shareable variables
std3.NumberOfStudents()

print "Totall number of students",Student.stdCount
