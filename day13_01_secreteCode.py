import random
import string
# Generate a random letter
random_letter1 = random.choice(string.ascii_uppercase)
random_letter2 = random.choice(string.ascii_lowercase)
random_letter3 = random.choice(string.ascii_lowercase)
random_letter4 = random.choice(string.ascii_lowercase)
random_letter5 = random.choice(string.ascii_lowercase)
random_letter6 = random.choice(string.ascii_lowercase)

value=int(input("Enter 1 to code and 0 to decode : "))
str=input("Enter Your messege : ")
words=str.split(" ")
nstr=[]
if(value==1):
 for word in words:
    if len(word)>=3:
       nword=random_letter1+random_letter2+random_letter3+word[1:]+word[0]+random_letter4+random_letter5+random_letter6
       nstr.append(nword)
    else:
        nstr.append(word[::-1])
elif(value==0):
    for word in words:
        if len(word)>=3:
            nword=word[-4]+word[3:-4]  # last bata 3 wata xore vane "-4" is the position of 4th last which is initial letter of real word and from 3 index to -4 is the remaining letter
            nstr.append(nword)
        else:
            nstr.append(word[::-1])
            

print(" ".join(nstr)) 
#Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'



