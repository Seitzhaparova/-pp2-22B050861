from math import pi
def volume(r):
    vol= 4/3 * pi * pow(r,3)
    return vol
    
rad= int(input())
print(volume(rad))
