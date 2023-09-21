# Decorators are used to change the functionality of the function without changing its body 

# #Demonstration 1
# def greet(word):

#     def say_hi(name):
#         return f"Hi {name}"
    
#     def say_hello(name):
#         return f"Hello {name}"
    
#     if word == 'hi':
#         return say_hi
    
#     if word == 'hello':
#         return say_hello
    
# pass_value = greet('hi')
# result = pass_value('Boy')
# print(result)


#Demonstration 2
def decorator(func):
    def wrapper(x):
        result = func(x)
        print("Hey Jude")
        # You can add additional functionality here if needed
        return result
    return wrapper

@decorator
def incr(x):
    return x + 1

x = 4
y = incr(x)
print(y)