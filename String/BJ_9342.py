# Topic : String _ 염색체
#
# Python 3 : 128ms

import sys, re

# 의미 
# ^[A-F]{0,1} : 문자열 처음에 A-F의 문자가 0개 또는 1개 등장해야한다. 
# A+, F+, C+ : 각각 A, F, C가 하나 이상씩 반복하여 등장해야 한다.
# [A-F]{0,1}$ : 문자열 마지막에 A-F의 문자가 0개 또는 1개 등장해야한다. 
regex = re.compile('^[A-F]{0,1}A+F+C+[A-F]{0,1}$') 

N = int(sys.stdin.readline())
result = list()
for n in range(N):
  word = sys.stdin.readline().rstrip()
  if regex.match(word) == None:
    result.append('Good')
  else:
    result.append('Infected!')

for r in result:
  print(r)

