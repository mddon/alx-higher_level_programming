#!/usr/bin/python3
"""Script that defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with self.real."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with self.real."""
        return self.real == value
