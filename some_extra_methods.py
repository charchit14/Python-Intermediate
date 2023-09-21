'''Bitwise Operator
AND &
OR | 
XOR ^
NOT ~
Left Shift <<
Right Shift >>'''

# #Program 1
# a = 2+3j
# print(type(a))


# #Program 2
# import math
# a = math.sin(60)
# print(a)


# #Program 3
# a = ',....,,,,cxv car,,,,,xxxx'
# print(a.strip('.,vcx'))


# #Program 4
# a = 'Man parena vane maya I am very sorry sorry'
# print(a.split())


# #Program 5
# a = "There is a %s and it has %d %s"
# s1 = 'ghost'
# d1 = 7
# s2 = 'eyes'
# final = a % (s1,d1,s2)
# print(final)


# #Program 6
# a = "There is a %s and it has %.2f %s"
# s1 = 'ghost'
# d1 = 7
# s2 = 'eyes'
# final = a % (s1,d1,s2)
# print(final)


# #Program 7
# a = "There is a {2} and it has {0} {1}" #2, 1, 0 determine the order of value from (s1,d1,s2)
# s1 = 'ghost'
# d1 = 7
# s2 = 'eyes'
# final = a.format(s1,d1,s2)
# print(final)


# #Program 8
# s1 = 'ghost'
# d1 = 7
# s2 = 'eyes'
# a = f"There is a {s1} and it has {d1} {s2}"
# print(a)


# #Program 9
# n = input("Enter name: ")
# p = input("Enter PIN: ")
# print()
# l = len(p)
# show = ("X" * (len(p) - 2)) + p[-2:]
# print(f"Your name is: {n}")
# print(f"Your PIN is: {show}")


# #Program 10
# list_1 = [1, 3, 43, 23]
# list_2= [12, 12, 32, 14]
# c = list_1 + list_2 #Concatenating two lists
# d = sum(list_1) #Sum of all elements of list
# e = [i+j for i,j in zip(list_1,list_2)] #Adding elements of two lists
# print(c)
# print(d)
# print(e)


# #Program 11
# list = [2,4,5]
# result = 1
# for i in list:  
#     result = result * i
# print(result)


# #Program 12 (Dictionary can be created this way as well)
# a = dict(b=99, c='cat')
# print(a)
# print(type(a))
# a['b'] = 100
# print(a)


# Program 13
# zoo = {'Zebra', 'Lion', 'Tiger', 'Elephant'}
# animals = {'Lion', 'Tiger', 'Dog'}
# if animals.issubset(zoo):
#     print("Let's Go")
# else:
#     print("Nah! Mate")


# Program 14
# l1 = [2,3,4]
# l2 = l1
# op = 'Shallow copy' if l2 is l1 else 'Deep copy'
# print(op)


# Program 15
# st_m = {
#     "Student1": 50,
#     "Student2": 60,
#     "Student3": 70,
#     "Student4": 80
# }
# for i in st_m:
#     print("The mark of {} is {}".format(i,st_m[i]))