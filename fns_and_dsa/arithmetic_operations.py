# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: Numeric result, or an error message string for invalid operation
                      or division by zero.
    """
    if operation is None:
        return "Error: Invalid operation"

    op = operation.strip().lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

