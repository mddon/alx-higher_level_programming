#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)


if number >= 0:
last_digit = number % 10
else:
last_digit = ((number * -1) % 10) * -1

output = "Last digit of %d is %d and is" % (number, last_digit)

if last_digit == 0:
    print(output, "0")
elif last_digit > 5:
    print(output, "greater than 5")
else:
    print(output, "less than 6 and not 0")
