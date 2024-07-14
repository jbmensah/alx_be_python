def safe_divide(numerator, denominator):
	try:
		numerator = float(numerator)
		denominator = float(denominator)
	except ValueError as e:
		return "Error: Please enter numeric values only."

	else:
		try:
			result = numerator / denominator
		except ZeroDivisionError as eror:
			return "Error: Cannot divide by zero."
		else:
			return f"The result of the division is result"