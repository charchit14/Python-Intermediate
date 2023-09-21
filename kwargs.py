#Demonstration of 'Keyword Arguments' (kwargs)
#The function recieves 'kwargs' as a 'dictionary of unordered items'

# #Program 1
# def any_func(a, b, **kwargs):
#     print("Value of a is: ", a)
#     print("Value of b is: ", b)
#     print("kwargs is: ", type(kwargs))
#     print("Value of kwargs is: ", kwargs)

# # Case I 
# # any_func(3, 2)

# # Case II
# any_func(3, 2, Company = 'codavatar', Position = 'Backend', ID = 999)

# # Program 2
# def player_role(**kwargs):
#     for p,r in kwargs.items():
#         print(f"The role of {p} is {r}")

# player_role(Haaland = "Striker", KDB = "Mid-fielder", Dias = "Defender")