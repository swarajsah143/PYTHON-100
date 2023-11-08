# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist


file_path=r"C:\Users\ompra\OneDrive\Desktop\PYTHON-100\filehandling\myfiles.txt"

  # to write in a file
  
# a=open(file_path,"w")
# a.write("I am written with write()")
# a.write("\nI am again written with write()")
# a.close()
 
      # to read in a file

# with open(file_path,"r") as a: # anoter method to open a file
  
#     text=a.read() #prints all elements inside file but  print(a.read(5))----- prints only first 5 character in a file
    
#     print(text)

  # to append in a file
  
# with open(file_path,"a") as a:
#     a.write("\nI have appended the content using append mode.")
   
        # to create a new file.
        
f=open("hyper.txt","x") 
   
      # to remove a file
# import os
# os.remove("hyper.txt") 
