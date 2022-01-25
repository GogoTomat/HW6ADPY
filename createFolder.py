import requests


YANDEX_TOKEN = ''
URL = "https://cloud-api.yandex.net/v1/disk/resources"

def creating_new_folder_yandex_disk(name_folder: str):
    headers = {
        "Accept": 'application/json',
        'Authorization': YANDEX_TOKEN}
    params = {'path': f'/{name_folder}'}
    res = requests.put(URL, headers=headers, params=params)
    return res.status_code

def delete_folder_yandex_disk(name_folder: str):
    params = {'path': name_folder}
    headers = {'Content-Type': 'application/json',
               'Authorization': YANDEX_TOKEN}
    res = requests.api.delete(URL, headers=headers, params=params)
    return res.status_code
