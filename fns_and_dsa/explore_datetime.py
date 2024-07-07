import datetime

def display_current_datetime():
	current_date = datetime.datetime.now()
	formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
	print("Current date and time:", formatted_date)

def calculate_future_date():
	future_date = int(input("Enter the number of days to add to the current date: "))
	current_date = datetime.datetime.now()
	future_date = current_date + datetime.timedelta(days=future_date)
	formatted_future_date = future_date.strftime("%Y-%m-%d")
	print(f"Future date: {formatted_future_date}")

display_current_datetime()
calculate_future_date()