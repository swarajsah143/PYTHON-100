lst1 = [1,2,8,3,5,"Hyper",True,None]
print(lst1)
print(lst1[0])
print(lst1[1])
print(lst1[2])
print(lst1[3])
print(lst1[4])
print(lst1[5])
print(lst1[6])
print(lst1[7])
print("\n")
 #List can store different datatypes variables


if 12 in lst1:   # By using "in" we can check the value is in the list or not
    print("Yes")
else:
    print("No")

if "Hyper" in lst1:   
    print("Yes")
else:
    print("No")

print("\n")

lst2 = ["Red", "Green", "Blue"]
print(lst2)
print(lst2[0])
print(lst2[1])
print(lst2[2])
print("\n")

lst1 = [1,2,8,3,5,"Hyper",True,None]
print(lst1[-5]) #Negative index
print(lst1[len(lst1)-5]) #Postive index
print(lst1[8-5])
print(lst1[3])
    # All print same value
    
    #LIST COMPREHENSION

# List comprehension allows us to create a new list based on an existing one. It's a concise way of creating lists and it’

            # List comprehension example
squares = [x**2 for x in range(10)] #x**2 is the condition 
print(squares)

              #another example
fruits = ['apple', 'banana', 'cherry',"Ape"]
numbers = [number for number in fruits if len(number)>4]
print(numbers)
# here, "Ape" is not included becoze its length is less than 4

            # another example 

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

