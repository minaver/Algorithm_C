# Topic : MATH _ 서로소 평균
#
# PyPy 3 : 632ms

import sys

def gcd(a,b):
  if a < b:
    a , b = b, a

  while b != 0:
    a , b = b , a%b
  return a

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
X = int(sys.stdin.readline())

result = list()
for a in A:
  if gcd(a,X) == 1:
    result.append(a)

print(sum(result)/len(result))




