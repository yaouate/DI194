# Exercise 1 : Hello World-I love Python
print ("Hello world\n"*4 + "I love python\n"*4)
#Exercise 2:What is the Season ?
season = int(input("Enter a month number betwen 1 to 12: "))
if season >=3 and season <6 :
    print("this is Spring")
elif season >=6 and season <9 :
    print("this is Summer")
elif season >=9 and season <12 :
    print("this is Autumn")
elif season ==12 or season ==1 or season == 2 :
    print("this is Winter")
else:
    print ("you did not enter a number betwen 1 and 12")