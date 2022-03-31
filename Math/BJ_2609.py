# Topic : MATH _ 최대공약수와 최소공배수
#
# 유클리드 호제법을 사용하여 해결
# PyPy 3 : 104ms

import sys

a , b = map(int,sys.stdin.readline().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a,b))
print(lcm(a,b))



