'''
Created on Dec 6, 2014

@author: ylyang
'''

"""
1. bucket can't be list, or bucket[raw[i]/100] will list index of range
2. when dictionry's key are int, they are naturally sorted?
3. in line 27, the why to iteration
"""

from sorting import generate_array
from insertion import insertion

def bucket(raw):
    bucket = {}
    i = 0
    while(i < len(raw)):
        k = raw[i]/100
        if bucket.has_key(k):
            bucket[k].append(raw[i])
        else:
            bucket[k] = [raw[i]]
        i+=1
    i = 0
    for k in bucket:
        curr = bucket[k]
        insertion(curr)
        for n in curr:
            raw[i] = n
            i+=1
        
    
    
if __name__ == "__main__":
    raw = generate_array(10)
    print raw
    bucket(raw)
    print raw