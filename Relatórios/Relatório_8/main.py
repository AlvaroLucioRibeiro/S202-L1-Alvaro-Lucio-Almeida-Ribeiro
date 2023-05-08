from database import Database
from game import Game

db = Database("bolt://44.200.108.112:7687","neo4j","silver-expense-meanings")
db.drop_all()

game_db = Game(db)

# Criando os jogadores
game_db.create_player(0, "Álvaro Ribeiro")
game_db.create_player(1, "Cristiano Ronaldo")
game_db.create_player(2, "Lionel Messi")

# Criando uma partida com os jogadores e o resultado
player_ids = [0, 1, 2]
result = "6x1 para Álvaro"
game_db.create_match(player_ids, result)

# Obtendo todas as partidas em que Álvaro Ribeiro participou
matches = game_db.get_player_matches([0])
for match in matches:
    print(match["result"])
    
# Atualizando o nome de Álvaro para Álvaro Ribeiro
game_db.update_player("Álvaro", "Álvaro Ribeiro")

# Obtendo todos os jogadores do banco de dados
players = game_db.get_players()
for player in players:
    print(player["name"])

# Deletando o jogador Cristiano Ronaldo
game_db.delete_player(2)

game_db.close()
