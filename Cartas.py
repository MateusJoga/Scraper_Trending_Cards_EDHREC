import requests
import bs4

r = requests.get(f'https://edhrec.com/')

r.raise_for_status()

soup = bs4.BeautifulSoup(r.content, 'html.parser')

container = soup.find('div', class_='index_containerRight__6v7J1')
container = container.find_all('div', class_='index_row__ADQ8G')
container = container[2].find('div', class_='card-body')
cartas = container.find_all('a', href=True)

with open('trending_cards.txt', 'w', encoding='utf-8') as file:
    for carta in cartas:
        texto = carta.get_text().strip()
        if texto:
            file.write('1 ' + texto + '\n')
