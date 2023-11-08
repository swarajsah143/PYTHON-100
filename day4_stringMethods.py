# Strings are immutable

name="SwAraJ"
print(name.upper()) #upperCase.Here "name" string is not changed into uppercase but new string hasbeen made So strings are immutable.

print(name.lower())# lowerCase

str1="@@swaraj swaraj swaraj@@@"
print(str1.rstrip("@")) # rstrip() trims the ending similar symbols but not initial one

print(str1.endswith("@@@")) 

print(str1.replace("swaraj","Hyper" )) #here string swaraj is replaced with hyper

print(str1.split("r")) # it splits the string from the given letter in  " " by making a list 

print(str1.count("swaraj"))

str2="swaraj swaraj swaraj swaraj swaraj swaraj swaraj swaraj swaraj swaraj  swaraj swaraj swaraj swaraj swaraj"

print(str2.count("swaraj"))

str3="my name is swarAj Sah"
print(str3.capitalize()) # turns first letter to uppercase and rest  to lowercase

print(str3.swapcase()) #uppercase to lowercase and viceversa

print(str3.endswith("ame",4,7)) # In between 4 to 7th position of string if it ends with "ame" then true else false

print(str3.find("is")) # finds the position of is in string
print(str3.find("iss")) # if no such value then returns -1

# print(str3.index("iss")) this gives error in case of index

print(str3.center(40)) #Gives space to keep at center as per required
print(len(str3.center(40))) 
print(len(str3)) 

str4="WelcomeToSwaraj123\n"
print(str4.isalnum()) #alphanumeric string means string made up of a-z,A-Z,0-9 .this shouldnot contain even a single space
  
print(str4.isalpha())  #only alphabet
print(str4.isupper())  # all should be uppercase
print(str4.isprintable()) # "\n" will not be printed so not printable

str5="A Memorable Day"
print(str5.istitle())  # 1st letter of each word should be capital