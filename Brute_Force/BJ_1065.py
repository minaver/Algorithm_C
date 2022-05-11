# Topic : Brute_Force  _ 한수
#
# Python 3 : 72ms
# 등차수열시 a(N+2)*2 == a(N) + a(N+1) 

import sys
import math

N = int(sys.stdin.readline())

count = 0
for n in range(1,N+1):
  num_len = int(math.log10(n)) + 1  # 먼저 n의 자리수를 구한다. 백자리 천자리 그리고 그외로 로직을 구분

  if num_len == 3:  # 백의 자리
    tmp = list(map(int,str(n))) # n을 자리수 각각을 쪼개 list화 한다.
    if tmp[0] + tmp[2] == tmp[1]*2: # 해당 list의 요소가 등차수열인지 체크
      count +=1
  elif num_len == 4:  # 천의 자리 : 해당 테스트 케이스에서 1000만 해당되므로 cotinue
    continue
  else: # 그외 자리(일의 자리, 십의 자리) : 이 경우 모든 경우가 한수이다.
    count += 1

print(count)
