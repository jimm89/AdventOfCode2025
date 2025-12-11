# open the file
import sys
from collections import defaultdict as dd
from functools import cache
read = sys.stdin.read
f = open("AOC25_11_in.txt")

inp = [x.split() for x in f.read().split('\n')]

global n
n = len(inp)

G = [[] for _ in range(n + 1)]

index_lookup = dd(int)
index_lookup['out'] = n
reverse_index = []

for i, (_in, *_outs) in enumerate (inp):
    index_lookup[_in[:-1]] = i
    reverse_index.append(_in[:-1])

reverse_index.append('out')

for i, (_in, *_outs) in enumerate (inp):
    for _out in _outs:
        G[index_lookup[_in[:-1]]].append(index_lookup[_out])

dfs_store = [-1] * (n + 1)

def dfs(u):
    
    if dfs_store[u] != -1:
        return dfs_store[u]
    
    if u == n:
        return 1
    
    ret = sum(dfs(v) for v in G[u])

    dfs_store[u] == ret
    
    return ret

print(dfs(index_lookup['you']))