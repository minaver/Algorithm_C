# Topic : MATH _ 피로도
# Python 3 : 80ms

import sys

A, B, C, M = map(int,sys.stdin.readline().split())

work = 0
hard = 0

for i in range(24):
  if hard + A > M: # 피로도가 쌓일 때 
    hard = hard - C
    if hard < 0:
      hard = 0
  else:
    hard = hard + A
    work = work + B

print(work)