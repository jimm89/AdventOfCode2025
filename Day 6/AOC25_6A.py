# open the file
import sys
read = sys.stdin.read
f = open("AOC25_6_in.txt")

# split() with no argument by default splits by *any whitespace*, which is perfect for this problem
ops = [x.split() for x in f.read().split('\n')]

N = len(ops) # number of rows
M = len(ops[N - 1]) # number of cols

# create answer variable
ans = 0

# iterate over all problems (each problem has its own column in ops)
for j in range(M):
    
    # get the numbers from each row except the last one
    nums = [ops[i][j] for i in range(N - 1)]
    
    # get the operation from the last row
    op = ops[N - 1][j]
    
    # use join to concatenate nums using op
    # use eval to evaluate the resulting expression
    # add to final answer
    ans += eval(op.join(nums))

print(ans)
