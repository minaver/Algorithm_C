# Topic : MATH _ 공약수
# Result : Python 3용
import sys

def gcd(p,q):
  if p == 0:
    return q;
  return gcd(q%p, p)

n = int(sys.stdin.readline().rstrip())

if n == 2:
  p,q = map(int,sys.stdin.readline().split())
  list = gcd(p,q)
  [print(i) for i in range(1,list+1) if list%i == 0]
    
else:
  p,q,r = map(int,sys.stdin.readline().split())
  list = gcd(p,gcd(q,r))
  [print(i) for i in range(1,list+1) if list%i == 0]


