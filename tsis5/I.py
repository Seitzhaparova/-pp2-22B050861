import re
l="YaUstalPizdec"
reg1=r"(^[A-Z])([a-zA-Z]*)"
reg=r"(.+?)([A-Z])"
def upper(match):
    return match.group(1).lower()+match.group(2).lower()
def change(match):
    return match.group(1).lower()+ "_" + match.group(2).lower()
#new_l=str([re.sub(reg1, upper, l, 0)])
#print(new_l)
result=[re.sub(reg, change, l, 0)]
print(result)