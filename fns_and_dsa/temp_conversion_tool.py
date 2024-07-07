# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
	return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# User interaction
def main():
	try:
		temperature = float(input("Enter the temperature to convert: "))
		unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

		if unit == 'F':
			converted_temp = convert_to_celsius(temperature)
			print(f"{temperature}°F is {converted_temp}°C")
		elif unit == 'C':
			converted_temp = convert_to_fahrenheit(temperature)
			print(f"{temperature}°C is {converted_temp}°F")
		else:
			raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

	except ValueError as e:
		print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
	main()
