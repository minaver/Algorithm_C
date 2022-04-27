# Topic : Data_Structure _ 큐 2
#
# Python 3 : 2196 ms
# pop 수행시 del을 사용하게 되면 나머지 것들을 앞으로 한칸씩 끌어오는데 시간이 걸린다.

import sys
from collections import deque

def push(queue,X):
  queue.append(X)
  return queue

def pop(queue):
  if len(queue) == 0:
    return -1
  else:
    return queue.popleft()

def size(queue):
  return len(queue)

def empty(queue):
  if len(queue) == 0:
    return 1
  else:
    return 0

def front(queue):
  if len(queue) == 0:
    return -1
  else:
    return queue[0]

def back(queue):
  if len(queue) == 0:
    return -1
  else:
    return queue[-1]


N = int(sys.stdin.readline())
queue = deque()
result = list()

for _ in range(N):
  cmd = sys.stdin.readline().rstrip().split()
  
  if cmd[0] == "push":
    push(queue,cmd[1])
  elif cmd[0] == "pop":
    result.append(pop(queue))
  elif cmd[0] == "size":
    result.append(size(queue))
  elif cmd[0] == "empty":
    result.append(empty(queue))
  elif cmd[0] == "front":
    result.append(front(queue))
  elif cmd[0] == "back":
    result.append(back(queue))

for r in result:
  print(r)

