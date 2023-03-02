import re
s = "I want to eat some rice with meat, maybe, chicken."
pattern =re.sub("[ ,.]", ":", s)
print(pattern)