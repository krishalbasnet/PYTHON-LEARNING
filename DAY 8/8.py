# Print the highest value from a list
LST = [1,41,5,8,33,21,90]
highest = LST[0]
for i,s in enumerate(LST):
    if(highest<LST[i]):
        highest = LST[i]
print(highest)