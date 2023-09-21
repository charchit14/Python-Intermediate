#Using 'setdefault' in dictionary

info = {
    "Name": "Kallu Laal",
    "Age": 19,
    "Address": "Mahottari"
}

'''This will set the default value for Hooby to Sleeping if it doesn't exist
here, hooby is key and sleeping is value'''
info.setdefault("Hobby", "Sleeping")    
print(info)
info.setdefault("Hobby", "Eating") #This has no effect as value for key 'Hobby' already exist
print(info)