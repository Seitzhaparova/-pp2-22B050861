import re
s = "YA Ustal Hochu est'"
print(re.findall(r"[A-Z][a-z]+",s))