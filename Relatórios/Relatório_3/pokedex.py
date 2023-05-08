from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

class Pokedex:
        
        def getPokemonsByType(types: list):
          return db.collection.find({"type": {"$in": types}})
      
        def getPokemonsByEggs(eggs: str):
          return db.collection.find({"egg": eggs})
      
        def getPokemonsByWeight(weight: str):
          return db.collection.find({"weight": weight})
      
        def getPokemonsByPrevolutionNum(name: str):
          return db.collection.find({"prev_evolution.name": name})
        
        def getPokemonsByCandyNone(candy: str):
          return db.collection.find({"candy": candy})
