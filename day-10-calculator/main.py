
from art import logo
#calculations

#add
def add(n1, n2):
    return n1 + n2

#substract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

#dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#user choose the first number. print all the possible symbols.
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    should_continue = True
    for symbol in operations:
        print(symbol)

    #loop through the dictionary

    while should_continue is True:
        operation_symbol = input("Pick an operation: ")

        #user choose the next number
        num2 = float(input("What is the next number?: "))

        #calculation_function stores function chosen from the operation dictionary (specific one from the symbol chosen by users)
        calculation_function = operations[operation_symbol]
        #then, we insert two numbers chosen by the user and run the fuction defined in the dictionary
        answer= calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if cont == "y":
            num1 = answer
        elif cont == "n":
            should_continue = False
            calculator()

calculator ()



