# Topic : MATH _ 최소공배수
#
# 유클리드 호제법을 사용하여 해결
# Python 3 : 68ms

import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


N = int(sys.stdin.readline())
for i in range(N):
  a , b = map(int,sys.stdin.readline().split())
  print(lcm(a,b))



