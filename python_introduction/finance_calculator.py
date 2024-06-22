# Calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - total_monthly_expenses

# Print out the monthly savings
print("Your monthly savings are $" + str(int(monthly_savings)) + ".")

# Projected Annual Savings
projected_savings = float(monthly_savings) * 12 + (float(monthly_savings) * 12 * 0.05)

# Print out projected savings
print("Projected savings after one year, with interest, is: $" + str(int(projected_savings)) + ".")