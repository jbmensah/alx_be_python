class Book:

	def __init__(self, title, author, is_checked_out=False):
		self.title = title
		self.author = author
		self.__is_checked_out = is_checked_out

	def is_checked_out(self):
		return self.__is_checked_out
	
	def set_checked_out(self, status):
		self.__is_checked_out = status

class Library:

	def __init__(self):
		self.__books = []

	def add_book(self, book):
		self.__books.append(book)

	def check_out_book(self, title):
		for book in self.__books:
			if book.title == title:
				if not book.is_checked_out():
					book.set_checked_out(True)
					print(f"Checked out: {title}")
				else:
					print(f"Book '{title}' is already checked out")
				return
		print(f"Book '{title}' not found in the library.")

	def return_book(self, title):
		for book in self.__books:
			if book.title == title:
				if book.is_checked_out():
					book.set_checked_out(False)
					print(f"Returned: {title}")
					return book(self)
				else:
					print(f"Book {title} is already returned.")
					return
		print(f"Book '{title}' not found in the library.")

	def list_available_books(self):
		available_books = []
		for book in self.__books:
			if not book.is_checked_out():
				available_books.append(f"{book.title} by {book.author}")
		return available_books