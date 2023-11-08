set={1,2,"swaraj",2,"name1","name2"}
print(set)
# sets doenot allow duplicate or copied items
for value in set:
    print(value) # it gives output in any order.In any  order means not necessarily prints 1,2,swaraj... It can also prints swaraj,1,name1,....

swaraj=set()  # empty set
# swaraj=set{}  #  Not a empty set
print(type(swaraj))