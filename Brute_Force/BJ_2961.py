# Topic : Brute_Force  _ 도영이가 만든 맛있는 음식
#
# Python 3 : 96ms
# 

from functools import reduce
import sys
from itertools import combinations

N = int(sys.stdin.readline())

# 신맛, 쓴맛 각각 저장
mat_s = []
mat_b = []
for _ in range(N):
  s , b = map(int,sys.stdin.readline().rstrip().split())
  mat_s.append(s)
  mat_b.append(b)

# 쓴맛과 신맛의 combination들의 차이를 각각 모두 저장
# 쓴맛, 신맛 두개의 리스트의 들어가는 요소들중 같은 인덱스를 가진 아이들은 재료로 매칭되는 아이들이다.
mat_s_diff = []
mat_b_diff = []
for i in range(1,N+1):
  tmp_s = combinations(mat_s,i)
  tmp_b = combinations(mat_b,i)

  # 신맛 곱하기
  for ts in tmp_s:
    # print("ts :",ts)
    mat_s_diff.append(reduce(lambda x, y: x * y, ts))

  # 쓴맛 더하기
  for tb in tmp_b:
    # print("tb :",tb)
    mat_b_diff.append(sum(tb))

# 쓴맛과 신맛 차이 저장
# mat_s_diff와 mat_b_diff의 차이를 구하는 do-while 문(인덱스가 같은 값을 빼준다.)
min = abs(mat_s_diff[0] - mat_b_diff[0])
for i in range(1,len(mat_s_diff)):
  diff = abs(mat_s_diff[i] - mat_b_diff[i])
  if diff < min:
    min = diff

print(min)

