class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self):
        if self.title == self.title:
            self._is_checked_out == True
            return True
        else:
            return False

    def return_book(self):
        if self.title == self.title:
            self._is_checked_out == False
            return True
        else:
            return False

class Library:
    def __init__(self):
        self._books = []
        self._checked_out_books = []
        

    def add_book(self, book):
        self._books.append(book)
        return

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
                self._books.remove(book)
                self._checked_out_books.append(book)
                break
        for remain in self._books:
            print(f"{remain.title} by {remain.author}")

    def return_book(self, title):
        for book in self._checked_out_books:
            if book.title == title:
                book._is_checked_out = False
                self._books.append(book)
                self._checked_out_books.remove(book)
                return
            print(f"Book {title} is not available")
        for new_list in self._books:
            print(f"{new_list.title} by {new_list.author}")


    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")