# open the file
import sys
read = sys.stdin.read
f = open("AOC25_7_in.txt")

# read in the grid into a 2-d list
grid = [list(x) for x in f.read().split('\n')]

# get the length n and the width m
n = len(grid)
m = len(grid[0])

# create an answer variable
ans = 0

# using the information in each row up to and including the penultimate one, we populate the contents of the subsequent row
for i in range(n - 1):
    for j in range(m):
        
        # we only need to do anything if there's a beam in the cell, for which we use the letter 'S' following the precedent set in the first row
        if grid[i][j] == 'S':

            # if there's no splitter, put a beam in the cell below
            if grid[i + 1][j] != '^':
                grid[i + 1][j] = 'S'

            # if there is a splitter, put a beam in the cells to the left and right of it, and we add one to our tally
            elif grid[i + 1][j] == '^':
                ans += 1              
                grid[i + 1][j - 1] = 'S'
                grid[i + 1][j + 1] = 'S'

print(ans)