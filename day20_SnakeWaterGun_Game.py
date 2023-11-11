import random
win=0
tied=0
lost=0
topic="Welcome To Snake Water Gun Game"
print(topic.center(50))
print()
print("You have 10 choice\n")
for i in range(10):
  computer=random.randint(0,2)
 # print(computer) Its Computer's Choice
  print(f"This is chance no.{i+1} \n")

  User=int(input("0 for snake\n1 for Water\n2 for Gun\n\nEnter your Answer : "))

  if User==0 or User==1 or User==2:
   def Choice(computer,user):
     if computer==user:
        return 0
     elif computer==0 and user==1:
        return -1
     elif computer==1 and user==2:
        return -1
     elif computer==2 and user==0:
        return -1
     else:
        return 1
   ans=Choice(computer,User)
   if ans==0:
    print(f"\nComputer choice : {computer}")
    print(f"User choice : {User}")
    print(" Game Tied\n")
    tied=tied+1
   elif ans==-1:
    print(f"\nComputer choice : {computer}")
    print(f"User choice : {User}")
    print("You lost\n")
    lost=lost+1
   elif ans==1:
    print(f"\nComputer choice : {computer}")
    print(f"User choice : {User}")
    print("You won\n")
    win=win+1
  else:
    print("\nInvalid Input.You lost your chance.\n")
    
print(f"{1}) You have tied {tied} times")  
print(f"{2}) You have won {win} times")  
print(f"{3}) You have lost {lost} times")
if win>lost:
 end_wish="\nCongratulation you played well!" 
 print(end_wish.center(50))
elif  lost>win:
    end_wish="\nSorry! Better luck next time."
    print(end_wish.center(50))
elif win==lost:
    end_wish="\nIt's a tie!"
    print(end_wish.center(50))



