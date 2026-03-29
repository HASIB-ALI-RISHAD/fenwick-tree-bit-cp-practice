import sys, os, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0) 
inf = 10**18
mod = 1000000007 

# https://cses.fi/problemset/task/1651/

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

def solve():
    n, q = get_ints()
    arr = get_list()
    
    # Initialize the Fenwick Tree.
    # We use size n + 1 because a range update up to 'b' 
    # requires us to subtract the delta at index 'b + 1'.
    ft = FenwickTree(n + 1)
    
    for _ in range(q):
        task = get_list()
        
        if task[0] == 1:
            # Range update
            a, b, u = task[1], task[2], task[3]
            ft.add(a, u)           # Add 'u' from index 'a' onwards
            ft.add(b + 1, -u)      # Remove 'u' from index 'b+1' onwards
            
        elif task[0] == 2:
            # query
            k = task[1]
            # The actual value is the original array value + all overlapping updates
            # arr is 0-indexed, so we use k - 1
            ans = arr[k - 1] + ft.query(k)
            fast_print(ans)


if __name__ == '__main__':
    # multiple test cases
    # t = get_int()
    # for _ in range(t):
    #     solve()
    
    # single test case
    solve()