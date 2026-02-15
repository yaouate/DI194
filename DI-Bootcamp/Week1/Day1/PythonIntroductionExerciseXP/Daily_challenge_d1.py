'''Daily Challenge: Build up a string
1. Ask for User Input:

The string must be exactly 10 characters long.
2. Check the Length of the String:

If the string is less than 10 characters, print: "String not long enough."
If the string is more than 10 characters, print: "String too long."
If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
3. Print the First and Last Characters:

Once the string is validated, print the first and last characters.
4. Build the String Character by Character:

Using a for loop, construct and print the string character by character. 
Start with the first character, then the first two characters, and so on, until 
the entire string is printed.
Hint: You can create a loop that goes through the string, adding one character at 
a time, and print it progressively.
'''
phrase = input("Enter a phrase that contain exacltly 10 characters no less and no more. ")
if len(phrase) < 10:
    print("String not long enough.")
if len(phrase) > 10:
    print("String not long enough.")
if len(phrase) == 10:
    print("Perfect string.")
    print("the first char is "+phrase[0] +" the last char is "+phrase[9]+".")
    for phrases in phrase: phrase[0],phrase[1]
    print(phrases)