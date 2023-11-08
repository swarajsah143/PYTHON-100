# NOTE No need to declare the type of variable whether it is numeric or string but at the time     of input ,it is necessary to declare datatype of variablr
# String variable requres "..."

a=333453
print(a,"-----number \n\n")

b="Swaraj"
print(b,"----string \n\n")

c=True
print(c,"---boolen \n\n")

d=None
print(d,"-----nonetype \n\n")

e=complex(2,5) #complex no.-----  2+5j
print(e,"-------complex no. \n\n")

f=[3,4,5]     #list----can be changed or mutable.It starts with big braces
print(f,"--------list type \n\n")

g=(2,3,[2,4],"Hyper"),("swaraj",3,5677) #tuple----cannot be changed or immutable.It starts with small braces
print(g,"--------tuple type \n\n")

h={"Name":"Swaraj","Class":12,"Roll":19} #Dict datatype means like dictnory. 
print(h,"------Dictonary type \n\n")


print("\nThe type of a is ",type(a))  # type() is used to find out type of variable 
print("The type of b is ",type(b))
print("The type of c is ",type(c))
print("The type of d is ",type(d))
print("The type of e is ",type(e))
print("The type of f is ",type(f))
print("The type of g is ",type(g))
print("The type of h is ",type(h))