import requests
import os
from dotenv import load_dotenv

load_dotenv()

game_cover_data = {}


def get_game_cover(game_name):
    headers = {'Client-ID': os.getenv('CLIENT-ID'), 'Authorization': os.getenv('AUTHORIZATION')}
    search_data = f'fields name, platforms, cover.image_id; search "{game_name}"; where platforms = (6);'

    data = requests.post('https://api.igdb.com/v4/games', headers = headers, data = search_data)
    image_data = data.json()
    for game in image_data:
        if game_name in game['name']:
            game_cover_data[game['name']] = game['cover']['image_id']

    print(game_cover_data)
    print(f'https://images.igdb.com/igdb/image/upload/t_cover_big/{game_cover_data[game_name]}.jpg')


get_game_cover('Forspoken')
