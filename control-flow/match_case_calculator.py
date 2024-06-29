#  Learn to use Match Case statements for handling multiple operations in a simple calculator program.

# Prompt for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operand = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation Using Match Case
match operand:
	case "+":
		result = num1 + num2		
	case "-":
		result = num1 - num2		
	case "/":
		if num2 != 0:
			result = num1 / num2			
		else:
			print("Cannot divide by zero.")
			result = None
	case "*":
		result = num1 * num2		
	case _:
		print("Error: Unsuppported operand.")
		result = None

if result is not None:
	print(f"The result is {result}")