import sqlite3
import requests
import pandas as pd


def get_dlss_data():
    conn = sqlite3.connect('gamedb.db')

    dlss_version_list = "https://raw.githubusercontent.com/beeradmoore/dlss-archive/main/dlss_records.json"
    data = requests.get(dlss_version_list)
    dlss_stable = data.json()['stable']
    dlss_dataframe_full = pd.DataFrame.from_dict(dlss_stable)

    dlss_dataframe = dlss_dataframe_full[['file_description', 'version', 'additional_label', 'download_url', 'is_signature_valid']]
    dlss_dataframe = dlss_dataframe.loc[dlss_dataframe['is_signature_valid'] == True]
    dlss_data = dlss_dataframe.sort_values('version', ascending = False, ignore_index = True)
    dlss_dataframe.to_sql('dlss_data', conn, if_exists = 'replace', index = False)
