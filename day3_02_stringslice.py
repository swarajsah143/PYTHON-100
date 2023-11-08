name="Swaraj"
length=len(name)
print(length,"\n")
print(name[0:3]) # upto 3rd character .Including 0 but not 3 as array 0,1,2,3,4,5 

print(name[0:6]) # upto 6th character

print(name[1:6]) # from 2nd character to 6th.Including 1 but not 3 as array 0,1,2,3,4,5 

print(name[:3])  # upto 3rd character,python automatically understands the initial postion

print(name[:]) # prints all character

print(name[-3])   # third last character of string
print(name[-1])   #  last character of string

print(name[0:-3]) # It means  0 to len(name)-3

print(name[-2:-4]) # 6-2=4 to 6-4=2 .  4 to 2 is not possible.
print(name[-4:-1]) #6-4=2 to 6-1=5. [2,5] 
print(name[0:6:2])#prints character at step=2
