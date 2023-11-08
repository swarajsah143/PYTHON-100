x=1
print(f"This is global variable {x}")

def var():
    # x=2
    # print("This is local variable {x}")
    global x # If we change x under global x then value changes globally 
    x = 3
    
    print("\nNow x is changed to global variable ")
var()
print(x)