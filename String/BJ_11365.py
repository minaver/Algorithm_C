# Topic : String _ !밀비 급일
#
# Python 3 : 68ms
# 1. 읽는 line이 "END"가 나올때까지 무한 loop으로 line을 받아와 L list에 넣어줌
# 2. L list에 있는 한줄 한줄의 String을 맨뒤 index부터 출력 

import sys

L = list()
while True:
  line = sys.stdin.readline().rstrip()
  if line == "END":
    break
  L.append(line)

for l in L:
  for i in range(len(l)-1,-1,-1):
    print(l[i],end="")
  print("")
