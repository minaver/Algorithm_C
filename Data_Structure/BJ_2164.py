# Topic : Data_Structure _ 카드 2
#
# PyPy 3 : 164 ms

import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque([ n+1 for n in range(N)])  # deque를 사용하여 1~N 초기화

# print(card.popleft())
# print(card.pop())

while len(card) != 1:
  # 1. 맨 위 카드 한장을 버린다.
  card.popleft()
  # 2. 다음 맨 위 카드를 맨 밑으로 옮긴다.
  card.append(card.popleft())

print(card[0])


