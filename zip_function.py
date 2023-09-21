#Use of zip function: to combine multiple list in single 'for' loop

std = ["A", "B", "C", "D"]
mrk = [50, 60, 70, 80]

for i,j in zip(std,mrk):
    print(f"{i}: {j}")