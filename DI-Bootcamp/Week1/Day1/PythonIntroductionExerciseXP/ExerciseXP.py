# Exercise 1: Hello World
print ("Hello world\n"*4)
#Exercise 2: Some Math
print ((99**3)*8)
#Exercise 3: What is the output?
#>>> 5 < 3 False
#>>> 3 == 3 True
#>>> 3 == "3" True
#>>> "3" > 3 type Error
#>>> "Hello" == "hello" False
#Exercise 4: Your computer brand
computer_brand = "Dell"
print ("I have a "+ computer_brand + " computer.")
# Exercise 5: Your information
name= "Yohai"
age= 32
shoe_size= 44
info = "My name is "+name+", and i'm " + str(age) + " old. My foot size is " +str(shoe_size) + "."
print (info)
#Exercise 6: A & B
a= 6
b= 5
if a>b:
    print ("Hello World")
#Exercise 7: Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
#Exercise 8: What’s your name?
name = input("Enter youre name: ")
if name == "yohai":
    print("You have the same name as the code writer")
else:
    print("Thanks")
#Exercise 9: Tall enough to ride a roller coaster
size = int(input("Enter your size in centimeter: "))
if size > 145:
    print("Tall enough to ride.")
else:
    print("Need to grow some more to ride.")