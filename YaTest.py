import requests
import unittest
from yadisk import YaFolderCreator


class TestYaDisk(unittest.TestCase):
  def setUp(self):
    self.uploader = YaFolderCreator('') #здесь необходимо ввести свой токен

  def test_create_folder(self):
    directory = 'PyTest'
    self.assertEqual(self.uploader.create_folder(directory).status_code, 201)
    folders_resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
    params={"path": '/'},
    headers={"Authorization": f'OAuth {self.uploader.token}'})

        
    folders_list = [f['name'] for f in folders_resp.json().get('_embedded').get('items') if f['type'] == 'dir']
    self.assertIn(directory, folders_list)

  def tearDown(self):
    del self.uploader
    
if __name__ == '__main__':
  unittest.main()
