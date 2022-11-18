"""Generates customer ID"""

import random

def cust_id_generator(first_digit):     #takes first digit for customer id
        for i in range(5):
                first_digit += str(random.randint(0, 9))

        return first_digit
