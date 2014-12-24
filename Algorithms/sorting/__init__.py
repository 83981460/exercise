import random

def generate_array(n):
    i = 0
    raw = []
    while i < n:
        raw.append(random.randint(0,1000))
        i+=1
    return raw