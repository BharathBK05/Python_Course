dont_stop = True
while dont_stop:
    value_1 = int(input("Enter 1st value - "))
    value_2 = int(input("Enter 2nd value - "))
    supported_operation = ['+','-','*','/']

    print("Select any 1 operation from the below list")
    print(supported_operation)
    operation = input("Select the operation - ")

    if operation == '+':
        s = value_1 + value_2
        print(s)
    elif operation == '-':
        s = value_1 - value_2
        print(s)
    elif operation == '*':
        s = value_1 * value_2
        print(s)
    elif operation == '/':
        s = value_1 / value_2
        print(s)
    elif operation == 'exit':
        # dont_stop = False
        break
    else:
        print("This operation is not supported")

print('completed')






    
    






    

        
        






