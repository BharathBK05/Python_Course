# 1. Variables store data values
a = 10 
b = 20
c = 'Hi' 
print("Variables")
print(a)
print(b)

#---------------------------------------------------------------------------------------------------


#4 . Data Types
#int - stores whole number
a = 10
b = -5
print("Int")
print(a)
print(b)

#float - stores decimal values
a = 10.5
b = -5.2
print("Float")
print(a)
print(b)

#string - stores single or sequence of characters
a = 'b'
b = 'bharath'
print("String")
print(a)
print(b)

#Boolean - stores only True or False
a = True
b = False
print("Boolean")
print(a)
print(b)


#---------------------------------------------------------------------------------------------------


#5. Data Structures
#List - Ordered, changeable collection
l = [1,2,3,4]
s = ['hi','hello','how','are','you','?']

#Tuple - Ordered, unchangeable collection
t = (1,2,3,4)
f = ('hi','hello','how','are','you','?')

#Dictionary - Key-value pairs(Keys should be unique)
d = {"name":"Ram",
     "age":20,
     "place":"Chennai"}
    
#set - Unordered, unique values. Whatever duplicate values given, it gets neglected
#Here s varible has 5 and 3 duplicated. But if print them it only shows one 5 and 3 
s = {1,2,4,5,5,3,3}
print(s)