import re
l="YaUstalPizdec"
reg=r"([^A-Z].*?)([A-Z])"
def change(match):
    return match.group(1)+" "+match.group(2)
result= [re.sub(reg, change, l,0)]
print(result)