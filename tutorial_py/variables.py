
#DECLARE

# it has no command for declaring variable
# it is created the moment you first assign a value to it
# variable do not need to be declared with any particular TYPE, and change TYPE after they have been set
a = "paulo"

print(type(a))

a = 10

print(type(a))

a = 10.5

print(type(a))

import datetime

a = datetime.datetime(1984, 4, 30)

print(type(a))

fruits= ['apple','banana','cherry']

print(type(fruits))

# Many values to Multiple variables
# Python allows you to assign values to multiple variavbles in one line

x, y, z = 'a', 2, datetime.datetime(2023,3,22)

print ("x: ", x, " y: - ", y ," z:- ", z)

# One value to Multiple variables
# Python allows you to assign the same value to multiple variables in one line

x = y = z = 'One value to Multiple variables'

print ("x: ", x, " y: - ", y ," z:- ", z)

# Unpack a Collection
# Unpack collectin of values in a list, tuple

x, y, z = fruits
print ("x: ", x, " y: - ", y ," z:- ", z)

# Global variables

varGlobal = 'PAULO' #variable global

def myfunc():
    print("varGlobal: " + varGlobal)

myfunc()

x = "awesome"

def myfunc2():
  x = "fantastic"
  print("Python is " + x)

myfunc2()

print("Python is " + x)

def myfunc3():
  global x
  x = "fantastic"

myfunc3()

print("Python is " + x)

# CASTING
# if you want to specify the data type of a variable, this can be done with casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)