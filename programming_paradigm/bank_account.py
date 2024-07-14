class BankAccount:
	"""Implementations of the BankAccount Class that Encapsulates banking operations."""
	def __init__(self, account_balance = 0):
		self.account_balance = account_balance
		
	def deposit(self, amount):
		self.account_balance += amount
		return self.account_balance

	def withdraw(self, amount):
		if self.account_balance > amount:
			self.account_balance -= amount
			return True
		return False

	def display_balance(self):
		if self.account_balance == 0:
			return "No balance available."
		else:
			print("Current balance: " + "${}".format(self.account_balance))