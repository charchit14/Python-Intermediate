#Demonstration of shallow copy

list1 = [2,4,5,'cat']
list2 = list1  #Creating a shallow copy
print(f"Before Change (L1): {list1}")
print(f"Before Change (L2): {list2}")

print()

#Now changing the value of list2
list2[3] = "dog"
print(f"After Change (L2): {list2}")
print(f"After Change (L1): {list1}")

'''Hence, in shallow copy both list's items are changed because they point to the same memory location'''

#To check whether two are deep copy or shallow copy of one another
#Will return 'True' if shallow copy else returns 'False' for deep copy
#This is called 'identity operator'  
print(list1 is list2 )