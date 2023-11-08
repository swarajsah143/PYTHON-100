num=int(input("Enter the number between 10 and 20 : "))
if num<10 or num>20:
    raise ValueError("Value must be between 10 and 20")
# here we raise the error by ourself to stop the further program 
else:
    print(f"{num} is the accurate value")
    
    # program which doesnot display error on entering quit or number between 5 and 10

n=input("Enter 'quit' to not get an error or enter num betn 5 and 10 : ")
if n=="quit":
    print("No error")

elif int(n)<5 or int(n)>10:
    raise ValueError("Value must be between 5 and 10")
print(f"{int(n)} is the value betn 5 and 10")

