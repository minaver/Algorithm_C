# Topic : Data_Structur_2  _ N번째 큰 수
#
# PyPy 3 : 792ms

import sys

N = int(sys.stdin.readline())

live = [] # 각각의 줄을 순회하며 가장 큰 N개의 숫자를 저장할 list

for n in range(N):
  if n == 0:  # 처음에는 그냥 저장한다.
    live = list(map(int,sys.stdin.readline().rstrip().split()))
  else: # 이후에는 이전 live와 비교하고 sort하여 가장 큰 N개의 list를 live에 저장한다.
    tmp = list(map(int,sys.stdin.readline().rstrip().split())) + live
    tmp.sort()
    live = tmp[N:]

print(live[0])
