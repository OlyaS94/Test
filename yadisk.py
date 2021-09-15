import requests


class YaFolderCreator:
  def __init__(self, token: str):
    self.token = token

  def create_folder(self, folder_name: str):
    HEADERS = {"Authorization": f'OAuth {self.token}'}
    URL = "https://cloud-api.yandex.net/v1/disk/resources"
    response = requests.put(URL, params={"path": '/' + folder_name}, headers=HEADERS)
    return response