from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://pokemondb.net/pokedex/all').text
soup = BeautifulSoup(html_text,'lxml')
tbody = soup.find('tbody')
pokemons = tbody.find_all('tr')
for pokemon in pokemons:
    pokedex_num = pokemon.find('span',class_='infocard-cell-data').text
    if int(pokedex_num) <= 1:
        name = pokemon.find('td',class_='cell-name').text
        types = pokemon.find('td',class_='cell-icon').text
        totalstats = pokemon.find('td',class_='cell-total').text
        more_info = pokemon.find('td',class_='cell-name')
        href = more_info.a['href']
        #print(pokemon)
        print(f"""
        Pokedex Number: {pokedex_num}
        Pokemon Name: {name}
        Types:{types}
        Total Stats:{totalstats}
        MoreInfo:{more_info}
        href:{href}
        """)