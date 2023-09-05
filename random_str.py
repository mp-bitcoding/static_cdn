import random

# List of strings
string_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Get 2 random strings from the list without duplicates
random_strings = random.sample(string_list, 2)

print(random_strings)
