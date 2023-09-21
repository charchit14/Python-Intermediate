#DEMONSTRATION 1
# Serializing i.e. transforming to store in the disk
# list1 = [1, 3, 5]
# list2 = [7, 9, 11]
# l = list1 + list2
# import pickle
# with open("E:\\Python Course\\Python Course - I\\My Work\\list.pkl", "wb") as f:
#     pickle.dump(l,f)

# Here, the mode 'wb' means 'write binary' which is the correct way to write binary data like pickled objects to a file


#DEMONSTRATION 2
# Deserializing
# import pickle
# with open("E:\\Python Course\\Python Course - I\\My Work\\list.pkl", "rb") as f:
#     load = pickle.load(f)
# print(load)
# After printing we will get the dumped file where the rsulting list after concatenation was stored


#DEMONSTRATION 3
#Dumping in the form of string
# import pickle 
# l = [2,3,4,1,6,7,9,8]
# st = pickle.dumps(l)    #The 's' in dumps denotes the string
# print(l)
# print(st)

# The pickle standard is not readable to human so we load it and print
# print(pickle.loads(st))