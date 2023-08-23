import os


def scan_custom_games(folder_path):
    games = []
    if os.path.isdir(folder_path):
        for game_folder in os.listdir(folder_path):
            game_path = os.path.join(folder_path, game_folder)
            if os.path.isdir(game_path):
                games.append((game_folder, game_path))
    return games

# Function to scan Steam game installations


def scan_steam_games():
    steam_path = os.path.expanduser('C:/Program Files (x86)/Steam/steamapps/common')
    games = []
    if os.path.isdir(steam_path):
        for game_folder in os.listdir(steam_path):
            game_path = os.path.join(steam_path, game_folder)
            if os.path.isdir(game_path):
                games.append((game_folder, game_path))
    return games


# Function to scan Origin game installations

def scan_origin_games():
    origin_path = os.path.expanduser('C:/Program Files (x86)/Origin Games')
    games = []
    if os.path.isdir(origin_path):
        for game_folder in os.listdir(origin_path):
            game_path = os.path.join(origin_path, game_folder)
            if os.path.isdir(game_path):
                games.append((game_folder, game_path))
    return games


# Function to scan Xbox game installations
def scan_xbox_games():
    xbox_path = os.path.expanduser('C:/XboxGames')
    games = []
    if os.path.isdir(xbox_path):
        for game_folder in os.listdir(xbox_path):
            game_path = os.path.join(xbox_path, game_folder)
            if os.path.isdir(game_path):
                games.append((game_folder, game_path))
    return games


# Function to scan Epic Games installations
def scan_epic_games():
    epic_path = os.path.expanduser('C:/Program Files/Epic Games')
    games = []
    if os.path.isdir(epic_path):
        for game_folder in os.listdir(epic_path):
            game_path = os.path.join(epic_path, game_folder)
            if os.path.isdir(game_path):
                games.append((game_folder, game_path))
    return games


def run_game_search():
    all_games = []

    # Scan Steam games
    steam_games = scan_steam_games()
    all_games.extend(steam_games)

    # Scan Origin games
    origin_games = scan_origin_games()
    all_games.extend(origin_games)

    # Scan Xbox games
    xbox_games = scan_xbox_games()
    all_games.extend(xbox_games)

    # Scan Epic Games
    epic_games = scan_epic_games()
    all_games.extend(epic_games)

    # Ask for custom folders
    while True:
        custom_folder_path = input("Enter a custom folder path (or 'done' to finish): ")
        if custom_folder_path.lower() == 'done':
            break
        custom_games = scan_custom_games(custom_folder_path)
        all_games.extend(custom_games)

    # Print all found games
    if all_games:
        print("Found games:")
        for game_name, game_path in all_games:
            print(f"{game_name} - {game_path}")
    else:
        print("No games found.")


run_game_search()
