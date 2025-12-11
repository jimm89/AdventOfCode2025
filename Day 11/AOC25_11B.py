# open the file
import sys
from collections import defaultdict as dd
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


dfs_store = [[[-1 for k in range(2)] for j in range(2)] for i in range(n + 1)]

def dfs(u, vis_dac = False, vis_fft = False):
    
    global dac, fft
    
    if dfs_store[u][vis_dac][vis_fft] != -1:
        return dfs_store[u][vis_dac][vis_fft]
    
    if u == n:
        
        if vis_dac and vis_fft:
            
            return 1
        
        return 0
    
    ret = sum(dfs(v, vis_dac or (v == dac), vis_fft or (v == fft)) for v in G[u])
    
    dfs_store[u][vis_dac][vis_fft] = ret
    
    return ret

print(dfs(index_lookup['svr']))