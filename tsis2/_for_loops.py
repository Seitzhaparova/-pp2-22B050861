#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2
for x in "banana":
  print(x)
#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#6
for x in range(6):
  print(x)
#7
for x in range(2, 6):
  print(x)
#8
for x in range(2, 30, 3):
  print(x)
#9
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#12
for x in [0, 1, 2]:
  pass
