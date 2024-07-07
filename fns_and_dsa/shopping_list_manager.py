def display_menu():
	print("Shopping List Manager")
	print("1. Add Item")
	print("2. Remove Item")
	print("3. View List")
	print("4. Exit")

def main():
	shopping_list = []

	while True:
		display_menu()
		choice = input("Enter your choice: ")

		if choice == '1':
			add_item = input("Enter the item to add: ")
			if add_item.strip(): # Check if add_item is not empty
				shopping_list.append(add_item)
			else:
				print("Item name cannot be empty. Please try again.")

		elif choice == '2':
			if not shopping_list:
				print("Shopping list is empty. Nothing to remove.")
			else:
				remove_item = input("Enter item to remove: ")
				if remove_item in shopping_list:
					shopping_list.remove(remove_item)
					print(f"{remove_item} removed from shopping list.")
				else:
					print(f"{remove_item} is not found in the shopping list.")

		elif choice == '3':
			if not shopping_list:
				print("Shopping list is empty")
			else:
				print("Shopping list: ")
				for item in shopping_list:
					print(item)

		elif choice == '4':
			print('Goodbye!')
			break
		
		else:
			print("Invalid choice. Please try again.")

if __name__ == '__main__':
	main()