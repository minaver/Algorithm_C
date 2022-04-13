# Topic : String _ 비밀번호 발음하기
#
# Python 3 : 68ms

import sys

vowel = ['a','e','i','o','u']

def check_accpetable(word):
  vowel_exist = False # 모음 개수

  # 1. 모음 포함 여부 check
  for w in word:
    if w in vowel:
      vowel_exist = True

  if vowel_exist == False:
    return False

  for i in range(len(word)-1):
    # 2. 같은 글자가 연속적으로 두번 등장하는지 check(ee, oo 제외)
    if word[i] == word[i+1] and word[i] != 'e' and word[i] != 'o':
      return False
  
  for i in range(len(word)-2):
    # 3. 모음 3개나 자음 3개가 연달아 count 되는지 확인
    if word[i] in vowel and word[i+1] in vowel and word[i+2] in vowel:  # 모음 3개가 연달아 나오는 경우
      return False
    elif not word[i] in vowel and not word[i+1] in vowel and not word[i+2] in vowel:  # 자음 3개가 연달아 나오는 경우
      return False
  
  return True


while True:
  word = sys.stdin.readline().rstrip()
  if word == "end":
    break

  if check_accpetable(word) == True:
    print("<",word,">"," is acceptable.",sep="")
  else:
    print("<",word,">"," is not acceptable.",sep="")

