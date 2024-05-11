#recursion to find factorial
num = int(input("Enter the number: "))
fact = num
def mul(a):
    return fact *(a-1)
while num>1:
    fact = mul(num)
    num=num-1
print(fact)