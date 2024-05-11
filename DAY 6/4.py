#add a number until the user terminates the program
ch ="Y"
while ch=='Y' or ch=='y':
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1+num2)
    ch =  input("Enter Y or y to rerun the program or click any other key to terminate: ")