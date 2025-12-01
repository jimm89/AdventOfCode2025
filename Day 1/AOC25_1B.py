#import the sys library, which will help us read the file
import sys

#define the 'read' function from the sys library in a shorthand way, for ease of use
read = sys.stdin.read

#open the file which contains our input
f = open("AOC25_1_in.txt")

#read in the file, and save the information in an array which we call 'moves'
#the 'split' function breaks the input file up, and the '\n' argument tells when to break it up (in this case, every new line)
moves = f.read().split('\n')

#define a variable to store the position of the dial, which begins at 50
pos = 50

#define a variable to store the size of the dial (note this is not necessary in this problem, but could be useful if the dial size might change)
dial_size = 100

#create an answer variable, which starts at 0 and is incremented every time our dial hits 0
ans = 0

#read the instructions one by one
for move in moves:
    
    #determine the direction
    direction = move[0]
    
    #determine the distance moved (note we must convert the text from the instruction to an integer)
    change = int(move[1:])
    
    #determine how many complete turns the dial does (each of which will cause us to pass zero exactly once
    ans += change // dial_size
    
    #remove the complete turns from consideration
    change %= dial_size
    
    #make the change negative if direction is left
    if direction == 'L':
        change *= -1  
    
    #determine whether the final partial change will cause us to pass 0, and increment our answer variable if so
    if pos + change >= dial_size or (pos > 0 and pos + change <= 0):
        ans += 1
    
    #change the position by the required amount, and then use modular arithmetic to ensure the answer remains between 0 and 99
    pos = (pos + change) % dial_size

#print the answer
print(ans)