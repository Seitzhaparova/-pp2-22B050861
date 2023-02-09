
def solve(numheads, numlegs):
    numRabbit = numlegs / 2 - numheads
    numChicken = numheads - numRabbit
    print(int(numChicken))
    print(int(numRabbit))
solve(35, 94)

"""
fignya eto
def solve(numheads, numlegs):
    r=c=1
    if(((4*r+2*c)==numlegs)&(r+c)==numheads):
        print(r, end=" ")
        print(c)
    else r +=1 , c +=1

solve(35, 94)
"""