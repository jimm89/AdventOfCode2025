# open the file
import sys
from bisect import bisect_left, bisect_right
read = sys.stdin.read
f = open("AOC25_5_in.txt")

# read in the inputs - this is more intricate today; firstly we need to separate the two parts of the input, using .split('\n\n')
# then we parse the two different parts
inp1, inp2 = f.read().split('\n\n')

# Let's process inp1 - the fresh ranges as strings - into a list of ranges [x, y] where x and y are integers
# To do that, we split by '\n' to get each range as a string, then split by '-' to get x and y, mapping those to integers as we did yesterday
fresh_raw = [list(map(int,rng.split('-'))) for rng in inp1.split('\n')]

# Processing the available ingredients is simpler: split again by '\n', then map to integers
available = list(map(int, inp2.split('\n')))

# Sort the ranges of fresh ingredients - this will sort them by x first, then by y
fresh_raw.sort()

# Create a new list into which we'll insert our merged ranges
fresh_processed = []

# Start at the beginning of the array, with index i = 0, and iterate while i remains within the bounds of the array
# i will be our left-most range of those to be merged
# fresh_raw[i][0] - the lower end of this range - will also be the low value of our merged range, since we have sorted by first index already
i = 0
while i < len(fresh_raw):
    
    # Initially the right-most range to be merged is the starting range
    j = i
    
    # Initially the low and high values of this range are the low and high values of the merged range
    curr_min, curr_max = fresh_raw[i]
    
    # iterate over j - while the next range contains any values which intersect with our current range, we include this range
    while j + 1 < len(fresh_raw) and fresh_raw[j + 1][0] <= curr_max:
        j += 1
        
        # update the high end of our merged range if necessary
        curr_max = max(curr_max, fresh_raw[j][1])
    
    # add the final merged range to our new, clean array
    fresh_processed.append([curr_min, curr_max])
    
    # start again at the range immediately after the final one we merged
    i = j + 1

# This big number will have us bisect our array effectively
BIG_NUMBER = 10**18

# This variable will store our answer - for each fresh ingredient, we'll add 1
ans = 0

for ingredient in available:
    # Is this ingredient fresh? Let's bisect the processed list using [ingredient, 10**18] and see if ingredient already sits in the range at that index
    idx = bisect_left(fresh_processed, [ingredient, BIG_NUMBER]) - 1
    if idx >= 0 and fresh_processed[idx][0] <= ingredient <= fresh_processed[idx][1]:
        ans += 1

print(ans)