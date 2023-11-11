                #Map

def cube(x):
    return x**3
l=[1,2,3,4,5,6,7]
newl=list(map(cube,l)) # map(function_name,list_name)
# It maps the element inside list one by one and then pass to function as parameter
print(newl)



            # Filter

# def filter_function(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,
#                10, 11, 12, 13, 14, 15, 16, 1
#                , 17, 18, 19, 20, 21, 22, 23,
#                24, 25, 26, 27, 28, 29, 30, 3
#                , 31, 32, 33, 34, 35, 36, 37,
#                38, 39, 40, 41, 42, 43, 44, 4
#                , 45, 46, 47, 48, 49, 50, 51,
#                52, 53, 54, 55, 56, 57, 58, 5
#                , 59, 60, 61, 62, 63, 64, 65,
#                66, 67, 68, 69, 70, 71, 72, 7
#                , 73, 74, 75, 76, 77, 78, 79,
#                80, 81, 82, 83, 84, 85, 86, 8
#                , 87, 88, 89, 90, 91, 92, 93,
#                94, 95, 96, 97, 98, 99, 100]
# filtered_numbers = list(filter(filter_function, numbers))
# print("Filtered Numbers are : ", filtered_numbers)
    
# Another Example

def filter_examp(y):
    if y>4:
        return y # it returns to function calling i.e. newscore
    else:
        return False
scores = [1,2,3,4,5,6,7,8,9,10,11,1]
newscore=list(filter(filter_examp,scores)) # this passes element one by one
print(newscore)


         #Reduce
from functools import reduce
l=[1,2,3,4,5,6,7]
sum=reduce((lambda x,y:x+y),l)
print(sum)


# output process:
 # lnew=l[0]+l[1] where 0 and 1 are x and y
 # llnew=lnew+l[2] 
 # llnew+l[3] 
 
 # 1+2
 # (1+2)+3
 # ((1+2+3)+4
 # (1+2+3+4)+5
 # (1+2+3+4+5)+6
 # (1+2+3+4+5+6)+7 =28 Ans

