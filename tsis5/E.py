import re
s = str(input()) #"abappleadvicebabewjdiwje"
pattern = re.search(r'[a].*[b$]',s)
print(pattern.group())