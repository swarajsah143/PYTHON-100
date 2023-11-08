num=input("Enter the number whose table is to be printed : ")
try:     # Some code that may raise an exception

    for i in range(1,11):
        print(f"{int(num)} X {i} ={int(num)*i}")
except:
    print("Invalid input!!.")
finally:
    print("I am always printed ")
# finally: always gets executed whatever the condition is 
# if statement inside try: will not work then also after that other code will run

print("My name is swaraj")
print("My name is hyper")

