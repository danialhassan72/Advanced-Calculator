#Mathematical calculator

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
     return n1 - n2
def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("what your first number?:"))

for symbol in operations:
    print(symbol)

should_continue = True
while should_continue:

        operation_symbol = input("pick an operation from line above")

        num2 = int(input("what's the second number ?"))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"f{num1}{operation_symbol}{num2} ={answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y" :
          num1 = first_answer
        else:
            should_continue = False
