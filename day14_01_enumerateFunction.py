lst=[11,22,33,44,55,66]
for index,num in enumerate(lst):
        print(f"{index} is the index of {num} ") 
print("\n")
for index,num in enumerate(lst,start=2):# starts with index=2
    print(f"{index} is the index of {num} ") 
    
print("\n")
    
lst=[11,22,33,44,55,66]   
for tup in enumerate(lst):
    print(tup)
    # enumerate with single variable acts as a tuple in which index becomes 1st value and variable becomes 2nd value
