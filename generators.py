#Generators generate one value at a time (memory-efficient): (lazy evaluation)
#Paranthesis are used for generators

l = [2, 3, 4, 5]

gen = (i**2 for i in l)

print(gen)

''' This only creates the generator but does not print the values
To print the values we need to define as follows '''

for j in gen:
    print(j)
    
''' Here printing is done one at a time, first number is printed then another then... by allocating the memory accordingly
So, each time it has only one item '''