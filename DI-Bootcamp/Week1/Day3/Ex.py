def assign_grades(scores_dict):
    grades_dict = {} # Create an empty dictionary to hold the results
    
    for student, score in scores_dict.items():
        if score >= 90:
            grades_dict[student] = "A"
        elif score >= 80:
            grades_dict[student] = "B"
        elif score >= 70:
            grades_dict[student] = "C"
        else:
            grades_dict[student] = "F"
            
    return grades_dict

# --- Testing the function ---
exam_scores = {"Alice": 92, "Bob": 75, "Charlie": 88, "Diana": 55}
final_grades = assign_grades(exam_scores)

print(final_grades)
# Output: {'Alice': 'A', 'Bob': 'C', 'Charlie': 'B', 'Diana': 'F'}
def count_words(text):
    word_counts = {}
    
    # .lower() ensures "The" and "the" are counted as the same word
    # .split() breaks the sentence into a list of individual words
    words_list = text.lower().split()
    
    for word in words_list:
        if word in word_counts:
            word_counts[word] += 1  # If it exists, increment the count
        else:
            word_counts[word] = 1   # If it's new, add it to the dict with a count of 1
            
    return word_counts

# --- Testing the function ---
sentence = "apple banana apple orange banana apple"
result = count_words(sentence)

print(result)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}
def add_to_cart(cart, item, price):
    if item in cart:
        cart[item] += price
        print(f"Updated {item} total.")
    else:
        cart[item] = price
        print(f"Added {item} to cart.")

# --- Testing the function ---
# Our starting cart
my_cart = {"shoes": 50.00, "hat": 15.00}


# Call the function (Notice we don't need to return anything!)
add_to_cart(my_cart, "socks", 5.99)  # Adding a new item
add_to_cart(my_cart, "shoes", 50.00) # Updating an existing item

print(f"\nFinal Cart: {my_cart}")
# Output: {'shoes': 100.0, 'hat': 15.0, 'socks': 5.99}
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Map characters to indices
# Loops through the list and creates {character: index}
disney_users_A = {char: i for i, char in enumerate(users)}
print(f"1. {disney_users_A}")

# 2. Map indices to characters
# Loops through the list and creates {index: character}
disney_users_B = {i: char for i, char in enumerate(users)}
print(f"2. {disney_users_B}")

# 3. Map sorted characters to indices
# We wrap users in sorted() to alphabetize the list before enumerating
disney_users_C = {char: i for i, char in enumerate(sorted(users))}
print(f"3. {disney_users_C}")