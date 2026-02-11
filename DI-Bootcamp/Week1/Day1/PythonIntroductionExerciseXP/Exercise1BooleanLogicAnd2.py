#exercise 1
first = "Hello World"
# This is a comment.
print("I AM A COMPUTER!")
if 1<2 and 4>2:
    print("Math is fun.")
nope = None
if 2>3 and 2<3:
     print("Math is not fun.")
else: print("Math is realy not fun, This calculation is False")
print (len ("What's my length?"))
test= int("1000")
print(type(test))
print (str(4)+"real")
print (3 * "cool")
print("ZeroDivisionError: division by zero")
print (type([]))
name=input("write your name please.")
print (name)
user_input=input("write a positive number.")
number = float(user_input)
if number > 0:
    print ("That number is greater than 0!")
if number < 0:
    print ("That number is less than 0!")
if number == 0:
    print ("You picked 0!")
index = "apple"
print (index.find('l'))
print ("y" in "xylophone")
string = "my_string"
print (string.islower())

#Exercise 2
humanYears=10
catYears1=15
catYears2=15+9
catYears3andMore=15+9+(4*(humanYears-2))
dogYears1=15
dogYears2=15+9
dogYears3andMore=15+9+(5*(humanYears-2))
if humanYears==1:
    print (humanYears,catYears1,dogYears1)
if humanYears==2:
    print (humanYears,catYears2,dogYears2)
if humanYears>2:
    print (humanYears,catYears3andMore,dogYears3andMore)