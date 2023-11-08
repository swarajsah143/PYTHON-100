print("                        This is a Hyper's Calculator\n\n    ")



num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))

print("\nPress '1' for Addition")
print("Press '2' for Subtraction")
print("Press '3' for Division")
print("Press '4' for Multiplication\n")

user_input=int(input("Enter any no. from 1 to 4 : "))

if user_input==1:
    print("\nThe sum of ",num1,"and",num2,"is ",num1+num2)

elif user_input==2:
    print("\nThe sub of ",num1,"and",num2,"is ",num1-num2)

elif user_input==3:
    print("\nThe div of ",num1,"and",num2,"is ",num1/num2)

elif user_input==4:
    print("\nThe mult of ",num1,"and",num2,"is ",num1*num2)

else:
    print("\nInvalid input")




