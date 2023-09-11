#!/usr/bin/python3
'''Script that defines a custom list class called MyList, which inherits from
the built-in list class.'''


class MyList(list):
    '''MyList - A custom list class that extends the built-in list class.'''

    def print_sorted(self):
        '''Prints the elements of the list in ascending order.'''

        print(sorted(self))
