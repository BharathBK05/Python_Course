# Operators

# Arithmetic
a = 10
b = 20
c = a - b
print(c)
print(a+b)
print(10+20)

#Comparison
a = 10
if a < 5:
    print('Hi')
else:
    print('Hello')


if a==10:
   print('a equals to 10')
else:
    print('a not equals to 10') 


#Logical
a = 10
b = 20

if a < 10 and b > 5: #here both conditions should be true
    print('Hi')
else:
    print('Hello')

if a < 10 or b > 5: #here any one conditions should be true
    print('Hi')
else:
    print('Hello')


# Not operator. Example: Check if a list is empty
my_list = []

if not my_list:
    print("The list is empty.")


#Assignment operators
a = 10
a = a + 1
a += 1 #Line no. 49 can also be written as this

b = b - 1
b -= 1


#-------------------------------------------------------------------------------------------------------------------

#Input from user

a = input()
b = input()
print(type(a)) #it gives string
print(type(b)) #it gives string

#type cast from string to int
a = int(input())
b = int(input())
print(type(a)) #it gives int
print(type(b)) #it gives int


#Error case. This is called as exception
try:
    a = int(input('Enter only integers - '))
    b = int(input('Enter only integers - '))
    print(a+b)
except:
    print('Invalid Input')

#String concatanation
a = input()
b = input()
print(a+b) #It concats the string

