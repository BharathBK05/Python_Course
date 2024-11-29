#for loop
#syntax ---> for variable in range(start_value,end_value,iteration_level):

# Print from 0 to 100
for i in range(0,100,1):
    if i == 10:
        continue #This is used to skip specific thing. #Here the number 10 gets skipped from printing
    print(i)
    
# #Print from 20 to 30
for i in range(20,30,1):
    print(i)

#print from 100 to 0
for i in range(100,0,-1):
    print(i)

#Print values in list
# syntax ---> for variable in list:
names = ['a','b','c','d','e']
for i in names:
    print(i)