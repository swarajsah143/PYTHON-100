tup=(1,2,3,33,432,5,90,11)
print(type(tup),tup)
tup=(1,)
print(type(tup),tup) # this is tuple with one parameter
tup=(1)
print(type(tup),tup)  # tis is int because one parameter with no comma is always integer


        # this will give error because we cannot chnage tuple 
# tup[1]=22
# print(tup)

tup=(1,2,3,33,432,5,90,11)
tup2= tup[0:6] # slicing of tuple
print(tup2)
tup2= tup[0:6:2] # slicing of tuple
print(tup2)