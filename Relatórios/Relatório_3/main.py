from pokedex import Pokedex
from helper.writeAJson import writeAJson

def main():
    
    # Buasca os pokemons com tipo grass
    types = ["Grass"]    
    pokemons_by_Grass = Pokedex.getPokemonsByType(types)
    writeAJson(pokemons_by_Grass, "pokemons_Grass")
    
    # Buasca os pokemons com ovos a 2km
    pokemons_by_Eggs = Pokedex.getPokemonsByEggs("2 km")
    writeAJson(pokemons_by_Eggs, "Pokemons_Eggs_2km")
    
    # Buasca os pokemons com pelo de 80 kg
    pokemons_by_Weight = Pokedex.getPokemonsByWeight("80.0 kg")
    writeAJson(pokemons_by_Weight, "Pokemons_Weight_80kg")
    
    # Busca os pokemons que evolui para o "Eevee"
    pokemons_by_Evolution = Pokedex.getPokemonsByPrevolutionNum("Eevee")
    writeAJson(pokemons_by_Evolution, "Pokemon_Evolution_Eevee")

    pokemons_by_Candy = Pokedex.getPokemonsByCandyNone("None")
    writeAJson(pokemons_by_Candy, "Pokemons_CandyNone")


if __name__ == '__main__':
    main()
