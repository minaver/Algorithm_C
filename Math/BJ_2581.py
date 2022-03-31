# Topic : MATH _ 소수
#
# Python 3 : 424ms / PyPy 3 : 184ms

import sys

def sosu(n):
  if n == 1:
    return False

  for i in range(2,n):
    if n%i == 0:
      return False

  return True


M = int(sys.stdin.readline());
N = int(sys.stdin.readline());

list = list()
sum = 0;

for i in range(M,N+1):
  if sosu(i) == True:
    sum = sum + i
    list.append(i)

if len(list) == 0:
  print(-1)
else:
  print(sum)
  print(min(list))
