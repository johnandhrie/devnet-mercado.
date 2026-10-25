
import random
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_LIST = ["pikachu", "charizard", "bulbasaur", "squirtle", "jigglypuff"]

def fetch_pokemon_data(pokemon_name):
    url = f"{BASE_URL}{pokemon_name.lower()}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "name": data["name"].lower(),
                "height": data["height"],
                "weight": data["weight"]
            }
        elif response.status_code == 404:
            return None
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def play_game():
    print("========================================")
    print("      WELCOME TO WHO'S THAT POKÉMON!    ")
    print("========================================")
    
    selected_pokemon_name = random.choice(POKEMON_LIST)
    pokemon_data = fetch_pokemon_data(selected_pokemon_name)
    
    if not pokemon_data:
        print("Could not retrieve Pokémon data.")
        return

    print("\nI have chosen a Pokémon! Can you guess who it is?")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")
    
    print("\nChoices:")
    for pokemon in POKEMON_LIST:
        print(f"- {pokemon.capitalize()}")
    print("-" * 40)

    attempts_left = 3

    while attempts_left > 0:
        print(f"Attempts remaining: {attempts_left}")
        guess = input("Your guess: ").strip().lower()

        if not guess or guess not in POKEMON_LIST:
            print("Invalid input. Please choose a name from the list of choices.\n")
            continue

        if guess == pokemon_data["name"]:
            print("\nCorrect! You guessed the Pokémon!")
            print(f"It was {pokemon_data['name'].capitalize()}!")
            return
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print("Wrong guess! Try again.\n")

    print("\nGame Over! You've run out of attempts.")
    print(f"The correct Pokémon was: {pokemon_data['name'].capitalize()}")

if __name__ == "__main__":
    play_game()