from database import Database
from game import Game

db = Database("bolt://44.200.108.112:7687","neo4j","silver-expense-meanings")
db.drop_all()

game_db = Game(db)

# Criar jogadores
game_db.create_player(1, "Álvaro")
game_db.create_player(2, "Cristiano Ronaldo")
game_db.create_player(3, "Lionel Messi")

# Atualizar jogador
game_db.update_player("Álvaro", "Álvaro Ribeiro")

# Deletar jogador
game_db.delete_player(3)

# Get jogadores
players = game_db.get_players()
for player in players:
    print(player["name"])

# Criar um match
game_db.create_match([1, 2], "Vitória de Álvaro por 3 a 1")

# Get Match
match = game_db.get_match(1)
if match:
    print(match["result"])
else:
    print("Match not found.")

game_db.close()