# open the file
import sys
read = sys.stdin.read
f = open("AOC25_8_in.txt")

# read in the co-ordinates
points = [list(map(int, x.split(','))) for x in f.read().split('\n')]

# define a function that calculates the square distance between two points
def sq_dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

# find the ultimate parent of point a
def find(a):
    
    # the ultimate parent is found when its parent is itself
    if a != p[a]:
        p[a] = find(p[a])
    
    return p[a]

# join points a and b
def union(a, b):
    
    # we're actually joining the ultimate parents of a and b
    a, b = find(a), find(b)
    
    # if they have the same ultimate parent, these sets are already joined, so we end here
    if a == b:
        return
    
    # we want to merge the smaller set into the bigger set, to ensure fewer updates are required
    if size[a] > size[b]:
        a, b = b, a
    
    # make b the ultimate parent of a, and this will make b the ultimate parent of all 'a's children too
    p[a] = b
    
    # increase the size of b's set, and make a's size 0 to remove a from consideration as a circuit
    size[b] += size[a]
    size[a] = 0
    
    return
    
# N is the number of points we have
N = len(points)

# initially define each point's parent as itself, and put it in a set of size 1 on its own
p = [i for i in range(N)]
size = [1]*N

# create an array called order to store the Euclidean distances
order = [(sq_dist(points[i], points[j]), i, j) for i in range(N) for j in range(i + 1, N)]

# sort order by descending square distance so that the shortest distance is at the end
order.sort(reverse = True)

# perform a loop that continues we tell it otherwise (using 'break'), taking the shortest distance from the end each time
while True:
    
    # take the two points with the shortest remaining distance
    d, i, j = order.pop()
    
    # join them (if necessary)
    union(i, j)

    # i and j now have the same ultimate parent - if this ultimate parent's set size is N, then we have joined all points together, so we print the answer and stop
    if size[find(i)] == N:
        print(points[i][0] * points[j][0]) # multiply x-coordinates of i and j
        break