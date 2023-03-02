import re
l="snake_case_soset"
l=l[0].upper()+l[1:]
#print(l)
reg=r"(.*?)_([a-zA-Z])"
def change(match):
    return match.group(1)+match.group(2).upper()
results=[re.sub(reg, change, l, 0)]
print(results)