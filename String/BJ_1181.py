# Topic : String _ 단어 정렬
#
# PyPy 3 : 1392ms
# Python 3 : 시간 초과

import sys

N = int(sys.stdin.readline())
result = list()

for n in range(N):
  word = sys.stdin.readline().rstrip()
  
  if n == 0:
    result.append(word)
  else: 
    for i in range(len(result)):
      if len(result[i]) > len(word):  # 새로 들어온 word의 길이가 i번째 result의 단어의 길이보다 짧을때
        result.insert(i,word)
        break
      elif len(result[i]) == len(word): # 새로 들어온 word의 길이가 i번째 result의 단어와 길이가 같을 때
        if result[i] == word: # 단어가 아예 같을때
          break
        elif result[i] > word:  # 새로 들어온 word가 사전상 i번째 result의 단어보다 앞서있을때
          result.insert(i,word)
          break
      
      if i == len(result) -1: # 마지막 result까지 위 조건들을 모두 만족하지 않았다면 result에 있는 모든 값보다 뒷 순서라는 의미이다.
        result.append(word)

for r in result:
  print(r)
