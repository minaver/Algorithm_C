# Topic : Brute_Force  _ 블랙잭
#
# PyPy 3 : 144ms

from itertools import combinations
import sys

N , M = map(int,sys.stdin.readline().split())

card = map(int,sys.stdin.readline().split())
comb_card = combinations(card,3)  # combination 사용하여 card 3개의 조합 find
sum_comb_card = map(sum,comb_card)  # combination된 카드들의 조합을 모두 더함

max = 0
for scc in sum_comb_card:
  if scc > max and scc <= M:  # M보다 작은 max를 find
    max = scc
    
print(max)



