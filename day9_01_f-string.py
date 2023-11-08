letter = "Hey my name is {0} and I am from {1}"
name = "Swaraj"
country = "Nepal"
print(letter.format(name, country))
#name=0 index  and country=1st index
print(f"Hey my name is {name} and I am from {country}")


#output: Hey my name is Swaraj and I am from Nepal

price = 49.0999
txt = f"For only {price:.2f} dollars!"# .2f means it takes 2 digit after decimal
print(txt)


