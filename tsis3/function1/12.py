def histogram(arr):
    for i in range(0, len(arr)):
        temp=int(arr[i])
        output=''
        while(temp >0):
            output+="*"
            temp = temp -1
        print(output)

a=input('input any array')
list=a.split()
histogram(list)