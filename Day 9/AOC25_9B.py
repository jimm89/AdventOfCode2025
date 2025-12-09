# open the file
import sys
read = sys.stdin.read
f = open("AOC25_9_in.txt")

# read in the co-ordinates
P = [list(map(int, x.split(','))) for x in f.read().split('\n')]

# create answer variable
ans = 0

# call L the number of points
L = len(P)

# iterate over all pairs (x1, y1) and (x2, y2) as potential opposite corners of the rectangle
for i in range(L):
    for j in range(i + 1, L):
        
        # sort the x coordinates and then the y coordinates (note that the doesn't change the potential grid at all)
        x1, x2 = sorted([P[i][0], P[j][0]])
        y1, y2 = sorted([P[i][1], P[j][1]])
        
        # now, for each possible line segment connecting two points, check whether it encroaches into the grid (not just on the boundary)
        for k in range(L):

            # again sort the x coordinates and then the y coordinates
            x3, x4 = sorted([P[k][0], P[(k + 1) % L][0]])
            y3, y4 = sorted([P[k][1], P[(k + 1) % L][1]])
            
            # if any part of any line enters the potential grid 'fully' (breaks through the boundary), this grid is not possible, so end the search here
            if x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2:
                break
        
        # if no part of any line enters the potential grid 'fully', this is a candidate answer
        else:
            ans = max(ans, (x2 - x1 + 1) * (y2 - y1 + 1))

print(ans)