num1=int(input("Enter the number : "))
if(num1==0):
    print("\nNeutral number")
elif(num1>0 and num1!=999 and num1!=333):
    print("\nPositive number") #before print,there is space which is known as indent.
elif(num1==999 or num1==333):
    print("\nSpecial number")    
else:
    print("\nNegative number")    
    
    # nested....if...elif...else
     
num2=int(input("\nEnter the another number :"))
if(num2==0):
    print("\nNeutral number ")
elif(num2>0):
    if(num2>0 and num2<=20):
        print("\nNumber is between 1-20")
    elif(num2>20 and num2<=40):
        print("\nNumber is between 20-40")
    else:
        print("\nNumber is above 40")
else:
    print("\nNegative number")

                

        