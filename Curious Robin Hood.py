import sys, os, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0) 
inf = 10**18
mod = 1000000007 

# https://lightoj.com/problem/curious-robin-hood

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def get_int(): 
    return int(sys.stdin.readline())

def get_ints(): 
    return map(int, sys.stdin.readline().split())

def get_list(): 
    return list(map(int, sys.stdin.readline().split()))

def get_string(): 
    return sys.stdin.readline().rstrip()

def get_words(): 
    return sys.stdin.readline().split()

def fast_print(ans):
    sys.stdout.write(str(ans) + '\n')

def print_list(arr):
    sys.stdout.write(" ".join(map(str, arr)) + '\n')


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


# We maintain the arr locally so we can directly 
# access the current value of a sack without needing 
# to reverse-calculate it from the tree

def solve():
    n, q = get_ints()
    arr = get_list()
    
    # Initialize the Fenwick Tree
    ft = FenwickTree(n)
    
    # Build the tree initially
    for i in range(n):
        if arr[i] > 0:
            ft.add(i + 1, arr[i])
    
    for _ in range(q):
        task = get_list()
        
        if task[0] == 1:
            i = task[1]
            val = arr[i]
            arr[i] = 0           # Empty the local sack tracking
            if val > 0:
                ft.add(i + 1, -val) # Remove amount from Fenwick tree
            fast_print(val)
            
        elif task[0] == 2:
            i, v = task[1], task[2]
            arr[i] += v          # Add to local tracking
            if v > 0:
                ft.add(i + 1, v)    # Add amount to Fenwick tree
                
        elif task[0] == 3:
            l, r = task[1], task[2]
            # Range sum is prefix(r) - prefix(l-1)
            # Offset by +1 for 1-based Fenwick tree indexing
            ans = ft.query(r + 1) - ft.query(l)
            fast_print(ans)

if __name__ == '__main__':
    # multiple test cases
    t = get_int()
    for i in range(1, t + 1):
        fast_print(f"Case {i}:")
        solve()
    
    # single test case
    # solve()