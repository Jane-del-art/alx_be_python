# pattern_drawing.py
# Draw a square pattern of asterisks using a while loop and nested for loop

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for each row
while row < size:
    # For loop for each column in the current row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    row += 1  # Increment row counter
