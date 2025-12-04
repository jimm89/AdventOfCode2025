# open the file
import sys
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

# create answer variable
ans = 0

# iterate over all cells in the grid
for i in range(len(rolls)):
    for j in range(len(rolls[i])):
        
        # using count_neighbours function, add 1 to our total if there are fewer than 4 neighbouring rolls
        if rolls[i][j] == '@' and count_neighbours(i, j) < 4:
            ans += 1

# print answer
print(ans)
