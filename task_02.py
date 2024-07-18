print("*************** WELCOME THE SIMPLE CALCULATOR *****************")
print("1 : Add")
print("2 : Substract")
print("3 : Multiply")
print("4 : Devide")

choices = int(input("Choose an operation : "))
res = 0

if (choices in [1, 2, 3, 4]) :
    n1 = float(input("Enter the 1st number : "))
    n2 = float(input("Enter the 2nd number : "))

    if (choices == 1) :
        res = n1 + n2
    elif (choices == 2) :
        res = n1 - n2
    elif (choices == 3) :
        res = n1 * n2
    elif (choices == 4) :
        res = n1 // n2

else:
    print("Invalid operation choice. Please try again.")

print("The Final result of the operation is : {}".format(res))