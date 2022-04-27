# Topic : Data_Structure _ 덱
#
# PyPy 3 : 180ms
# 그냥 deque 사용

import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()
result = list()

for _ in range(N):
  cmd = sys.stdin.readline().split()
  if cmd[0] == "push_front":
    dq.appendleft(cmd[1])
  elif cmd[0] == "push_back":
    dq.append(cmd[1])
  elif cmd[0] == "pop_front":
    if len(dq) == 0 :
      result.append(-1)
    else:
      result.append(dq.popleft())
  elif cmd[0] == "pop_back":
    if len(dq) == 0 :
      result.append(-1)
    else:
      result.append(dq.pop())
  elif cmd[0] == "size":
    result.append(len(dq))
  elif cmd[0] == "empty":
    if len(dq) == 0 :
      result.append(1)
    else:
      result.append(0)
  elif cmd[0] == "front":
    if len(dq) == 0 :
      result.append(-1)
    else:
      result.append(dq[0])
  elif cmd[0] == "back":
    if len(dq) == 0 :
      result.append(-1)
    else:
      result.append(dq[-1])

for r in result:
  print(r)