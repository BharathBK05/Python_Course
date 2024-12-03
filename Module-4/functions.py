def summation(a,b,c): #function definition
    #total is a function variable
    total = a+b+c
    return total

def percentage(obtained_marks,total_marks): #function definition
    #percent is a function variable
    percent = (obtained_marks/total_marks) * 100 
    return percent

maths = 100
physics = 90
chemistry = 80
obtained_marks = summation(physics,chemistry,maths) #calling the function
percent = percentage(obtained_marks,300) #calling the function
print("The percentage of the student is " + str(percent))


# scope:



# def <functioname>(parameters,...,...,...,..)
