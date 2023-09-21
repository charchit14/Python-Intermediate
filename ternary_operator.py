# Ternary operator: Using 'if-else' in a single line

# #Program 1
# a = {
#     'Uncle': 40,
#     'Aunt': 39,
#     'Boy': 21,
#     'Girl': 17
# }

# result = 'Okay!' if a['Girl'] > 18 else 'FBI'
# print(result)


#Program 2
age = int(input('Enter your age: '))
check = "You can vote" if age >= 18 else f"Come back after {18 - age} years"
print(check)