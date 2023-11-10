# My simple calculator
def
 
add(num1, num2):

    
return num1 + num2

def
 
subtract(num1, num2):

    
return num1 - num2

def
 
multiply(num1, num2):

    
return num1 * num2

def
 
divide(num1, num2):

    
return num1 / num2


print("Enter your numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# a list of the basic operations
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# selecting an operation
choice = input("Enter your choice: ")

# executing operation
if choice == "1":
    result = add(num1, num2)
elif
 
choice == "2":
    result = subtract(num1, num2)
elif choice == "3":
    result = multiply(num1, num2)
elif choice == "4":
    result = divide(num1, num2)
else:
    print("Invalid choice.")
    exit()

# Display the result
print("The result is:", result)