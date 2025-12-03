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

ans = 0

for digs in digits:
    
    # define a temporary max value for this string
    tmp_max = 0
    
    # define the length of the input number as L
    L = len(digs)
    
    # loop over all possible values of the first digit
    for i in range(L):
        # loop over all possible values of the second digit
        
        for j in range(i + 1, L):
            
            # update the maximum possible value
            tmp_max = max(tmp_max, 10 * digs[i] + digs[j])
    
    # add the maximum possible for this number string to our total answer
    ans += tmp_max

print(ans)