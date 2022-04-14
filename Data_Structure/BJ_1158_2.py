# Topic : Data_Structure _ 요세푸스 문제 _ By using 양방향 Queue(deque)
#
# PyPy 3 : 480 ms

import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

yoseps = deque([i+1 for i in range(N)])
result = list() # 결과를 저장할 list

# 중식당 테이블처럼 원하는 요소를 내 앞으로 가져다 놓는 형식이다. 
for i in range(N - 1):
	for _ in range(K - 1):
		yoseps.append(yoseps.popleft()) # 좌측에 있는 요소를 우측에 붙인다.(K번째 움직인 요소를 맨 좌측에 놓기 위해서)
	result.append(yoseps.popleft()) # 현재 가장 왼쪽에 있는 요소를 result에 저장
result.append(yoseps.popleft()) # 마지막 요소를 result에 저장
# < ~ > 형식으로 만들어준다.
result = str(result)
result = result.replace('[','<')  
result = result.replace(']','>')
print(result)