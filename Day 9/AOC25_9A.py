# open the file
import sys
read = sys.stdin.read
f = open("AOC25_9_in.txt")

# read in the co-ordinates
P = [list(map(int, x.split(','))) for x in f.read().split('\n')]

# create answer variable
ans = 0

# call L the number the points
L = len(P)

# iterate over all pairs (x1, y1) and (x2, y2) as opposite corners of the rectangle
for i in range(L):
    x1, y1 = P[i]
    
    for j in range(i + 1, L):
        x2, y2 = P[j]
        
        # update the answer with the corresponding grid area if greater than the current answer
        ans = max(ans, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

print(ans)