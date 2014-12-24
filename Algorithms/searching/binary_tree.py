'''
Created on Dec 9, 2014

@author: ylyang
'''

from sorting import generate_array
import random

class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(raw):
    root = Node(raw[0])
    i = 1
    while i < len(raw):
        r = root
        while True:
            if r.value >= raw[i]:
                if r.left is not None:
                    r = r.left
                    continue
                else:
                    r.left = Node(raw[i])
                    break
            if r.value < raw[i]:
                if r.right is not None:
                    r = r.right
                    continue
                else:
                    r.right = Node(raw[i])
                    break
        i+=1
    return root

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print root.value
    in_order(root.right)
    
def search(raw, target):
    root = build_tree(raw)
    while root is not None:
        if root.value == target:
            return True
        if root.value > target:
            root = root.left
            continue
        if root.value < target:
            root = root.right
    return False

if __name__ == "__main__":
    raw = generate_array(10)
    print raw
    print search(raw, raw[random.randint(0,9)])
    print search(raw, 33)