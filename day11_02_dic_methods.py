dic1={
    11:22,
    33:44,
    55:66,
    77:88,
    99:98
}
dic2={
    11:23,
    33:45,
    52:66,
    72:88,
    99:92
}
dic1.update(dic2)
print(dic1)

dic1.pop(55) # removes 55:66 from dic1
print(dic1)

# popitem()--- removes last item
dic1.popitem()
print(dic1)

# to delete dictonary
# del dic1

del dic2[72]  # to remove particular item
print(dic2)

dic2.clear() #empty dictonary
print(dic2)