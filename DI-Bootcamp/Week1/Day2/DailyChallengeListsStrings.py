# Challenge 1
# 1. Get user input
word = input("Enter a word with consecutive duplicates: ")

# 2. Initialize a result string with the first character
# (We start with an empty string to be safe)
clean_word = ""

# 3. Loop through the word
for char in word:
    # If clean_word is empty OR the current character is different 
    # from the very last character we added...
    if len(clean_word) == 0 or char != clean_word[-1]:
        clean_word += char

# 4. Print result
print(f"Modified string: {clean_word}")

#Challenge 2
# 1. Get user input
word = input("Enter a word with consecutive duplicates: ")

# 2. Initialize a result string with the first character
# (We start with an empty string to be safe)
clean_word = ""

# 3. Loop through the word
for char in word:
    # If clean_word is empty OR the current character is different 
    # from the very last character we added...
    if len(clean_word) == 0 or char != clean_word[-1]:
        clean_word += char

# 4. Print result
print(f"Modified string: {clean_word}")