l = input().split()
def filter(l):
    d = {}
    temp = []
    for i in l:
        if i not in d.keys():
            d[i] = 1
    for i in d.keys():
        temp.append(i)
    return temp
print(filter(l))
