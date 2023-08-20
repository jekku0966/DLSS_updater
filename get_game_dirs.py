import os


def scan_steam_games():
    steam_path = os.path.expanduser('C:/Program Files (x86)/Steam/steamapps/common')
    games = []
    if os.path.isdir(steam_path):
        for game_folder in os.listdir(steam_path):
            game_path = os.path.join(steam_path, game_folder)
            if os.path.isdir(game_path):
                games.append((game_folder, game_path))
    return games
