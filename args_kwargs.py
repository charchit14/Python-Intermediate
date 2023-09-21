#Args and Kwargs together 

def any_func(a, b, c = 'Cow', d = 100, *args, **kwargs):
    print("Value of a is: ", a)
    print("Value of b is: ", b)
    print("Value of c is: ", c)
    print("Value of d is: ", d)
    print("Value of args is: ", args)
    print("Value of kwargs is: ", kwargs)

any_func(1, "Value of b", "Value of c", 12, 0, 1, 2, Name = "Ghost")

#Here defaault value of 'c' and 'd' will be printed only if no arguemet is passed in function call