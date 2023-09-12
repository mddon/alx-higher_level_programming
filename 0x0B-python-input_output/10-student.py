#!/usr/bin/python3
"""This script defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        Methods:
        - to_json(self, attrs=None): Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list, optional): List of attribute names to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary representation of the Student object.

        """
        if attrs is None:
            return self.__dict_
        return {key: value for key, value in self.__dict__.items() if key in attrs}_
