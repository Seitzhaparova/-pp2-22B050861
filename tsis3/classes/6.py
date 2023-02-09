class Number():
    def __init__(self, arr):
        self.arr=arr
    def filtering(self):
        return list(filter(lambda x: Prime(x), self.arr))  
        
def Prime(x):
    for i in range(2, x-1):
        if(x%i==0):
            return False
    return True
    
c= Number([1,2,3,4,5,6,7])
print(c.filtering())