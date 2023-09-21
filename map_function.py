# Map function

l1= [2,3,4]
l2= [6,1,0]
add_func = lambda x,y: x+y
result = map(add_func, l1, l2)
print(list(result))