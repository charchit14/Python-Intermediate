#Demonstration of Arbitary function (*args)
#The function recieves 'args' as a 'tuple of ordered items'

# #Program 1 
# def any_func(a,b, *args):
#     print("Value of a is: ", a)
#     print("Value of b is: ", b)
#     print(f"args is: {type(args)}")
#     print("Value of args is: ", args)

# #Case I
# # any_func(2, 3)

# #Case II
# any_func(2, 3, 4, 6, 1, 7)

# #Program 2
# def cal_max(*args):
#     return max(*args)

# result = cal_max[2,9,1,6]
# print(f"Maximum number is: {result}")