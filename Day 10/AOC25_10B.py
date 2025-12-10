# open the file
import sys
import z3
read = sys.stdin.read
f = open("AOC25_10_in.txt")

inp = [x.split() for x in f.read().split('\n')]

ans = 0

for lights, *keys, joltage in inp:
    
    keys = [list(map(int, key[1:-1].split(','))) for key in keys]
    
    joltage = list(map(int, joltage[1:-1].split(',')))
    
    coeffs = [z3.Int(f'c{i}') for (i, key) in enumerate(keys) ]
    
    equations = [(v >= 0) for v in coeffs]
    
    for i, jolt in enumerate(joltage):
        to_add = [coeffs[j] for (j, key) in enumerate(keys) if i in key]
        tmp_eq = (sum(to_add) == jolt)
        equations.append(tmp_eq)
    
    opt = z3.Optimize()
    opt.minimize(sum(coeffs))
    
    for eq in equations:
        opt.add(eq)
    
    opt.check()
    
    mod = opt.model()
    for dec in mod.decls():
        ans += mod[dec].as_long()

print(ans)