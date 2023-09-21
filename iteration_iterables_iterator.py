# Iteration, iterable, and iterator

list = [1,2,3,4]
for i in list:
  print(i)

# Here, list is iterable
# The process of taking each item one after another is iteration
''' Iterator is an object that supports iterator protocol
(i.e. saves current state and returns next item when next() function is used) '''

print()

my_iterator = iter(list)
item = next(my_iterator)
print(item)

''' Here, 'my_iterator' is created from the list, and then 'next()' is used to get the next element from the iterator, 
which would be the first element of the list (in this case, 1)
And, if we write the same code (code with 'next' keyword) and print it again then it will give us the second element (2 in this case)'''

# 'iter' and 'next' are the keywords here