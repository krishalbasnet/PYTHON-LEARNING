list = [1,2,3,4,5]
lis = len(list)
num1 = int(input("Enter the new first data: "))
num2 = int(input("Enter the new last data: "))
list[0]= num1
list[lis-1] = num2
print(list)