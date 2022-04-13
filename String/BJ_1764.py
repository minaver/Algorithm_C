# Topic : String _ 듣보잡
#
# PyPy 3 : 시간 초과

import sys

N , M = map(int,sys.stdin.readline().split())

#  듣잡 저장 
never_heard = list()
for n in range(N):
  never_heard.append(sys.stdin.readline().split())

#  보잡 저장
never_seen = list()
for m in range(M):
  never_seen.append(sys.stdin.readline().split())

#  듣잡 + 보잡 저장 
result = list()
for h in never_heard:
  for s in never_seen:
    if h == s:
      result.append(h)

# 사전순 정렬
print(sorted(result))

