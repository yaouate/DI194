#Daily Challenge: Build up a string
#1. Ask for User Input:
phrase = input("Enter a phrase that contain exacltly 10 characters no less and no more. ")
if len(phrase) < 10:
    print("String not long enough.")
elif len(phrase) > 10:
    print("String not long enough.")
elif len(phrase) == 10:
    print("Perfect string.")
    print("the first char is "+phrase[0] +" the last char is "+phrase[9]+".")
    built_phrase = ""
    for char in phrase:
        # Add the current character to our "collector"
        built_phrase += char
        # Print the current state of the built phrase
        print(built_phrase)
#5. Bonus: Jumble the String (Optional)
import random
phrase_list = list(phrase)
# 2. Shuffle the list in place
random.shuffle(phrase_list)
# 3. Join the list back into a single string
jumbled_phrase = "".join(phrase_list)
print(f"Jumbled:  {jumbled_phrase}")