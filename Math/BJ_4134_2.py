# Topic : MATH _ 다음 소수
#
# PyPy 3 : 448ms

import sys
import math

def sosu(n):
  if n <= 1:
    return False 

  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  
  return True


n = int(sys.stdin.readline())

for i in range(n):
  num = int(sys.stdin.readline())
  count = 0
  while True:
    if sosu(num+count) == True:
      print(num+count)
      break
    count = count + 1

