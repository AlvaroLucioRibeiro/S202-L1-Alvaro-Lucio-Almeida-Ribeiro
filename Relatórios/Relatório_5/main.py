from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BooksCLI

db = Database(database="relatorio_5", collection="Livros")
bookModel = BookModel(database=db)

bookCLI = BooksCLI(bookModel)
bookCLI.run()
