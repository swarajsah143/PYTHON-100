
      #Fibonacci series by recursion 
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
         
n=int(input("Enter a positive integer : "))
for i in range(n):
    print(fibo(i))    
       # factorial program

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
n = int(input("Enter a number to find its factorial :"))
print(fac(n))






