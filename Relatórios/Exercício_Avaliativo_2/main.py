# Nome: Álvaro Lúcio Almeida Ribeiro 
# Matrícula: 163 
# Exercício Avaliativo 2

from database import Database
from teacher_crud import TeacherCRUD
# --------------------------------------------------------------------------------------- #
# Questão 3
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

class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Enter the teacher's name: ")
        ano_nasc = int(input("Enter the teacher's birth year: "))
        cpf = input("Enter the teacher's cpf: ")
        self.teacher_crud.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Enter the teacher's name: ")
        teacher = self.teacher_crud.read(name)
        print(teacher)

    def update_teacher(self):
        name = input("Enter the teacher's name: ")
        newCpf = input("Enter the teacher's new cpf: ")
        self.teacher_crud.update(name, newCpf)
        
    def delete_teacher(self):
        name = input("Enter the teacher's name: ")
        self.teacher_crud.delete(name)

    def run(self):
        print("Welcome to the Teacher CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()

# --------------------------------------------------------------------------------------- #
db = Database("bolt://18.206.250.26:7687", "neo4j", "twist-film-offers")
teacher_crud = TeacherCRUD(db)
cli = TeacherCLI(teacher_crud)
cli.run()
db.close()