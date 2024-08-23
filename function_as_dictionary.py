#We can define the function and store thrm as a value in dictionary


# Define the functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# Store the functions in a dictionary
operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Example usage
a = 10
b = 5

# Accessing the functions from the dictionary and calling them
result_add = operations['add'](a, b)
result_subtract = operations['subtract'](a, b)
result_multiply = operations['multiply'](a, b)
result_divide = operations['divide'](a, b)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
