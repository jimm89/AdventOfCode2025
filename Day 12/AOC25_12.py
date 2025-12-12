# open the file
import sys
read = sys.stdin.read
f = open("AOC25_12_in.txt")

inp = f.read().split('\n\n')

ans = 0

cases = inp[-1].split('\n')

for case in cases:
    idx = case.index(':')
    w, h = map(int, case[:idx].split('x'))
    nums = list(map(int, case[idx + 2:].split()))
    if sum(nums) <= (w // 3) * (h // 3):
        ans += 1
    
print(ans)
    