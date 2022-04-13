# Topic : String _ 나는 친구가 적다
#
# Python 3 : 72ms

import sys

def pickChar(word):
  new_word_list = list()
  for w in word:
    if not (int(ord(w)) >= 48 and int(ord(w)) <= 57): # 입력받은 문자가 숫자가 아닐때(ASCII CODE :: 0 = 48 / 9 = 57 )
      new_word_list.append(w)
  
  new_word = "".join(new_word_list) # list로 받은 값을 str으로 변화 시킴(이후 'in' 으로 비교하기 위해서)

  return new_word

word = sys.stdin.readline().rstrip()
key_word = sys.stdin.readline().rstrip()

new_word = pickChar(word)

if key_word in new_word:  # in으로 키워드가 교과서에 있는지 확인
  print(1)
else:
  print(0)