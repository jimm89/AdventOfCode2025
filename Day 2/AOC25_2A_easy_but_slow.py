import sys
read = sys.stdin.read
f = open("AOC25_2_in.txt")

#read in the file, and save the information in an array which we call 'rngs'
#the 'split' function breaks the input file up, and the ',' argument tells when to break it up (in this case, every new line)
rngs = f.read().split(',')

def is_invalid(num):
    
    # get length of number
    num_length = len(str(num))
    
    # if the number has odd length, we immediately know it is not invalid
    if num_length % 2 == 1:
        return False
    
    # if a number is invalid, then the 'first half of the number' equals 'the second half of the number', so I'll check that the characters in the first half match those in the second half, and return 'True' if so
    return str(num)[ : num_length // 2] == str(num)[num_length // 2 : ]
    
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