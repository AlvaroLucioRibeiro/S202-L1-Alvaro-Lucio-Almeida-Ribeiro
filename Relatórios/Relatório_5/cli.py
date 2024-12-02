class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class BooksCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        _id = int(input("Enter the id: "))
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        price = float(input("Enter the price: "))
        self.book_model.create(_id, title, author, year, price)

    def read_book(self):
        book_id = str(input("Enter the book ID: "))
        book = self.book_model.read_by_id(book_id)

    def update_book(self):
        book_id = str(input("Enter the book ID: "))
        title = input("Enter the new title: ")
        author = input("Enter the new author: ")
        year = input("Enter the new year: ")
        if year:
            year = int(year)
        price = input("Enter the new price: ")
        if price:
            price = float(price)
        self.book_model.update(book_id, title, author, year, price)

    def delete_book(self):
        book_id = str(input("Enter the book ID: "))
        self.book_model.delete(str(book_id))

    def run(self):
        print("Welcome to the Book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
