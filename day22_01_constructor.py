class person:    
    def __init__(self,name,grade,occ):#It accepts  arguments along with self which is known as parameterized constructor
        
        print("Hey,I will be called every instant\n")
        self.name=name
        self.grade=grade
        self.occ=occ
       #First this function runs completely then moves to another line by assigning values in variables.
     
    def info(self):

        print(f"Name : {self.name}")
        print(f"Grade : {self.grade}")
        print(f"Occupation : {self.occ}\n")
         
a=person("sanu",10,"CA")
b=person("hyper",12,"HR")
c=person("swaraj",11,"Fronted Dev.")

a.info()
b.info()
c.info()


class person:
    def __init__(self):
        print("hey i am a default constructor")
a=person()
     
    #  This is default constructor as it doesnot takes any parameter
    

         #Direct by function
         
# def info(n,g,r):
#     print(f"Name : {n}")
#     print(f"Grade : {g}")
#     print(f"Roll : {r}\n")
# info("SANU","10th","3456789")
# info("swaraj","12nd","14563789")
# info("hyper","11st","21456789")
# info("bauwo","9th","45236789")
    
