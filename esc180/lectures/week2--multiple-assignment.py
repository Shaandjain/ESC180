#multiple assignment
x, y, x = 5, "hi", "praxis" #same as x = 5, then y = "hi", etc..

#swap values using multiple assignment
x,y = y,x

#doesn't work
#x = y
#y = x

temp = x
x = y
y = temp

#Cracking the Coding Interview (CTCI)
#x and y are integers
#write code swap their values without
#multiple assignemnt, and without temporary space

x = x+y #first line of the solution
#communicating info to and from functions

print(x,y)