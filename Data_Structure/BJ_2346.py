# Topic : Data_Structure _ 풍선 터뜨리기
#
# Python 3 : 88ms 

import sys
from collections import deque

N = int(sys.stdin.readline())

ballon = deque(enumerate(map(int,sys.stdin.readline().split())))
result = []

while ballon:
  idx , num = ballon.popleft()
  result.append(idx + 1)
  if num > 0:
    ballon.rotate(-(num-1)) 
  elif num < 0:
    ballon.rotate(-num)


print(' '.join(map(str,result)))
