# open the file
import sys
read = sys.stdin.read
f = open("AOC25_3_in.txt")

# read in the file, and save the information in an array which we call 'rngs'
# the 'split' function breaks the input file up, and the '\n' argument tells when to break it up (in this case, every new line)
rngs = f.read().split('\n')

# let's now break each string up into its digits
# list(rng) turns each string 'rng' into an array of the individual digits, but still in text form
# map(int, ...) turns each of the digits into integers
# list(map...) turns the map back into an array (a list) which means we can easily access the elements
# digits stores each such list of integers as an element in its own array, making it a 2x2 matrix
digits = [list(map(int, list(rng))) for rng in rngs]

def solve(digits, J):
    
    # define our answer variable
    ans = 0
    
    for digs in digits:
        
        # define L as the length of the number string
        L = len(digs)
        
        # store the largest j digit number ending at or before positions i = 0 to L, for j = 0 to 12
        dp = [[0 for j in range(J + 1)] for i in range(L + 1)]
        
        # iterate over all positions in the number string
        for i in range(L):
            
            # iterate over all possible subsequence lengths
            for j in range(J + 1):
                
                # our maximum of length j up to this position is at least as good as it was up to the previous position
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                
                # we can create a new candidate of length j + 1 by using the candidate of length j up to the previous position, and the digit at position i+1 (i in 0-based) of the subsequence
                if j < J:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], 10 * dp[i][j] + digs[i])
        
        # the final answer for each string is the best possible subsequence of length J up to and including the final digit of the number string
        ans += dp[L][J]
    
    return ans

print(solve(digits, 12))