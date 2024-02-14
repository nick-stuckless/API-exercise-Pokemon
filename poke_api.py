'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")

    print(poke_info)
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    poke_name = str(pokemon_name).strip().lower()
    poke_url = POKE_API_URL + poke_name 

    # TODO: Build a clean URL and use it to send a GET request

    print("Getting Pokemon info ...", end="")
    resp = requests.get(poke_url)

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp.status_code == requests.codes.ok:
        print("Success!")
        dict = resp.json()
        return dict
    else:
        print("Failure: ")
        print(f"{resp.status_code} {resp.reason} ({resp.text})")
    # TODO: If the GET request failed, print the error reason and return None
        return

if __name__ == '__main__':
    main()