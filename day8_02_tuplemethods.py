tup=("nepal","pakistan","bhutan","japan")
print(tup)
lst=list(tup) #  to convert tuple into list
print(lst)
lst[1]="Australia"  # to change 
print(lst)
lst.pop(2) # to remove 
lst.append("Nigeria")
tup=tuple(lst) # to convert list into tuple
print(tup)


#tuple.index(element, start, end)

tup1=(0,1,2,3,4,5,6,7,3,4,2,1)
pos=tup1.index(3,6,10)   #index of 3 between 6th to 10th
print("The index of 3 from 6th position to 10th position is ",pos)