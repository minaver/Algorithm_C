# Topic : String _ 회문
#
# PyPy 3 : 248ms
# 1. 일단 유사 회문을 체크
# 2-1. 유사 회문일 경우 그냥 return 0
# 2-2. 유사회문이 아닐 경우 그 문자의 앞뒤의 문자와 비교하여 해당 문자와 비교후 해당 문자와 같다면 그 문자를 빼고 기회를 한번 더줌
# 3-1. 한번 더 주어진 기회에서 유사회문이 아닐 경우 return 2 
# 3-1. 한번 더 주어진 기회에서 유사회문일 경우 return 1 

import sys

def checkCycle(word,life):
  count = len(word)//2
  word = list(word)
  # 오름차순 비교에 사용할 리스트 (회문규칙에 맞지 않는 요소를 지운 리스트를 파라미터로 넣어줘야하는데 이후 내림차순 비교에서 전체 리스트가 필요하니 새로운 list를 만들어준다.)
  # 여기서 input_word = word 하면 주소만 복사되어 word에서 요소 지우면 input_word에서도 없어진다.
  input_word = list(word) 

  # 유사 회문 check
  for i in range(count):
    if word[i] != word[(len(word)-1)-i]:
      # 이미 life를 하나 쓴 경우
      if life == 0:
        return 2
      # 만약 해당 비교 앞에서 같은 단어가 등장시 기회를 한번 더준다.
      # 오름차순 비교에서 확인
      if word[i+1] == word[(len(word)-1)-i]:
        del input_word[i] # i번째 인덱스 요소를 지워버린다
        result = checkCycle(input_word,life-1) # 회문규칙에 맞지 않는 요소를 지운 리스트로는 만족하는지 확인
        if result == 1: # 만약 유사 회문일 경우 바로 return 1하고 유사회문이 아닐 경우 내림차순에서는 만족하는지 수행해준다.
          return 1
      # 내림차순 비교에서 확인
      if word[i] == word[(len(word)-1)-i-1]:
        del word[len(word)-1-i] # len(word)-1-i번째 인덱스 요소를 지워버린다
        return checkCycle(word,life-1) # 회문규칙에 맞지 않는 요소를 지운 리스트로는 만족하는지 확인

      # 오름차순 내림차순 비교시 둘다 일치하지 않는 경우
      return 2

  
  # 그냥 회문일 경우
  if life == 1 and i == count-1:  
    return 0
  # 유사 회문일 경우
  elif life == 0 and i == count-1:
    return 1


N = int(sys.stdin.readline())
result = list()
for n in range(N):
  word = sys.stdin.readline().rstrip()
  result.append(checkCycle(word,1))

for r in result:
  print(r)
