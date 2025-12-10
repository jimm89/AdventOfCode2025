# open the file
import sys
read = sys.stdin.read
f = open("AOC25_10_in.txt")

inp = [x.split() for x in f.read().split('\n')]

ans = 0

for lights, *keys, joltage in inp:
    
    lights = lights[1:-1]
    L = len(lights)
    
    keys = [list(map(int, key[1:-1].split(','))) for key in keys]
    
    target = 0
    for i in range(L):
        if lights[i] == '#':
            target += (1 << i)
    
    tmp_ans = 100
    
    for mask in range(1 << len(keys)):
        curr = 0
        for i, key in enumerate(keys):
            if (mask & (1 << i)):
                for switch in key:
                    curr ^= (1 << switch)
        if curr == target:
            tmp_ans = min(tmp_ans, mask.bit_count())
    
    ans += tmp_ans

print(ans)
        