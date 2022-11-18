

import random

def name_generator(name):
        """Generates names from the alphabet, using a template name"""
        new_name = ""
        for char in name:
                # print(char)
                # switch is used to add uppercase to name
                if char.isupper():
                        switch = 1
                else:
                        switch = 0
                # change character to lowercase
                char = char.lower()
                # print(char)
                # if a vowel
                if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                        # and if uppercase
                        if switch:
                                new_name += random.choice(["a", "e", "i", "o", "u"]).upper()
                        else:
                                new_name += random.choice(["a", "e", "i", "o", "u"])
                # add space
                elif char == " ":
                        new_name += char
                else:
                        consonants = []
                        for i in range(65, 91):
                                consonants.append(chr(i))
                        for letter in consonants:
                                if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
                                        consonants.remove(letter)
                        
                        if switch:
                                new_name += random.choice(consonants)
                        else:
                                new_name += random.choice(consonants).lower()
                                
        return new_name

# for i in range(1000):
#         print(name_generator("George Akanimoh"))