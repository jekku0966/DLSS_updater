import requests
import pandas as pd


def get_dlss_data():
    dlss_data = "https://raw.githubusercontent.com/beeradmoore/dlss-archive/main/dlss_records.json"
    data = requests.get(dlss_data)
    dlss_stable = data.json()['stable']
    dlss_dataframe_full = pd.DataFrame.from_dict(dlss_stable)

    dlss_dataframe = dlss_dataframe_full[['version', 'additional_label', 'download_url', 'is_signature_valid']]
    dlss_dataframe = dlss_dataframe.loc[dlss_dataframe['is_signature_valid'] == True]
    return dlss_dataframe.sort_values('version', ascending = False, ignore_index = True)