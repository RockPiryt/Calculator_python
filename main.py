# Program - Calculator
from art import logo


#Functions
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

#Operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide}

def calculator():
    print(logo)
    #User inputs first number
    num1 = float(input('Please write the first number: '))


    #Show user operation available
    for operation in operations:
        print(operation)

    ##########use while loop to unlimited operations#####
    should_continue =  True

    while should_continue is True:
        #User input operation symbol
        operation_symbol = input('Please pick an operation: ')
        # Ask user for next number
        num2 = float(input('Please write the next number: '))

        #####schema to calculate#####
        # function = operation['*']
        # function(2,3)
        ###########################
        # choose function which is assigned to symbol
        calculation_func = operations[operation_symbol]
        # give function for exmaple 'add' 2 arguments
        answer = calculation_func(num1, num2)

        #Show answer to user
        print(f' {num1} {operation_symbol} {num2} = {answer}')

        #conditionals for while loop
        continue_question = input(f'Type "y" to continue calculationg with {answer}, type "n" to new calculating or type "e" to exit: ')
        if continue_question == 'y':
            num1 = answer # assign to first number answer from first calculation
        elif continue_question == 'n':#start new calcualtion
            should_continue = False
            calculator()
        else:#type 'e'
            should_continue = False
            
calculator()





###########without while loop - only to operations are available

# #User input operation symbol
# operation_symbol = input('Please pick an operation from the line above: ')

# Ask user for next number
#num2 = int(input('Please write the second number: '))

#####schema to calculate#####
# # function = operation['*']
# # function(2,3)
#############################

# # choose function which is assigned to symbol
# calculation_func = operations[operation_symbol]

# # give function for exmaple 'add' 2 arguments
# answer = calculation_func(num1, num2)

# #Show answer to user
# print(f' {num1} {operation_symbol} {num2} = {answer}')

# # Use answer value to next operations
# operation_symbol = input('Please pick another operation: ')
# num3 = int(input('Please write the next number: '))
# calculation_func2 = operations[operation_symbol]
# next_answer = calculation_func2(answer, num3)
# print(f' {answer} {operation_symbol} {num3} = {next_answer}')

#use output function as argument - this can make bug
# next_answer = calculation_func2(calculation_func(num1, num2), num3)
# next_answer = 2 * 3 * 3 = 18





