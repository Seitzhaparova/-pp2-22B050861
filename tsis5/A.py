import re
a = "a ab abb abbbb abbbbbbb abbb"
print(re.findall("a[b]*",a))