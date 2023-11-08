set1={1,2,3,"swaraj",6,7}
set2={11,21,3,"swaraj",16,7}


print(set1.union(set2))  #union() simply (AUB)


set1.update(set2)   #those elements od set2 which are not in set1 can be kept in set1 by the help of update()
print(set1,set2)

   #Intersection methods

#intersect() method returns a new set with common elements from both sets

set1={1,2,3,"swaraj",6,7}
set2={11,21,3,"swaraj",16,7}

print(set1.intersection(set2))  #intersection() simply (AnB)

print(set1)  # this willnot changed after intersection


set1.intersection_update(set2)   # now set1 is changed/updated to intersection of both set
print(set1)

set1.update(set2)   #those elements od set2 which are not in set1 can be kept in set1 by the help of update()
print(set1,set2)

# Symertic difference 

set1={1,2,3,"swaraj",6,7}
set2={11,21,3,"swaraj",16,7}
print(set1.symmetric_difference(set2)) # symmetric_difference() = A-B U B-A

print(set1)   # Original Set1

# Symertic difference update
set1.symmetric_difference_update(set2)  
print(set1)
#now set1 is updated to symmetric difference of two sets

# Difference set
set1={1,2,3,"swaraj",6,7}
set2={11,21,3,"swaraj",16,7}

print(set1.difference(set2)) 
# only Set1 not common element
print(set1)
set1.difference_update(set2)
print(set1)

#SUBSETS METHODS and DISJOINT SETS

#issubset() checks if all elements of set1 are present in set2 or not

#isdisjoint() checks if there is no common element between two sets or not
set1={1,2,3,"swaraj",6,7}
set2={11,21,32,"swaraaaj",16,72}
set3={1,2,3}
print(set3.issubset(set1))    
#True means all elements of set3 are in set1
print(set1.isdisjoint(set2))   
#False means there is atleast one common element

print(set1.issuperset(set3))

# to add element in  set
set1={1,2,3,"swaraj",6,7}
set1.add(4)  
set1.add("Hyper")  
print(set1)

# to remove element in  set

set1.remove("swaraj")
set1.discard(2)
print(set1)
 
 # to pop out from set
set1={1,2,3,"swaraj",6,7}
element=set1.pop() # any one element from set will come outside
print(set1)
print(element)

del set1
# print(set1) Here it doesnot print because set1 is deleted

#clear()--- to delete all elements from set 
set1={1,2,3,"swaraj",6,7}
set1.clear()
print(set1)
# output=set()