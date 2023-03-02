import re
s = ['a', 'babb', 'abb', 'abbb', 'abbbb', 'abbbbb', "ab"]
reg = r"[b]{2,3}\b"
ans=[]
for i in s:
    if re.search(reg,i):
        ans.append(i)
    else:
        pass
print(ans)