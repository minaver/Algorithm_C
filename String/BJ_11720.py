# Topic : String _ 숫자의 합
#
# Python 3 : 72ms
# 전체 수를 String으로 통으로 받아와 하나하나를 int로 변환하면서 sum에 더해준다.

import sys

num = sys.stdin.readline()
input = sys.stdin.readline().rstrip()

sum = 0
for n in input: 
  sum += int(n)

print(sum)



