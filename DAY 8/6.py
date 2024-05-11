list = [1,2,3]
def swap(swalist):
    listl = len(swalist)
    temp = swalist[0]
    swalist[0] = swalist[listl - 1 ]
    swalist[listl - 1] = temp
    print(swalist)       
swap(list)
    