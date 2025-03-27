# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08- Test Processing Classes Module
# # Description: A collection of tests for the processing classes module used in Assignment08
# ChangeLog: (Who, When, What)
# Chantal Van den bussche, 3/25/2025, Created script
# Chantal Van den bussche, 3/26/2025, Added test_write_employee_data_to_file method
# ------------------------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as data
from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    """
    A class that tests file processing

    ChangeLog:
    Chantal Van den bussche, 3/26/2025, Created class
    """

    def setUp(self):
        """
        This method creates a temporary file for testing.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/2025, Created method
        """
        # Create temp file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        """
        This method cleans up and deletes temp file.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/2025, Created method
        """
        # Clean up & delete temp file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        """
        This method tests the reading of file and translating file fata into objects.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/2025, Created method
        """
        # Create sample data and write into temp file
        sample_data = [{"FirstName": "Chantal", "LastName": "Vandenbussche",
                        "ReviewDate": "2025-03-25", "ReviewRating": 5},
                       {"FirstName": "David", "LastName": "Nguyen",
                        "ReviewDate": "2025-03-25", "ReviewRating": 3}]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)
        # read_employee_data_from_file and check if it returns expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name,
                                                   self.employee_data,
                                                   employee_type=Employee)
        # Assert employee data list contains expected employee objects
        # employee object 0 - Chantal,Vandenbussche,2025-03-25,5
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "Chantal")
        self.assertEqual(self.employee_data[0].last_name,"Vandenbussche")
        self.assertEqual(self.employee_data[0].review_date, "2025-03-25")
        self.assertEqual(self.employee_data[0].review_rating, 5)
        # employee object 1 - David,Nguyen,2025-03-25,3
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[1].first_name, "David")
        self.assertEqual(self.employee_data[1].last_name, "Nguyen")
        self.assertEqual(self.employee_data[1].review_date, "2025-03-25")
        self.assertEqual(self.employee_data[1].review_rating, 3)

    def test_write_employee_data_to_file(self):
        """
        This method tests the writing of Employee objects to JSON file.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/2025, Createed method
        """
        # Create sample employee objects
        sample_data = [
            data.Employee("Chantal","Vandenbussche","2025-03-25",5),
            data.Employee("David","Nguyen","2025-03-25",3)
        ]
        # write_employee_data_to_file & write data to temp file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_data)
        # Read data from temp file & check if matches expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)
        # Assert employee data list contains expected employee objects
        # employee object 0 - Chantal,Vandenbussche,2025-03-25,5
        self.assertEqual(len(file_data), len(sample_data))
        self.assertEqual(file_data[0]["FirstName"], "Chantal")
        self.assertEqual(file_data[0]["LastName"],"Vandenbussche")
        self.assertEqual(file_data[0]["ReviewDate"], "2025-03-25")
        self.assertEqual(file_data[0]["ReviewRating"], 5)
        # employee object 1 - David,Nguyen,2025-03-25,3
        self.assertEqual(len(file_data), len(sample_data))
        self.assertEqual(file_data[1]["FirstName"], "David")
        self.assertEqual(file_data[1]["LastName"], "Nguyen")
        self.assertEqual(file_data[1]["ReviewDate"], "2025-03-25")
        self.assertEqual(file_data[1]["ReviewRating"], 3)

if __name__ == "__main__":
    unittest.main()