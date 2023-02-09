from itertools import permutations
str = input('input any string:')
perm= [''. join(p) for p in permutations(str)]
print(perm)



