str = input("Enter the text: ")
test = "  " in str
if test:
    print("There is double space.")
else:
    print("There is no double space.")