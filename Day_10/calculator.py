def add(num1, num2):
    """Takes two argument and returns the addition
    
    Args:
        num1(int): First operand
        num2(int): Second operand
    Returns:
        Addition of First operand and Second operand
    """
    return num1 + num2
def mul(num1, num2):
    """Takes two argument and returns the multiplication
    
    Args:
        num1(int): First operand
        num2(int): Second operand
    Returns:
        Multiplication of First operand and Second operand
    """
    return num1 * num2
def sub(num1, num2):
    """Takes two argument and returns the subtraction
    
    Args:
        num1(int): First operand
        num2(int): Second operand
    Returns:
        Subtraction of First operand and Second operand
    """
    return num1 - num2
def div(num1, num2):
    """Takes two argument and returns the division
    
    Args:
        num1(int): First operand
        num2(int): Second operand
    Returns:
       division of First operand and Second operand
    """
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Can't divide 0 by 0")

def mod(num1, num2):
    """Takes two argument and returns the modulus
    
    Args:
        num1(int): First operand
        num2(int): Second operand
    Returns:
       modulus of First operand and Second operand
    """
    return num1 % num2

def calculator():
    # create a dictionary for the operations
    """Takes no argument perform calculator function when called"""
    
    """Set the keys to operation and values to the function"""
    operation = {
        "+": add, 
        "-": sub,
        "/": div,
        "*": mul,
        "%": mod
    }

    # Ask user for input
    first_operand = float(input("What's the first number: "))

    """Print out the operations possible for user to make a choice"""
    for symbol in operation:
        print(symbol)

    while(True):
        try:
            # Ask user for operation choice
            operator = input("Pick an operation: ")
            #Ask for second operand
            second_operand = float(input("what's the next number: "))
            
            # get the value for the key selected
            calculation = operation[operator]
            answer = calculation(first_operand, second_operand)
            print("{} {} {} = {}".format(first_operand, operator, second_operand, answer))
            end_loop = input("Type 'y' to continue calculating with {}, or Type 'n' to start again: ".format(answer))
            if end_loop in ["y", "yes", "YES"]:
                first_operand = answer # make the first operand equals the answer
            elif end_loop in ["n", "No","no"]:
                calculator()
            else:
                break
        except (ValueError, ZeroDivisionError, TypeError):
            print("Error: Use correct input or check Usage")  
calculator()