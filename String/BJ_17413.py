# Topic : String _ 단어 뒤집기 2
#
# Python 3 : 312 ms

import sys

line = sys.stdin.readline().rstrip()

# <가 나온 경우 >가 나오기 전까지 Flag는 True 
# Flag -> True : 그냥 저장 / False : 반대로 저장
flag = False  
word = ""
result = ""

for l in line:
  if flag == False: # default는 반대로 저장
    if l == '<': # 만약 < 가 등장시 flag True로
      flag = True
      word += l # 그냥 저장
    elif l == ' ':  # ' ' 공백 등장시 단어가 끝난것이므로 result에 해당 단어 더해준다.
      word += l # 공백은 뒤집지 않으므로 그냥 저장
      result += word
      word = ""
    else:
      word = l + word  # 반대로 저장

  else: # default는 그냥 저장
    word += l # 그냥 저장
    if l == '>':  # 만약 > 등장시 <>가 마무리 된것이므로 flag False로 내리고 result에 word 추가
      flag = False
      result += word
      word = "" 

print(result+word)
