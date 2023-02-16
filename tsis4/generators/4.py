from math import pow
def squares(a,b):
    ans=[]
    for i in range (a, b+1):
        sq=pow(i,2)
        ans.append(int(sq))
    return ans

a=int(input("Input first number: "))
b=int(input("Input second number: "))
print(squares(a,b))