# Topic : String _ 듣보잡 _ 2
#
# Pythond : 124 ms

import sys

N , M = map(int,sys.stdin.readline().split())

#  듣잡 저장 
never_heard = set()
for n in range(N):
  never_heard.add(sys.stdin.readline().rstrip())

#  보잡 저장
never_seen = set()
for m in range(M):
  never_seen.add(sys.stdin.readline().rstrip())

# 합집합 연산 and 사전순 정렬
result = sorted(never_heard & never_seen)

print(len(result))
for r in result:
  print(r)


