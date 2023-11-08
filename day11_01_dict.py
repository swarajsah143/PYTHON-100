dic={
     22:"swaraj",
     69:"Hyper",
     "Ram":"shyam"
    }
# 22,69."Ram" are keys and "swaraj","Hyper","shyam" are values
print(dic)
print(dic["Ram"]) # it maps ram with shyam
print(dic[69]) # it maps 69 with Hyper
print(dic.get(69)) #another method to map
print(dic.keys()) # 22,69,"Ram"
print(dic.values())
for key in dic.keys():
    print(dic[key]) # corresponding to keys 
print(dic.items()) # gives pair 

for key, value in dic.items():
  print(f"The value corresponding to the key {key} is {value}") 
      
