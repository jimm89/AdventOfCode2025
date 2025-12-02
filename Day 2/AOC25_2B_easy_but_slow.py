import sys
read = sys.stdin.read
f = open("AOC25_2_in.txt")

#read in the file, and save the information in an array which we call 'rngs'
#the 'split' function breaks the input file up, and the ',' argument tells when to break it up (in this case, every new line)
rngs = f.read().split(',')

def is_invalid_len(num, rep):
    
    num_length = len(str(num))
    
    # if the pattern length doesn't divide the number length, this pattern length does not fit
    if num_length % rep > 0:
        return False
    
    # let's define num_reps as the number of times we need the pattern to recur
    num_reps = num_length // rep
    
    # then every 'rep' digits must be the same
    return str(num) == num_reps * str(num % (10 ** rep))

def is_invalid(num):
    
    # Let's try to determine whether the number has a repeating pattern of length L, for any length L up to but not including the length of our number
    # We can start from L/2 and work backwards to 1
    
    for i in range(len(str(num)) // 2, 0, -1):
        if is_invalid_len(num, i):
            return True
    
    return False

ans = 0  

for rng in rngs:
    lo, hi = rng.split('-')
    lo = int(lo)
    hi = int(hi)
    
    # the input looks pretty simple, but we should always prepare for the most difficult scenario
    # we must count all invalid numbers x, such that lo <= x <= hi
    
    for num in range(lo, hi + 1):
        if is_invalid(num):
            ans += num

print(ans)