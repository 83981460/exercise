'''
Created on Dec 3, 2014

@author: ylyang
'''

"""
1. in line 14, start from i = 1
"""

from sorting import generate_array

def insertion(raw):
    i = 1
    while i < len(raw):
        buf = raw[i]
        while(i > 0 and raw[i-1] > buf):
            raw[i] = raw[i-1]
            i-=1
        raw[i] = buf
        i+=1
    return raw

if __name__ == "__main__":
    raw = generate_array(10)
    print raw
    print insertion(raw)
