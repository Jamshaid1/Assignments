#!/usr/bin/python
# solved By Jamshaid Ahmed Ghauri
# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

def print_multiplication_table( n ):
   num=1
   for i in range(1,n+1):
    print num,"*",i,"=",num*i
   for i in range(1,n+1):
    print (num+1),"*",i,"=",(num+1)*i

   return

print_multiplication_table(2)
print 

print_multiplication_table(3)
