# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while) for each row
while row < size:
    # Inner loop (for) for each column in the row
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to next line after each row
    row += 1  # Increment row counter
