def check(n):
    ans=[]
    for i in range(1, n+1):
        check=True
        if(int(i)%3!=0 or int(i)%4!=0):
            check=False
        if(check==True):
            ans.append(int(i))
    return ans

n=int(input("Input any number: "))
print(check(n))