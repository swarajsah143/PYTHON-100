class Student:
    name="name1"
    caste="caste1"
    grade=12
    roll=19
    college="National Infotech"
# print(Student.name) direct print through class

    def info(self): # Self is that parameter which is used for that object which is being called
      print("Name : ", self.name) 
      print("Caste : ", self.caste)
      print("Grade : ", self.grade)
      print("Roll No : ", self.roll)
      print("College : ", self.college)
    
      
a=Student()
# a.name=input("") # we can take input from the user by this way. 
a.name="Swaraj"
a.caste="Sah"
a.grade=12
a.roll=2
a.college="National Infotech\n"

b=Student()
b.name="Sanu"
b.caste="Gupta"
b.roll=1
b.grade=11
b.college="South ZOne\n"

c=Student()
#If no info is given then all info will be default  value.

a.info() #calling a function
b.info()
c.info()

# a.name="Hyper"
# a.roll=20
# print(a.name,a.roll)
# # This will print the new value of a's name attribute  
