### 🌟 Exercise 1: Converting Lists into Dictionaries


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Using zip() to pair elements, then dict() to convert them into a dictionary
result_dict = dict(zip(keys, values))

print(result_dict)

### 🌟 Exercise 2: Cinemax #2


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
        
    print(f"{name.capitalize()}'s ticket is ${price}")
    total_cost += price

print(f"\nThe total cost for the family is ${total_cost}")

###**Bonus Part: User Input**

user_family = {}
total_cost = 0

print("--- Welcome to Cinemax Ticket Calculator ---")
print("(Type 'quit' as the name when you are finished adding members)")

while True:
    name = input("Enter family member's name: ")
    if name.lower() == 'quit':
        break
        
    age_input = input(f"Enter {name}'s age: ")
    
    # Ensuring the age input is a valid number
    if age_input.isdigit():
        user_family[name] = int(age_input)
    else:
        print("Please enter a valid number for age.")

print("\n--- Receipt ---")
for name, age in user_family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
        
    print(f"{name.capitalize()}'s ticket is ${price}")
    total_cost += price

print(f"\nTotal Cost: ${total_cost}")

### 🌟 Exercise 3: Zara


# 1. Create the dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# 2. Change the value of number_stores to 2
brand["number_stores"] = 2

# 3. Print a sentence describing Zara's clients
clients = ", ".join(brand["type_of_clothes"][:3]) # Just taking men, women, children
print(f"Zara produces clothing for {clients}.")

# 4. Add a new key country_creation
brand["country_creation"] = "Spain"

# 5. Check if competitors exists and add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6. Delete the creation_date key
brand.pop("creation_date") 
# del brand["creation_date"] also works

# 7. Print the last item in international_competitors
print(f"Last competitor: {brand['international_competitors'][-1]}")

# 8. Print the major colors in the US
print(f"US major colors: {', '.join(brand['major_color']['US'])}")

# 9. Print the number of keys
print(f"Number of keys: {len(brand)}")

# 10. Print all keys
print(f"Dictionary keys: {list(brand.keys())}")


# --- BONUS ---
more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000
}

# Merging dictionaries using update()
brand.update(more_on_zara)

print("\n--- After Update ---")
print(f"Updated number of stores: {brand['number_stores']}")
# Note: update() overrides existing keys. So number_stores goes from 2 back to 10000.

### 🌟 Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Characters to their indices
# enumerate(users) gives pairs of (0, "Mickey"), (1, "Minnie"), etc.
disney_dict_1 = {character: index for index, character in enumerate(users)}
print("Result 1:", disney_dict_1)

# 2. Indices to characters
disney_dict_2 = {index: character for index, character in enumerate(users)}
print("Result 2:", disney_dict_2)

# 3. Sorted characters to their indices
# We sort the list first, then enumerate it
sorted_users = sorted(users)
disney_dict_3 = {character: index for index, character in enumerate(sorted_users)}
print("Result 3:", disney_dict_3)
