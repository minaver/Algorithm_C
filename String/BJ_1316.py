# Topic : String _ 그룹 단어 체커
#
# PyPy 3 : 틀림
# 왜 틀린지 모르겠음

import sys

# 1. word로 들어온 문자열을 인덱스 순서대로 loop 돈다.
# 2. 연속 되어있는 문자가 끝나는 지점에서 그동안 before_word에 저장되었던 문자와 같은 문자가 있는지 확인하고 있다면 False return 한다.
# 3. 2에서 False return하지 않았으면 앞선 연속된 문자를 before_word에 저장한다(ex. aab 경우 index 2 에서 1과 비교후 a 저장)
# 4. 1에서 loop을 1~len(word)까지 돌고 word[i-1]을 저장하므로 word의 마지막 인덱스에 해당하는 문자에 대한 비교가 없다 
#   만약 i가 마지막 loop이고 3번까지의 과정을 모두 거쳤다면 마지막으로 word의 마지막 인덱스가 그룹 단어를 만족하는지 체크해준다.

def group_word_checker(word):
  before_word = list()
  for i in range(1,len(word)):  # 1
    if word[i-1] == word[i]:
      continue

    for bw in before_word:  # 2
      if bw == word[i-1]:
        return False

    before_word.append(word[i-1]) # 3

    if i == len(word) -1: # 4
      for bw in before_word:
        if bw == word[i]:
          return False
    
  return True


N = int(sys.stdin.readline())
count = 0

for n in range(N):
  word = sys.stdin.readline().rstrip()
  if group_word_checker(word) == True:
    count += 1
  
print(count)


