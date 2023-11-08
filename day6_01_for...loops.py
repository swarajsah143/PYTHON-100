# print natural no. using for lop in python ?

color=["red","blue","green","pink"]
for i in color:
    print(i)
    # print(i,end=",") output- red,blue,green,pink
    for j in i:
        print(j)
        
# for k in range(20001):
#     print(k)

for l in range(1,20,2): # range(x,y,z) x=initial value , y=final value , z=increment or decrement
    print(l+1)
