import string, os
for i in string.ascii_uppercase:
   with open(i + ".txt", "w") as f:
       f.writelines(i)