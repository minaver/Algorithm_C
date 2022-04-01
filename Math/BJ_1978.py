# Topic : MATH _ 소수 찾기
#
# Python 3 : 68ms

import sys

def sosu(n):
  if n == 1:
    return False
  
  for i in range(2,n):
    if n%i == 0:
      return False
  
  return True

N = int(sys.stdin.readline())

list = list(map(int,sys.stdin.readline().split()))
count = 0

for num in list:
  if sosu(num) == True:
    count = count + 1

print(count)