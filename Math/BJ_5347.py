# Topic : MATH _ LCM
#
# PyPy 3 : 108ms

import sys

# 최대 공약수 구하기
def gcd(a,b):
  while b != 0:
    a , b = b , a%b
  return a

# 최소 공배수 구하기
def lcm(a,b):
  return a*b//gcd(a,b)

n = int(sys.stdin.readline())

for i in range(n):
  a , b = map(int,sys.stdin.readline().split())
  if a >= b:
    print(lcm(a,b))
  else:
    print(lcm(b,a))
