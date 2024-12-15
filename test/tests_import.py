import unittest
from unittest.mock import patch, mock_open
from main import *  #  importing functions

class TestImportFromFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="John,Doe,yes\nJane,Smith,no\n") # file exists and has correct data
    def test_import_valid_file(self, mock_file):
        students = import_from_file()
        expected = [
            {"first_name":"John", "last_name":"Doe","present":True},
            {"first_name":"Jane", "last_name":"Smith","present":False},
        ]
        self.assertEqual(students, expected)

    @patch("builtins.open", new_callable=mock_open, read_data="")  # file is empty :(
    def test_import_empty_file(self, mock_file):
        students = import_from_file()
        self.assertEqual(students, [])

    @patch("builtins.open", side_effect=FileNotFoundError) # file does not exist :p
    def test_import_file_not_found(self, mock_file):
        students = import_from_file()
        self.assertEqual(students, [])

    @patch("builtins.open", new_callable=mock_open, read_data="InvalidData") # invalid data >:(
    def test_import_invalid_data(self, mock_file):        
        students = import_from_file()
        self.assertEqual(students, []) # in case of invalid data -> empty list 

if __name__ == "__main__":
    unittest.main()
