def desc(n):
    ans=[]
    for i in range(n, 0, -1):
        ans.append(int(i))
    return ans

n=int(input("Input any number: "))
print(desc(n))