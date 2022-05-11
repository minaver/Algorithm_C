# Topic : Brute_Force  _ 한수
#
# Python 3 : 72ms
# 

import sys
import math

N = int(sys.stdin.readline())

count = 0
for n in range(1,N+1):
  num_len = int(math.log10(n)) + 1

  if num_len == 3:
    tmp = list(map(int,str(n)))
    if tmp[0] + tmp[2] == tmp[1]*2:
      count +=1
  elif num_len == 4:
    continue
  else:
    count += 1

print(count)
