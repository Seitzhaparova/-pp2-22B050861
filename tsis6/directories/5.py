a = [1, 2, 4, 8, 16]
f = open('write.txt', "w")
for i in a:
    f.write("%s\n" % i)
f.close()

with open('write.txt', 'r') as f:
    print(f.read())
