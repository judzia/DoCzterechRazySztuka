import unittest
from unittest.mock import patch, mock_open
from main import export_attendance


class TestExportAttendance(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)  # students list has data
    def test_export_students(self, mock_file):
        students = [
            {"first_name": "John", "last_name": "Doe", "present": True},
            {"first_name": "Jane", "last_name": "Smith", "present": False},
        ]
        export_attendance(students)
        mock_file().write.assert_any_call("John,Doe,yes\n")
        mock_file().write.assert_any_call("Jane,Smith,no\n")

    @patch("builtins.open", new_callable=mock_open)  # students list has no data :o
    def test_export_empty_list(self, mock_file):
        students = []
        export_attendance(students)
        mock_file().write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
