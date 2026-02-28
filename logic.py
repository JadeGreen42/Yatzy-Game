from display import ndice
import random

def RNGenerator():
    rng = [0]*5
    for i in range(5):
        rng[i] = random.randint(1,6)
    return rng

def userIN():
    try:
        raw = input(("Which ones to keep? \n").strip())
        keep = [int(c) for c in raw]
        return keep
    except ValueError:
        return [] 

def validity(checker):
    return len(checker)>0 and all(0<=x<=5 for x in checker)

def hexcomp(pos, RNG, copybar):
    #print(pos, RNG, copybar)
    for x in range(len(copybar)):
        if x+1 not in pos:
            copybar[x] = RNG[x]
    return copybar

def SingleRound():
    copybar = [0]*5
    pos = [-1]*5
    for i in range(3):
        RNG = RNGenerator()
        copybar = hexcomp(pos, RNG, copybar)
        ndice(*copybar)
        if i < 2:
            while True:
                pos = userIN()
                if validity(pos):
                    break
                print("Invalid. Try again.")
    return copybar
