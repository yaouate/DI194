# Exercise 1: Favorite Numbers
my_fav_numbers = {7, 13, 21}
#Add two new numbers to the set
my_fav_numbers.add(42)
my_fav_numbers.add(100)
#Remove the last number you added (100)
my_fav_numbers.remove(100)
print(my_fav_numbers)
friend_fav_numbers = {13, 50, 88, 7}
#Combine them into a new set called our_fav_numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
#2
my_tuple = (1, 2, 3)
# my_tuple.append(4)  <-- This will cause an AttributeError
#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana"
basket.remove("Banana")
#Remove "Blueberries"
basket.remove("Blueberries")
#Add "Kiwi" to the end
basket.append("Kiwi")
#Add "Apples" to the beginning (index 0)
basket.insert(0, "Apples")
#Count how many times "Apples" appear
apple_count = basket.count("Apples")
print(f"Apples appear {apple_count} times.")
#Empty the list
basket.clear()
#Print final state
print(basket)
#4
# Integer (int): Whole numbers without a fractional part (e.g., 2, -5, 100). They are used for counting discrete items.
# Float (float): Short for "floating-point number." These represent real numbers and always contain a decimal point (e.g., 1.5, -0.25, 3.0).
mixed_list = []
current_val = 1.5

while current_val <= 5:
    # If the number is a whole number (like 2.0), 
    # we convert it to an int to match your requested sequence.
    if current_val % 1 == 0:
        mixed_list.append(int(current_val))
    else:
        mixed_list.append(current_val)
    
    current_val += 0.5

print(mixed_list)
#5
# range(1, 21) starts at 1 and stops before 21
for i in range(1, 21):
    print(i)
# Start at 2, stop at 21, jump by 2
for i in range(2, 21, 2):
    print(i)
#6
while True:
    name = input("Please enter your name: ")

    # Check if the name contains digits or is too short
    if name.isdigit():
        print("Error: A name cannot be just numbers.")
    elif len(name) < 3:
        print("Error: Your name must be at least 3 characters long.")
    else:
        # If it passes both checks, it's a proper name
        print("Thank you!")
        break  # This exits the loop
#7
# 1. Ask for multiple fruits and store them as a list
fav_fruits_input = input("Enter your favorite fruits (separated by spaces): ")
fav_fruits_list = fav_fruits_input.split()

# 2. Ask for a specific fruit to check
choice = input("Enter the name of any fruit: ")

# 3. Check if the choice is in the list
if choice in fav_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
#8
toppings = []
base_price = 10.0
topping_price = 2.50

print("Welcome to the Pizza Order System! (Type 'quit' when you are done)")

while True:
    entry = input("Enter a topping: ").lower()
    
    if entry == 'quit':
        break
    
    # Add the topping to our list and confirm to the user
    toppings.append(entry)
    print(f"Adding {entry} to your pizza.")

# Calculate the final price
total_price = base_price + (len(toppings) * topping_price)

# Final summary
print("\n--- Your Order Summary ---")
if toppings:
    print(f"Toppings: {', '.join(toppings)}")
else:
    print("Toppings: Plain cheese (No extra toppings)")

print(f"Total Cost: ${total_price:.2f}")
#9
# 1. Initialize our total cost variable
total_cost = 0

# 2. Ask how many family members are buying tickets
try:
    num_people = int(input("How many people are in your family? "))

    # 3. Loop through each person
    for i in range(num_people):
        age = int(input(f"Enter the age of person {i + 1}: "))
        
        # 4. Apply the pricing rules
        if age < 3:
            print("Ticket is free.")
            total_cost += 0
        elif 3 <= age <= 12:
            print("Ticket cost is $10.")
            total_cost += 10
        else:
            print("Ticket cost is $15.")
            total_cost += 15

    # 5. Print the final result
    print(f"\nThe total ticket cost for your family is: ${total_cost}")

except ValueError:
    print("Please enter a valid number for age and quantity.")
#bonus
# 1. Collect ages from the group
raw_input = input("Enter the ages of the teenagers (separated by spaces): ")
# Convert the string input into a list of integers
all_ages = [int(age) for age in raw_input.split()]

# 2. Filter the list (Remove those outside the 16-21 range)
# We keep the person if their age is >= 16 AND <= 21
attendees = [age for age in all_ages if 16 <= age <= 21]

# 3. Print the final results
print("\n--- Movie Entry Summary ---")
print(f"Original group ages: {all_ages}")
print(f"Final list of attendees: {attendees}")
print(f"Total allowed: {len(attendees)} people")