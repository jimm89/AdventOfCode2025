# open the file
import sys
read = sys.stdin.read
f = open("AOC25_7_in.txt")

# read in the grid into a 2-d list
grid = [list(x) for x in f.read().split('\n')]

# get the length n and the width m
n = len(grid)
m = len(grid[0])

# initialise an array which tells us how many paths are currently in each column
# at first, the only path is in the cell marked 'S' in the input file, so we set that cell to 1 and the rest to 0
paths = [0] * m
paths[grid[0].index('S')] = 1

# using the information in each row up to and including the penultimate one, we populate the contents of the subsequent row
for i in range(n - 1):
    
    # we will create a new set of paths for the subsequent row
    new_paths = [0] * m
    
    for j in range(m):
        
        # we only need to do anything if there's a beam in the cell, for which we use the letter 'S' following the precedent set in the first row
        if grid[i][j] == 'S':
            
            # if there's no splitter, put a beam in the cell below, and add the paths from that column to the same column in new_paths 
            if grid[i + 1][j] != '^':
                grid[i + 1][j] = 'S'
                new_paths[j] += paths[j]
            
            # if there is a splitter, put a beam in the cells to the left and right of it, and we add the paths from our current column to both of those columns
            else:
                new_paths[j - 1] += paths[j]
                new_paths[j + 1] += paths[j]
                grid[i + 1][j - 1] = 'S'
                grid[i + 1][j + 1] = 'S'
    
    # change the values in paths to match new_paths
    paths = new_paths

print(sum(paths))