# Topic : Data_Structur_2  _ N번째 큰 수
#
# PyPy 3 : 메모리 초과

import sys

N = int(sys.stdin.readline())

box = list()

for _ in range(N):
  box.extend(list(map(int,sys.stdin.readline().rstrip().split())))

box.sort()
print(box[-5])




