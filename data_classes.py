# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08- Data Classes Module
# # Description: A collection of data classes used for Assignment08
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chantal Van den bussche, 3/25/2025, Created script
# Chantal Van den bussche, 3/25/2025, Edited script
# Chantal Van den bussche, 3/25/2025, Added script
# ------------------------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this "
                        "application.")
    else:
        from datetime import date
except Exception as e:
    print(e.__str__())

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'
MENU: str = ''' 
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''
employees: list = []  # a table of employee data
menu_choice = ''


class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    - Chantal Van den bussche, 3/25/2025: Added docstring to methods
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        This constructor set Person objects attribute default values when Person object is created.

        :param first_name:
        :param last_name:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        This method holds and returns capitalized first name of Person object.

        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        This method validates Person object's first name contains alphabetical letters only.

        :param value:
        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """
        This method holds and returns capitalized last name of Person object.

        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        This method validates Person object's last name contains alphabetical letters only.

        :param value:
        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """
        This method returns comma-separated string for Person object class.

        :return:

        ChangeLog:
        Chantal Van den bussche, 3/26/2025, Added docstring
        """
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "",
                 review_date: str = "1900-01-01", review_rating: int = 3):
        """
        This constructor sets Employee objects attribute value when Employee object is created.
        
        :param first_name: 
        :param last_name: 
        :param review_date: 
        :param review_rating:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        super().__init__(first_name=first_name,last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        This method holds and returns Employee object's review dates

        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        This method validates Employee object's review date is of correct format.

        :param value:
        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        This method holds and returns Employee object's review rating.

        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        """
        This method validates Employee object's review rating is of an acceptable rating.

        :param value:
        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        """
        This method returns comma-separated string for Employee object class.

        :return:

        ChangeLog:
        - Chantal Van den bussche, 3/26/2025: Added docstring
        """
        return (f"{self.first_name},{self.last_name},{self.review_date},"
                f"{self.__review_rating}")

