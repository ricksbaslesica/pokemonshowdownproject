class Pokemon: 
	def __init__ (pokemon, speciesname, type1, type2,
                      HP, attack , defense, specialattack, specialdefense, speed
                      ):
		pokemon.speciesname = speciesname
		pokemon.type1 = type1
		pokemon.type2 = type2
		pokemon.HP = HP
		pokemon.attack= attack
		pokemon.defense = defense
		pokemon.specialattack = specialattack
		pokemon.specialdefense = specialdefense
		pokemon.speed = speed
		pokemon.basestats = ([pokemon.HP,pokemon.attack,
			pokemon.defense,pokemon.specialattack,
			pokemon.specialdefense, pokemon.speed])
MrRime = Pokemon("Mr. Rime", "Ice", "Psychic", 80, 85, 75, 110, 100, 70)
Inteleon = Pokemon("Inteleon", "Water", "None", 70, 85, 65, 125, 65, 120)
Ludicolo = Pokemon("Ludicolo", "Water", "Grass", 80, 70, 70, 90, 100, 70)
Hawlucha = Pokemon ("Hawlucha", 78, 92, 75, 74, 63, 118)
Hippowdon = Pokemon("Hippowdon", "Ground", "None", 108, 112, 118, 68, 72, 47)
Hydreigon = Pokemon("Hydreigon", "Dark", "Dragon", 92, 105, 90, 125, 90, 98)
Snorlax = Pokemon("Snorlax", "Normal", "None", 160, 110, 65, 65, 110, 30)

def printpokemon(pokemontoprint):
        print (pokemontoprint.speciesname, ":", pokemontoprint.type1, "/", 
               pokemontoprint.type2, pokemontoprint.basestats)

printpokemon (MrRime)
printpokemon (Inteleon)
