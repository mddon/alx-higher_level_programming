#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """Override equality and inequality operators."""

    def __eq__(self, value):
        """Override equality operator with inequality behavior."""
        return super().__eq__(value)

    def __ne__(self, value):
        """Override inequality operator with equality behavior."""
        return super().__ne__(value)
