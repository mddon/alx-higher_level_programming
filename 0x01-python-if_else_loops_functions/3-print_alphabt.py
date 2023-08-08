#!/usr/bin/python3
for ascii_alphabet in range(97, 123):
    if (ascii_alphabet != 101 and ascii_alphabet != 113):
        print("{:c}".format(ascii_alphabet), end='')
