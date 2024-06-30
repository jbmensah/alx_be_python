number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
	# Outer loop iterates through the rows (multiplication factors)
	for j in range(1, 11):
		# Inner loop iterates through columns (other factors)
		product = number * i
	print(f"{number} x {i} = {product}") # Print with new line for better formatting
	# print() # Move to a new line after each row