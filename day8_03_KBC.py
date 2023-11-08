# Amount=0
# print("Which one among them is a domestic animal ?\n")
# lst1=("Leopard","Tiger","Cat","Lion")
# print(lst1,"\n")
# ans1=str(input("Enter the answer : "))
# if ans1==lst1[2]:
#     print("Well done! This is correct")
#     Amount=Amount+1000
# else:
#     print("Sorry, that's incorrect. The correct answer was ",lst1[2])
print("Welcome to KBC presented by Swaraj".center(60))
name=str(input("\n\nPlease enter your name Sir! "))
point=("1000","3000","5000","10000")
points=0

que1="Which one among them is a domestic animal?"
que2="Which one among them is a Wild animal ?"
que3="Which one among them is a Pet animal ?"

que=(que1,que2,que3)
ans1=("Cat","Tiger","Leopard","Lion")
ans2=("Cat","Lion","Rabbit","Dog")
ans3=("Tiger","Lion","Dog","Wolf")
ans=(ans1,ans2,ans3)
for i in range(3):
    print("\n",i+1,".",que[i],"\n")
    print(ans[i])
    ans_user=str(input("Enter your ans :"))
    if ans_user==ans[i][i]:
        print("\nWell done! This is correct answer.")
        points=point[i]
    else:
        print("\nOops! This is incorrect answer.")
        if i==0:
            print("\nYou havenot scored a single point")
        else:
            points=point[i-1]
        break
print("\nYour scored point is : ",points)
print("\nThanks,",name,"for playing !")

    
