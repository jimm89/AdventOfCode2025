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

def sum_rep(lo, hi, length, rep):
    
    # discount any repetition lengths which are not a factor of length
    if length % rep != 0:
        return 0
    
    rep = length // rep
    
    # For ease, let's call the smallest repeating pattern lo_rep and the longest half number hi_rep
    # This is because each pattern in this range accounts for exactly one possible invalid number, so if rep = 3, 1234 could be 123412341234, an invalid number
    lo_rep = 10 ** (length // rep - 1)
    hi_rep = 10 * lo_rep - 1
    
    # what's the smallest invalid number that's >= lo and has this length and this degree of repetition?
    if length > len(str(lo)):
        min_ = lo_rep
    else:
        min_ = lo
        min_ //= (lo_rep * 10) ** (rep - 1)
        # try this number, and increment by 1 if too low
        tmp = min_
        for i in range(rep - 1):
            tmp = tmp * (10 * lo_rep) + min_
        if tmp < lo:
            min_ += 1
    
    # what's the largest invalid number that's <= hi and has this length and this degree of repetition?
    if length < len(str(hi)):
        max_ = hi_rep
    else:
        max_ = hi
        max_ //= (lo_rep * 10) ** (rep - 1)
        tmp = max_
        for i in range(rep - 1):
            tmp = tmp * (10 * lo_rep) + max_
        if tmp > hi:
            max_ -= 1
    # So now I know the range of invalid partial numbers, I must sum that range and then multiply by (lo_rep * 10 + 1)**(rep - 1)
    ret = sum_range(min_, max_)
    adder = ret
    for i in range(rep - 1):
        ret = ret * (10 * lo_rep) + adder
    return ret

def sum_(lo, hi, length):
    
    # define an array to store the number of invalid numbers which have a repeating pattern of anywhere between 1 and length // 2 inclusive
    rep_counts = [0] * (length // 2 + 1)
    
    # iterate over all possible repetition lengths
    for l in range(1, length // 2 + 1):
        rep_counts[l] = sum_rep(lo, hi, length, l)
    
    # define a variable to return the number of invalid numbers of this length between lo and hi inclusive
    ret = 0
    for l in range(1, length // 2 + 1):
        if length % l > 0:
            continue
        # add the number of that length
        ret += rep_counts[l]
        
        # delete double counts - any with a shorter repeating pattern that is a factor of l
        for x in range(1, l):
            if l % x == 0:
                ret -= rep_counts[x]

    return ret

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