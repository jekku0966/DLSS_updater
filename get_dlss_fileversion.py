import os
import win32api


def search_file_in_folder(root_folder, target_filename):
    return next(
        (
            os.path.join(root, target_filename)
            for root, dirs, files in os.walk(root_folder)
            if target_filename in files
        ),
        None,
    )


root_folder = 'D:/SteamLibrary/steamapps/common'
target_filename = 'nvngx_dlss.dll'

if result := search_file_in_folder(root_folder, target_filename):
    print(f"File '{target_filename}' found at: {result}")
else:
    print(f"File '{target_filename}' not found in the specified folder.")


def get_dll_version(dll_path):
    try:
        dll_version = win32api.GetFileVersionInfo(dll_path, '\\')
        ms, ls = dll_version['FileVersionMS'], dll_version['FileVersionLS']
        return f"{ms >> 16}.{ms & 0xFFFF}.{ls >> 16}.{ls & 0xFFFF}"
    except Exception:
        return None


dll_path = (r'C:/XboxGames/Ghostwire-Tokyo/Content/Engine/Plugins/Runtime/Nvidia/DLSS/Binaries/ThirdParty/Win64'
            r'/nvngx_dlss.dll')

if version := get_dll_version(dll_path):
    print(f"DLL Version: {version}")
else:
    print("Unable to retrieve DLL version.")
