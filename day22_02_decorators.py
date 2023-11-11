# Decorator decorates the initial function and returns .It  takes another function as an arguments

def greet_decorator(function):
    def inner1(*args, **kwargs):
        print("This is before main function ")
        function(*args,**kwargs)#calling main function
        a=3
        print(("This is after main function \n\n"))
    return inner1

@greet_decorator
def sum_three_numbers(a, b,c):
    # print("Inside the function")
   print(a + b+c)
sum_three_numbers(1,2,3)

        #finding product by decorating 
@greet_decorator
def product(c,d,e):
    print(c*d*e)
product(3,4,2)
