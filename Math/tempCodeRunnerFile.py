# Topic : MAth _ 공약수
# Result : python 용
import sys

def gcd(p,q):
  if p == 0:
    return q;
  return gcd(q%p, p)

n = int(sys.stdin.readline().rstrip())
list = list()

if n == 2:
  p,q = map(int,sys.stdin.readline().split().rstrip())
  gcd = gcd(p,q)
  [print(i) for i in range(1,gcd+1) if gcd%i == 0]
    
else:
  p,q,r = map(int,input().split().rstrip())
  gcd(p,gcd(q,r))
  [print(i) for i in range(1,gcd+1) if gcd%i == 0]


