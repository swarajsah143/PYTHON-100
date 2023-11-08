lst=[1,12,23,4,5,6,4,4,4,45,15]
print(lst)
print(lst.index(6)) # prints the index of 6
# print(lst.count(4))
# m=lst
# m[2]=3 # changes 23 into 3
# print(lst)
# lst.insert(2,999) # "2" is index and "24" is element which is added to the index=2
# print(lst)
# lst.append(7)   # to add items
# print(lst)
# lst.sort(reverse=False) #arrange accending
# print(lst)
# lst.sort(reverse=True)   #arrange descending
# print(lst)
# lst.append("Swaraj") # to add string
# print(lst)
# lst.remove(6) # to remove items
# print(lst)

a=[22,33,44,55]
b=[66,77,88,99]

# copy list ?

# a.extend(b)
# print(a)

#    OR    to add diff list together
c=a+b
print(c)
#Note:we cannton arrange the list containing integer and string 


list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = list1[:] # from index o to len(list1)
print(list2)

 # Using list()
list1 = [1, 2, 3, 4, 5]
list2 = list(list1)
print(list2)

#Usinf copy()
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
print(list2)