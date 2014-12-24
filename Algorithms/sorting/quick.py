'''
Created on Dec 4, 2014

@author: ylyang
'''

'''
1. in line 14 the return condition is left >= right, not only right
'''
from median import partition
from sorting import generate_array

def quick(raw, left, right):
    if left >= right:
        return
    pivot = partition(raw, left, right)
    quick(raw, left, pivot-1)
    quick(raw, pivot+1, right)

if __name__ == "__main__":
    raw = generate_array(10)
    print raw
    quick(raw, 0, len(raw)-1)
    print raw