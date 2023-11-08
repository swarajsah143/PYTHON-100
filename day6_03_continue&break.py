  # continue--- skip the itteration

for i in range(10):
    if i+1==5:
        continue
    print("5 x",i+1,"=",5*(i+1))
    
print("\n")
    # break---- skip the loop
    
for i in range(10):
    if i+1==5:
        break
    print("5 x",i+1,"=",5*(i+1))
    
   # calculate factorial of given number 
    
num=int(input("Enter the no. whose factorial is to be determined : "))
facNo=num
fac=1
for j in range(num):
    fac=fac*num
    num=num-1
print("The factorial of ",facNo,"is",fac)