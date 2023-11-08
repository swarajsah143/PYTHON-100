# is --- compares identities
# == --- compares values i.e. 1,2,3,.....

a=1
b="1"
print(a is b)
print(a == b)

c=[1,2,3]
d=[1,2,3]
print(c is d) # False because these are two diffrent lists
print(c == d)

e=(1,2,3)
f=(1,2,3)
print(e is f) # true because these are same  tuple because tuple are immutables
print(e == f)

