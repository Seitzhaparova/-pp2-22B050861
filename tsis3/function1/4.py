def filter_prime(arr):
    ans=[]
    for i in arr:
        prime=True
        if(int(i)==1):
            continue
        for j in range(2, int(i)-1):
            if(int(i)%j==0):
                prime=False
        if(prime==True):
            ans.append(int(i))
    return ans

list = input('input any list of numbers:').split()
print(filter_prime(list))
    
       

