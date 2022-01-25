from createFolder import creating_new_folder_yandex_disk, delete_folder_yandex_disk
import unittest

class TestControlPanelUnitTest(unittest.TestCase):

    def testCreateFolder(self):
        self.assertEqual(creating_new_folder_yandex_disk('test'), 201)

    def testDeleteFolder(self):
        self.assertEqual(delete_folder_yandex_disk('test'), 204)
