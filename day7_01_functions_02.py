# def sum(a=2,b=4):
#     a=5
#     b=6
#     print("the sum is ",a+b)
# sum(2,3)
    #Priority is given to value inside main module then function calling  parameters then function defining
    
         #tuple type variable

def average(*numbers):
    print(type(numbers))#tuple type
    sum=0
    for i in numbers:#value of i is equal to value stored inside numbers
        sum=sum+i
    print(numbers)
    print("the average is : ",sum/len(numbers))
average(12,11,9,15,13)


     #Dictionary type variable
     
def name(**names):
    print("\n",type(names))
    print(names)
    print("Hello,", names["fname"], names["mname"], names["lname"])
name(mname = "Hyper", lname = "Sah", fname = "Swaraj")

     #Return statement

def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  # return 7   priority goes to first Return
  return sum / len(numbers)
c = average(5, 6, 7, 1)
print(c)
 # In Return,The value under return goes in the variable of callinf function and then gets printed.
     
     #Another example of return 
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))







