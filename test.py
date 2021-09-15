import unittest
from unittest.mock import patch
import secretary


class TestSecretary(unittest.TestCase):
  def setUp(self):
    print('Testing...')


  def test_check_document_existance(self):
    self.assertEqual(secretary.check_document_existance('2207 876234'), True)
    self.assertEqual(secretary.check_document_existance('uhh'), False)

  @patch('builtins.input')
  def test_get_doc_owner_name(self, user_input):
    user_input.side_effect = ['11-2']
    self.assertEqual(secretary.get_doc_owner_name(), 'Геннадий Покемонов')

  def test_get_all_doc_owners_names(self):
    self.assertEqual(secretary.get_all_doc_owners_names(),{"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})


  def test_remove_doc_from_shelf(self):
    secretary.remove_doc_from_shelf('10006')
    self.assertEqual(secretary.directories['2'],[])

  
  @patch('builtins.input')
  def test_delete_doc(self, user_input):
    user_input.side_effect = ['11-2']
    self.assertEqual(secretary.delete_doc(), ('11-2', True))


  @patch('builtins.input')
  def test_move_doc_to_shelf(self, user_input):
    user_input.side_effect = ['11-2', '3']
    secretary.move_doc_to_shelf()
    self.assertEqual(secretary.directories['3'],['11-2'])


  def test_show_document_info(self):
    self.assertEqual(secretary.show_document_info('11-2'),'invoice "11-2" "Геннадий Покемонов"')


  def tearDown(self):
    print('Testing complete!')

if __name__ == '__main__':
  unittest.main()