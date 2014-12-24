'''
Created on Dec 4, 2014

@author: ylyang
'''

"""
1. in line 32~34 the pivot is excluded from both recursion
2. in line 25, j need to be minus 1 before return as pivot position
"""

from sorting import generate_array

def partition(raw, left, right):
    pivot = raw[right]
    i = left
    j = left
    while i <= right:
        if raw[i] <= pivot:
            buf = raw[j]
            raw[j] = raw[i]
            raw[i] = buf
            j+=1
        i+=1
    j-=1
    return j

def find_k(raw, k, left, right):
    idx = partition(raw, left, right)
    if idx == k:
        return idx
    if idx < k:
        return find_k(raw, k, idx+1, right)
    if idx > k:
        return find_k(raw, k, left, idx-1)
    
def median(raw, left, right):
    if left >= right:
        return
    med = find_k(raw, (left+right)/2, left, right)
    median(raw, left, med-1)
    median(raw, med+1, right)
    

if __name__ == "__main__":
    raw = generate_array(10)
    print raw
#     print partition(raw, 5, len(raw)-1)
#     print find_k(raw, 2, 0, len(raw)-1)
    median(raw, 0, len(raw)-1)
    print raw