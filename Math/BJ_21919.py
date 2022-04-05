# Topic : MATH _ 소수 최소 공배수
#
# Python 3 : 84ms

import sys
import math

def sosu(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  
  return True

N = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split()))

sum = 1
for a in A:
  if sosu(a) == True:
    sum *= a

if sum == 1:
  print(-1)
else:
  print(sum)