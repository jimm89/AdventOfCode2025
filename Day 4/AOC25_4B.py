# open the file, and import required functions and libraries - this time including 'deque' from collections, which we will need for bread-first search (BFS)
import sys
from collections import deque
read = sys.stdin.read
f = open("AOC25_4_in.txt")

# create a proper matrix structure for the grid
rolls = [list(x) for x in f.read().split('\n')]

# define a function to count valid neighbours
def count_neighbours(x, y):
    tot = 0
    
    # a neighbour can be -1, 0 or 1 away in the x direction
    for dx in range(-1, 2):
    
        # if the x-shift takes us out of range (because we were at the edge of the grid), we do not consider this value
        if x + dx < 0 or x + dx >= len(rolls):
            continue
        
        # a neighbour can be -1, 0 or 1 away in the y direction
        for dy in range(-1, 2):
            
            # if the y-shift takes us out of range (because we were at the edge of the grid), we do not consider this value
            if y + dy < 0 or y + dy >= len(rolls[x]):
                continue
            
            # if there is no shift at all, it is not a neighbour, it is the cell itself, so ignore
            if dx == dy == 0:
                continue
            
            # if the neighbouring cell contains '@', then it is a roll
            if rolls[x + dx][y + dy] == '@':
                tot += 1
    return tot

# define a function to retrieve all neighbouring rolls which are next to fewer than 4 rolls themselves
def get_neighbouring_rolls(x, y):
    
    # create an array to store the valid rolls
    valid_neighbours = []
    
    # use the same shift logic as in count_neighbours
    for dx in range(-1, 2):
        if x + dx < 0 or x + dx >= len(rolls):
            continue
        for dy in range(-1, 2):
            if y + dy < 0 or y + dy >= len(rolls[x]):
                continue
            if dx == dy == 0:
                continue
            
            # this time we're checking whether the cell contains '@' AND whether it has fewer than 4 neighbouring rolls itself
            # if so we add it to our valid neighbouring rolls array
            if rolls[x + dx][y + dy] == '@' and count_neighbours(x + dx, y + dy) < 4:
                valid_neighbours.append((x + dx, y + dy))
    
    return valid_neighbours

ans = 0

# for BFS, we will use a queue structure called a deque, which allows us to efficiently remove the first element
# note that a regular array is much less efficient at doing this, due to the data structure type and the way it allocates values into memory
Q = deque()

# iterate over all cells in the grid
for i in range(len(rolls)):
    for j in range(len(rolls[i])):
        
        # using count_neighbours function, add cells to our queue if they are a roll with fewer than 4 neighbours
        if rolls[i][j] == '@' and count_neighbours(i, j) < 4:
            Q.append((i, j))

# this is the BFS: while there remain rolls in our queue for removal, we continue
while Q:
    # take the front roll in the queue
    i, j = Q.popleft()
    
    # if we've processed this roll already, we don't need to do it again
    if rolls[i][j] == '.':
        continue
    
    # if we haven't processed already, we add one to our count of removed rolls
    ans += 1
    
    # we then set this cell to '.' to reflect the fact there is no longer a roll there
    rolls[i][j] = '.'
    
    # finally, we re-examine its neighbours, and add any valid ones back to our queue
    for x, y in get_neighbouring_rolls(i, j):
        Q.append((x, y))

print(ans)