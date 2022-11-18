import random

def bvn_generator():
        """A function that generates BVN numvbers at random"""
        # all BVN start with 22
        bvn = "22"
        for i in range(9):
                bvn += str(random.randint(0, 9))
        
        return bvn
