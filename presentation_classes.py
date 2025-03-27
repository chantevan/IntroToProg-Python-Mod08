# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08- Presentation Classes Module
# # Description: A collection of presentation (I/O) classes module used for Assignment08
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chantal Van den bussche, 3/26/2025, Created and added script
# Chantal Van den bussche, 3/26/2025, Added script to import Employee from data_classes
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
except Exception as e:
    print(e.__str__())

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Chantal Van den bussche, 3/26/2025, Edited docstring in methods
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This method displays a custom error messages to the user

        :param message: string with message data to display
        :param error: Exception object with technical message to display
        :return: None

        ChangeLog: (Who, When, What)
        RRoot,1.3.2025,Created method
        Chantal Van den bussche, 3/26/2025, Edited docstring
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """ This method displays the menu of choices to the user

        :return: None

        ChangeLog: (Who, When, What)
        RRoot,1.3.2025,Created method
        Chantal Van den bussche, 3/26/2025, Edited docstring
        """
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """ This method gets a menu choice from the user

        :return: string with the users choice

        ChangeLog: (Who, When, What)
        RRoot,1.3.2025,Created method
        Chantal Van den bussche, 3/26/2025, Edited docstring
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice


    @staticmethod
    def output_employee_data(employee_data: list):
        """ This method displays employee data to the user

        :param employee_data: list of employee object data to be displayed
        :return: None

        ChangeLog: (Who, When, What)
        RRoot,1.3.2025,Created method
        Chantal Van den bussche, 3/26/2025, Edited docstring
        """
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations"

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """ This method gets the first name, last name, review date, and review rating from the user.

        :param employee_data: list of dictionary rows to be filled with input data
        :return: list

        ChangeLog: (Who, When, What)
        RRoot,1.3.2025,Created method
        Chantal Van den bussche, 3/26/2025, Edited docstring
        """

        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
