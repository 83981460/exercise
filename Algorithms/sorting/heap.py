'''
Created on Dec 5, 2014

@author: ylyang
'''

'''
1. in line 15, the index of node n's children are 2*n+1 and 2*n+2
2. in line 19 to 23, when heapify, the largest among three (1 father, 2 children) is moved to father
'''

from sorting import generate_array

def heapify(raw, idx, lmt):
    left = idx * 2 + 1
    right = idx * 2 + 2
    large_value = raw[idx]
    large_idx = idx
    if left <= lmt and raw[left] > large_value:
        large_value = raw[left]
        large_idx = left
    if right <= lmt and raw[right] > large_value:
        large_idx = right
    if large_idx != idx:
        buf = raw[idx]
        raw[idx] = raw[large_idx]
        raw[large_idx] = buf
        heapify(raw, large_idx, lmt)

def build_heap(raw, left, right):
    i = (left + right) / 2
    while i >= left:
        heapify(raw, i, right)
        i-=1
        
def heap(raw, left, right):
    i = right
    while(i >= left):
        build_heap(raw, left, i)
        buf = raw[i]
        raw[i] = raw[0]
        raw[0] = buf
        i-=1
        

if __name__ == "__main__":
    raw = generate_array(10)
    print raw
#     heapify(raw, (len(raw)-1)/2, len(raw)-1)
#     build_heap(raw, 0, len(raw)-1)
    heap(raw, 0, len(raw)-1)
    print raw
    
    