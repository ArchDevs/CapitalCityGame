import random
from db import country_capitals

def shuffle_countries():
    countries = list(country_capitals.keys())
    random.shuffle(countries)
    return countries

def get_user_input(user_input, country, capital):
    if user_input.lower() == capital.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False
