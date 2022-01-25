from main import get_name, del_doc, add_new_doc
import unittest

class TestControlPanelUnitTest(unittest.TestCase):

    def testGetName(self):
        self.assertEqual(get_name('11-2'), 'Геннадий Покемонов')

    def testDelDoc(self):
        self.assertTrue(del_doc('2207 876234'))


    def testAddNewDoc(self):
        self.assertEqual(add_new_doc('4545', 'passport', 'Ivan', 3), 3)
