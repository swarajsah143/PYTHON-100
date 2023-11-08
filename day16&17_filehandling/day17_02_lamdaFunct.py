# Note: lambda function is an anonymous function which means it doesnot require any name to define

# f=lambda x,y,z:(x+y+z)/3 # inline function where x,y,z are parameters 
# print(f(1,2,3)) # gives average




def apply(fx,value):
    return 2+fx(value)  #2+ 64(cube of 4)
# example of function inside function.

cube=lambda a:a**3
print(apply(cube,4))

# print((lambda a:a**3)(2))  it direct gives cube of 2


