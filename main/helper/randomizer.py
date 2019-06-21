'''generate random data'''
import random
import string

def random_string(length):
    '''Generate a random string of fixed length'''
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def random_int(lowerLimit, upperLimit):
    '''Generate a random integer'''
    return random.randint(lowerLimit, upperLimit)

def random_bool():
    '''Generate random boolean value'''
    return bool(random.getrandbits(1))
