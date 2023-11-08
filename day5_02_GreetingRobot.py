import time
timeinhr=time.strftime("%H")

# if(int(timeinhr)>=4 and int(timeinhr)<12):
#     print("Good Morning!") 
# elif(int(timeinhr)>=12 and int(timeinhr)<16):
#     print("Good Afternoon!") 
# elif(int(timeinhr)>=16 and int(timeinhr)<20):
#     print("Good Evening!") 
# else:
#     print("Good Night!")


            #Match case method
Hour=int(timeinhr)

Hour=int(input("Enter the current time in hour : "))
         
match Hour:
    case _ if(4<=Hour<12):
        print("Good Morning!!")
    case _ if(12<=Hour<16):
        print("Good Afternoon!!")
    case _ if(16<=Hour<20):
        print("Good Evening!!")
    case _ if((20<=Hour<=24) or (1<=Hour<4)): 
        print("Good Night!!") 
    case _:
        print("Please Enter the correct time!!")
        
        