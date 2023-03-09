import os
print('Exist:', os.access("lines2.txt", os.F_OK))
os.remove("lines2.txt")