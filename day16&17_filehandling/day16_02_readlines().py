# f=open("marks.txt","x") 
# with open("marks.txt","w") as text:
    # text.write("10,15,20,25")
    # text.write("\n30,14,24,28")

f=open("marks.txt","r")
i=0
while True:
    marks=f.readline()# readline()--- reads all the line step by step
    i=i+1
    if not marks:
        break
    m1=int(marks.split(",")[0])
    m2=int(marks.split(",")[1])
    m3=int(marks.split(",")[2])
    m4=int(marks.split(",")[3])
    print(f"The marks of student {i} in SSt is {m1*3}")
    print(f"The marks of student {i} in Maths is {m2}")
    print(f"The marks of student {i} in Science is {m3}")
    print(f"The marks of student {i} in English is {m4}")
    print("\n")
f.close