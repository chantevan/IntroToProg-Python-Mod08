# ------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# Chantal Van den bussche, 3/25/2025, Created Script
# Chantal Van den bussche, 3/26/2025, Edited Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    """
    A class that tests menu choice input and employee data input

    ChangeLog:
    Chantal Van den bussche, 3/26/2025, Created class
    """

    def setUp(self):
        """
        This method establishes a list for testing.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/2025, Created method
        """
        self.employee_data = []

    def test_input_menu_choice(self): # Simulate user input '2' and check if the function returns '2'
        """
        This method tests menu choice input.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/2025, Created method
        """
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        """
        This method tests Employee data input.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/225, Created method
        """
        with patch('builtins.input', side_effect=['Chantal', 'Vandenbussche',
                                                  '2025-03-25', 1]):
            IO.input_employee_data(self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'Chantal')
            self.assertEqual(self.employee_data[0].last_name, 'Vandenbussche')
            self.assertEqual(self.employee_data[0].review_date, '2025-03-25')
            self.assertEqual(self.employee_data[0].review_rating, 1)
        # Simulate invalid date input
        with patch('builtins.input', side_effect=['David', 'Nguyen',
                                                  'INVALID DATE', 1]):
            IO.input_employee_data(self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input
        # Simulate invalid rating input (not an int)
        with patch('builtins.input', side_effect=['David', 'Nguyen',
                                                  '2025-03-25', 'INVALID RATING']):
            IO.input_employee_data(self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()