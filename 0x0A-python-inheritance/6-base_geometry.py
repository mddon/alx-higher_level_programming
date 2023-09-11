#!/usr/bin/python3
"""Script that defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Calculate the area of the geometry.
        Raises:
            Exception: This method is not implemented.
        Note:
            Subclasses should implement this method to calculate the area of the specific geometry.
        """
        raise Exception("area() is not implemented")
