# Topic : Data_Structure _ 프린터 큐
#
# Python 3 : 100ms
# 초기 아이디어 : docs와 m 인덱스를 같이 움직이면서 인덱스가 m인 요소의 변한 인덱스가 0이고 이때 docs에서 max인 경우를 찾는다.

from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
  n , m = map(int,sys.stdin.readline().split()) # N, M 입력 받음
  docs = deque(sys.stdin.readline().split())  # 문서들 deque로 초기화
  count = 1 # 몇번째로 출력되는지를 확인할 var

  while len(docs) > 0:  # docs이 모두 pop되어 길이가 0이 될때까지 loop 
    if max(docs) == docs[0]:  # 만약 맨앞값이 가장 큰값이면 출력한다
      if m == 0: # 출력시 확인하기 원했던 요소라면 count print
        print(count)
        break
      else: # 아니면 count만 올리고 없애준다.
        docs.popleft()
        m -= 1
        count += 1
    else: # 가장 큰값이 아니면 맨앞값을 맨 뒤로 옮긴다. 
      if m == 0:
        m = len(docs)-1
      else:
        m -= 1
      docs.append(docs.popleft())



