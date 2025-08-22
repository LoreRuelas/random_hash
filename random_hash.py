import random

def find00_in1000Attempts():

    for attempt in range(0, 1000):
        hash_val = ''.join(random.choice('0123456789abcdef') for _ in range(32))
        
        if hash_val.startswith("00"):
            return True

    return False
