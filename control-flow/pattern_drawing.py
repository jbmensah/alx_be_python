size = int(input("Enter the size of the pattern: "))
counter = 0

while counter < size:  # Change condition to counter < size
	# Print rows of square
	for j in range(size):
		print('*', end="")
	print()
	counter += 1  # Increment counter