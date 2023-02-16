import math
def area(h,b1,b2):
    area=((b1+b2)/2)*h
    return(area)
h=int(input("input heigh: "))
base1=int(input("input first base length"))
base2=int(input("input second base length"))
a=area(h, base1, base2)
print('area of trapezoid: '+str(a))