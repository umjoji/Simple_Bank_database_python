import random


def phone_number_generator():
        """A program that generates random phone numbers
        using the Nigerian standard of numbering"""
        network_code = ""
        network_codes = []
        for i in range(2, 20): 
                if i < 10:
                        network_code = "080" + str(i)
                else: 
                        network_code = "08" + str(i)
                network_codes.append(network_code)
        
        network_code = random.choice(network_codes)
        for i in range(7):      # because the first four digits are already defined
                network_code += str(random.randint(0, 9))       # choose a random number from 0 to 9
        
        # format number in 08xx xxx xxxx
        number = "{} {} {}".format(network_code[:4], network_code[4:7], network_code [7:])

        return number   

        # number = ""
        # for i in range(100):
        
        # number = phone_number_generator(code)
        # print()
        

