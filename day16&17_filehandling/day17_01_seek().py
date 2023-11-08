# myfiles=r"C:\Users\ompra\OneDrive\Desktop\PYTHON-100\day16&17_filehandling\myfiles.txt"

# # content in myfiles-- I am written with write()
# with open(myfiles,"r") as f:
#     f.seek(5) # seek() it leaves 1st 5 element and then read
#     print(f.tell()) 
#     # tell() ----tells the position from where seek has been done 
#     a=f.read(5) # read only 5 elements after seek()
#     print(a) #writt
    
with open("truncate.txt","w") as t:
    t.write("Hello Baby")
    t.truncate(7) # it only takes first 7 element wriiten in t.write()

