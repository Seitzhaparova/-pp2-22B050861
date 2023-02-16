def filter_even(n):
    ans=[]
    for i in range(1, n+1):
        even=True
        if(int(i)%2!=0):
            even=False
        if(even==True):
            ans.append(int(i))
    return ans

n = int(input('input any number:'))
print(filter_even(n))
    
       

