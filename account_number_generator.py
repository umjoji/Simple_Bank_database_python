"""Generates account numbers for clients"""

import random

def account_number_generator(first_digit):
        for i in range(9):
                first_digit += str(random.randint(0, 9))

        return first_digit