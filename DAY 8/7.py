#length of list without using len()

def length(data):
    leng = 0
    for i in enumerate(data):
        leng+=1
    return(leng)
list = [1,2,3,4,5,7,"Held"]
print(length(list))