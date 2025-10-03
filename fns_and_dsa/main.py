# main.py (inside fns_and_dsa folder)

from arithmetic_operations import perform_operation

def main():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    result = perform_operation(num1, num2, operation)
    print("Result:", result)

if __name__ == "__main__":
    main()
