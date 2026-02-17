#Exercise : List #1
[print(val) for val in [1, 2, 3, 4]]
print([val * 20 for val in [1, 2, 3, 4]])
names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters) # Output: ["E", "T", "M"]
evens = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(evens) # Output: [2, 4, 6]
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = [val for val in list1 if val in list2]
print(intersection) # Output: [3, 4]
words = ["Elie", "Tim", "Matt"]
reversed_lower = [word[::-1].lower() for word in words]
print(reversed_lower) # Output: ['eile', 'mit', 'ttam']
str1 = "first"
str2 = "third"
common_letters = [char for char in str1 if char in str2]
print(common_letters) # Output: ["i", "r", "t"]
div_by_12 = [num for num in range(1, 101) if num % 12 == 0]
print(div_by_12) # Output: [12, 24, 36, 48, 60, 72, 84, 96]no_vowels = [char for char in "amazing" if char not in "aeiou"]
no_vowels = [char for char in "amazing" if char not in "aeiou"]
print(no_vowels) # Output: ['m', 'z', 'n', 'g']
matrix = [[i for i in range(3)] for j in range(3)]
print(matrix) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
grid = [[i for i in range(10)] for _ in range(10)]
# To see it formatted nicely in your console:
for row in grid:
    print(row)