"""Generaates addresses using random"""

import random
from name_generator import *

def address_generator():
        # get city names from file
        f = open("list_cities_nigeria.csv", "r")
        cities = []
        cities = f.readlines()
        cities.remove(cities[0])
        # give seed name
        street_name = name_generator("Nsukara")
        street_number = random.randint(1, 280)
        city = random.choice(cities)
        # format address
        address = "{} {} street, {}.".format(street_number, street_name, city)

        return address


# print(address_generator())
