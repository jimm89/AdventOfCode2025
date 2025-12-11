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

global dac, fft
dac = index_lookup['dac']
fft = index_lookup['fft']

@cache
def dfs(u, vis_dac = False, vis_fft = False):
    
    global dac, fft
    
    if u == n:
        
        if vis_dac and vis_fft:
            
            return 1
        
        return 0
    
    ret = 0
    
    for v in G[u]:
       
        ret += dfs(v, vis_dac or (v == dac), vis_fft or (v == fft))
    
    return ret

print(dfs(index_lookup['svr']))