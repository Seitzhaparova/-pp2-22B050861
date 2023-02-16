from math import tan, pi,floor
def area(n, l):
    area= n*(l ** 2) / (4*tan(pi/n))
    return area
side=int(input("Input number of sides: "))
length=int(input("Input the length of a side: "))
a=area(side, length)
ans=floor(a)
print("The area of the polygon is: "+str(ans))

#4 25 625