num = int(input("Enter the number:"))
sum = 0
while num!=0:
    sum = sum+num%10
    num = num/10
    num = int(num)
print("The sum is ",sum)