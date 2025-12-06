# open the file
import sys
read = sys.stdin.read
f = open("AOC25_6_in.txt")

# this time, instead, we list out character by character, since the number of spaces is important
chars = [list(x) for x in f.read().split('\n')]

NN = len(chars) # number of rows
MM = len(chars[NN - 1]) # number of cols

# create answer variable
ans = 0

# start at column 0, and continue until we've reached the last column
j = 0
while j < MM:
    
    # left is the start of our current problem
    left = j
    
    # find the end of our current problem by continuing until the next character are our operations row is no longer a space, or if we've reached the end of the row
    while (j + 1 < MM and chars[NN - 1][j + 1] == ' ') or j + 1 == MM:
        j += 1
    
    # right is the space after our current problem
    right = j
    
    # our numbers are in cols [left, right - 1]
    # I can use a technique called list comprehension to easily read all the numbers vertically at once
    nums = [''.join([chars[i][col] for i in range(NN - 1) if chars[i][col] != ' ']) for col in range(left, right)]
    op = chars[NN - 1][left]
    
    # evaluate the resulting expression and add to our answer
    ans += eval(op.join(nums))
       
    # start again at the next character for the next problem
    j = right + 1

print(ans)