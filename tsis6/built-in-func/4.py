from time import sleep
import math

def delay(a, b):
  sleep(a / 1000)
  return math.sqrt(b)

a = int(input("enter ms: "))
b = int(input("enter number: "))
print(delay(a, b))