task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
	case "high":
		if time_bound == "yes":
			reminder = 'that requires immediate attention today!'
			print(f"Reminder: '{task}' is a high priority task {reminder}")
	case "low" |"medium":
		if time_bound == "no":
			reminder = 'Consider completing it when you have free time.'
			print(f"Note: '{task}' is a low priority task. {reminder}")

