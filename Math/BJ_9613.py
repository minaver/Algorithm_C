# Topic : MATH _ GCD 합
#
# PyPy 3 : 120ms

import sys

def gcd(a,b):
  if a < b:
    a , b = b, a

  while b != 0:
    a , b = b , a%b
  return a

t = int(sys.stdin.readline())

for i in range(t):
  test_case = list(map(int,sys.stdin.readline().split()))
  gcd_list = list()

  for p in range(1,test_case[0]+1):
    for q in range(p+1,test_case[0]+1):
      result = gcd(test_case[p],test_case[q])
      gcd_list.append(result)
  
  print(sum(gcd_list))


