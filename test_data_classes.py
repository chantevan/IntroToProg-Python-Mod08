# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08- Test Data Classes Module
# # Description: A collection of tests for the data classes module used in Assignment08
# ChangeLog: (Who, When, What)
# Chantal Van den bussche, 3/25/2025, Created script
# Chantal Van den bussche, 3/26/2025, Edited script
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    '''
    A class representing test person data

    ChangeLog:
    Chantal Van den bussche, 3/25/2025, Created class
    '''

    def test_person_init_(self): # Test the constructor
        """
        This method tests the constructor of Person class

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Edited method and added docstring
        """
        person = Person("Chantal", "Vandenbussche")
        self.assertEqual(person.first_name, "Chantal")
        self.assertEqual(person.last_name, "Vandenbussche")

    def test_person_invalid_name(self): # Test name validations
        """
        This method tests first and last name validation of Person class

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        with self.assertRaises(ValueError):
            person = Person("111", "Vandenbussche")
            with self.assertRaises(ValueError):
                person = Person("Chantal", "111")

    def test_person_str(self): # Test the __str__() magic method
        """
        This method tests the __str__() magic method of Person class.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        person = Person("Chantal", "Vandenbussche")
        self.assertEqual(str(person), "Chantal,Vandenbussche")


class TestEmployee(unittest.TestCase):
    '''
    A class representing test employee data

    ChangeLog:
    Chantal Van den bussche, 3/25/2025, Created class
    '''

    def test_student_init(self): # Test the constructor
        """
        This method tests the constructor of Employee class.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        employee = Employee("David", "Nguyen", "2025-03-25", 5)
        self.assertEqual(employee.first_name, "David")
        self.assertEqual(employee.last_name, "Nguyen")
        self.assertEqual(employee.review_date, "2025-03-25")
        self.assertEqual(employee.review_rating, 5)

    def test_review_date_type(self): # Test the review date validation
        """
        This method tests review date validation of Employee class.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        with self.assertRaises(ValueError):
            employee = Employee("Chris", "Kennedy", "INVALID DATE", 1)

    def test_review_rating_type(self): # Test review rating validation
        """
        This method tests review rating type validation of Employee class.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        with self.assertRaises(ValueError):
            employee = Employee("Chris", "Kennedy", "2025-03-25", "1")

    def test_review_rating_range(self): # Test review rating range validation
        """
        This method tests review rating range validation of Employee class.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        with self.assertRaises(ValueError):
            employee = Employee("Chris", "Kennedy", "2025-03-25", 6)

    def test_student_str(self): # Test the __str__() magic method
        """
        This method tests the __str__() magic method of Employee class

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/25/2025, Created method
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        employee = Employee("Zach", "Maly", "2025-03-25", 3)
        self.assertEqual(str(employee),"Zach,Maly,2025-03-25,3")


if __name__ == '__main__':
    unittest.main()