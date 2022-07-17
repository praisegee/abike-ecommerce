import random

def generate_id():
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unique_id = str(random.randint(10000000, 99999999))
    unique_id += random.choice(alphabets) + random.choice(alphabets)
    return unique_id
