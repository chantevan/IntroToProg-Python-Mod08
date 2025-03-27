# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08- Processing Classes Module
# # Description: A collection of data processing classes used in Assignment08
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chantal Van den bussche, 3/25/2025, Created script
# Chantal Van den bussche, 3/25/2025, Added script
# ------------------------------------------------------------------------------------------------- #


try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this "
                        "application.")
    else:
        import json
except Exception as e:
    print(e.__str__())


class FileProcessor:
    """
    A collection of processing layer methods that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Chantal Van den bussche, 3/26/2025,Edited docstring
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list,
                                     employee_type: object):
        """
        This method reads data from a json file and loads it into a list of dictionary rows

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: an reference to the Employee class
        :return: list

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created method
        Chantal Van den bussche, 3/26/2025, Edited docstring
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)
                    # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name=employee["FirstName"]
                    employee_object.last_name=employee["LastName"]
                    employee_object.review_date=employee["ReviewDate"]
                    employee_object.review_rating=employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this "
                                    "script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        This method writes data to a json file with data from a list of dictionary rows

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file
        :return: None

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created method
        Chantal Van den bussche, 3/26/2025, Edited docstring
        """
        try:
            list_of_dictionary_data: list = []
            # Convert List of employee objects to list of dictionary rows.
            for employee in employee_data:
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")
