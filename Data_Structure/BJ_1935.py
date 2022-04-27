# Topic : Data_Structure _ 후위 표기식 2
#
# Python 3 : 68ms
import sys 

N = int(sys.stdin.readline())
postfix = list(sys.stdin.readline().rstrip()) # 후위 표기식 list로 저장
stack = list()  # 후위 표기식 계산시 사용할 stack 저장
num = list()  # A~Z에 대응되는 숫자 저장

# num 초기화
for _ in range(N):
  num.append(int(sys.stdin.readline()))


for pf in postfix:
  # [1] 문자일 경우
  # A~Z에 대응되는 수를 찾아 stack에 차례로 push 해준다.
  if ord(pf) >= 65 and ord(pf) <= 90:
    # print("pf :",pf,"i :",i)
    stack.append(num[ord(pf)-65])
  # [2] 수식일 경우
  # 스택에 들어있는 상위 두 요소를 pop해 해당 수식에 대한 계산을 진행한다.
  # 계산 결과를 stack에 저장해준다.
  # 주의사항 : '/'와 '-' 연산시 순서에 유의하자 
  else:
    x1 = stack.pop()
    x2 = stack.pop()
    if pf == '*':
      new_one = x2 * x1
    elif pf == '/':
      new_one = x2 / x1
    elif pf == '+':
      new_one = x2 + x1
    elif pf == '-':
      new_one = x2 - x1
    stack.append(new_one)
    # print("pf :",pf,"new_one :",new_one)

# 마지막까지 남아있는 스택의 값이 최종 결과값이다.
print('%0.2f' %stack[0])

