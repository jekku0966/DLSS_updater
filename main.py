import dlss_downloader
import get_game_dirs


if __name__ == '__main__':

    print(dlss_downloader.get_dlss_data())
    for game_name, directory in get_game_dirs.scan_steam_games():
        print(game_name, directory)
