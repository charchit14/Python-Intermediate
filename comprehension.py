#List comprehension
#Squaring each element in list and printing (under 3 different condition)
li = [2,3,1,4]
l2 = [i**2 for i in li]
l3 = [i**2 for i in li if i>3]
l4 = [i**2 if i>3 else i**3 for i in li]
print(l2)
print(l3)
print(l4)

print()

#Set comprehension (curly bracket is used for set comprehension)
ls = [1,2,1,1,1,2,3,4,4,4,4,2,2]
s = {i for i in ls}
print(s)

print()

#Dictionary comprehension
#Print items in key and square of their numbers in values
ld = [1,2,3,4]
d = {i:i**2 for i in ld}
print(d)