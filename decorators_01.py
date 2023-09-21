#Program 1

# def greet (fx):
#     def mfx():
#         print("Good Night")
#         fx()
#         print("Chill Dude")
#     return mfx

# @greet
# def hello():
#     print("Hello World")

# hello()

# '''Here, @greet is used as a decorator on 'hello()' function
# So, when we call 'hello' function, at first, it goes to 'greet' because of decorator
# Then, inside that greet 'Good Night' will execute then,
# 'Hello World' from 'hello' function will execute because after printing 'Good Night'
# it calls the passed function 'fx' (fx is passed to greet) which is 'hello' in this case
# Finally, 'Chill Dude' will be printed'''


#Program 2
# def greet (fx):
#     print("Good Night")
#     fx()
#     print("Chill Dude")
#     return fx

# @greet
# def hello():
#     print("Hello World")

# hello()


#Program 3 
# def greet (fx):
#     def mfx(*args):
#         print("Good Night")
#         fx(*args)
#         print("Chill Dude")
#     return mfx

# @greet
# def add(a,b):
#     print(a+b)

# add(2,4)