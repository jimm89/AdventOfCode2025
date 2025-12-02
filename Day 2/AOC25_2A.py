import sys
read = sys.stdin.read
f = open("AOC25_2_in.txt")

#read in the file, and save the information in an array which we call 'rngs'
#the 'split' function breaks the input file up, and the ',' argument tells when to break it up (in this case, every comma)
rngs = f.read().split(',')

def sum_first_n(n):
    return n * (n + 1) // 2

def sum_range(min_, max_):
    return sum_first_n(max_) - sum_first_n(min_ - 1)

def sum_(lo, hi, length):
    
    # discount any odd length numbers, as we know all invalid numbers have even length
    if length % 2 == 1:
        return 0
    
    # For ease, let's call the smallest half-number lo_half and the largest half number hi_half
    # This is because each half-number in this range accounts for exactly one possible invalid number, so 1234 could be 12341234, an invalid number
    lo_half = 10 ** (length // 2 - 1)
    hi_half = 10 * lo_half - 1
    
    # what's the smallest invalid number that's >= lo and has this length?
    # if the length is bigger than the length of the bottom number of our range, then our smallest number is simply a power of 10 (e.g. 10, 100, 1000, etc)
    if length > len(str(lo)):
        min_ = lo_half
    # otherwise, our smallest number is the smallest repeating pattern number >= lo
    else:
        min_ = lo // (lo_half * 10)
        if (min_ * (10 * lo_half + 1)) < lo:
            min_ += 1
    
    # what's the largest invalid number that's <= hi and has this length?
    # if the length is smaller than the length of the top number of our range, then our largest number is simply a sequence of repeating 9s (e.g. 99, 999, 9999, etc)
    if length < len(str(hi)):
        max_ = hi_half
    # otherwise, our largest number is the largest repeating pattern number <= hi
    else:
        max_ = hi // (lo_half * 10)
        if (max_ * (10 * lo_half + 1)) > hi:
            max_ -= 1
    
    # So now I know the range of invalid half numbers, I must sum the numbers in that range and then multiply by (10 * lo_half + 1) 
    return sum_range(min_, max_) * (10 * lo_half + 1)

ans = 0

for rng in rngs:
    lo, hi = rng.split('-')
    lo = int(lo)
    hi = int(hi)
    
    # the input looks pretty simple, but we should always prepare for the most difficult scenario
    # we must count all invalid numbers x, such that lo <= x <= hi
    # we will start by considering numbers with the same length as lo, and iterate until we reach numbers of the same length as hi
    
    for length in range(len(str(lo)), len(str(hi)) + 1):
        ans += sum_(lo, hi, length)

print(ans)