# Topic : String _ 경고
#
# Python 3 : 읭 왜 틀리지..???

import sys

start_h, start_m , start_s = map(int,sys.stdin.readline().split(':'))
end_h, end_m, end_s = map(int,sys.stdin.readline().split(':'))

start_total_second = start_h * 60 * 60 + start_m * 60 + start_s
end_total_second = end_h * 60 * 60 + end_m * 60 + end_s

# 하루가 지나지 않은 경우 계산
if end_h > start_h: 
  result_total_second = end_total_second - start_total_second
# 하루가 지난 경우 계산
else:
  result_total_second = 24*3600 - start_total_second + end_total_second

result_h = result_total_second // 3600
# result_m = (result_total_second - result_h*3600) // 60
result_m = result_total_second // 60 % 60
result_s = result_total_second % 60
  
print("%02d:%02d:%02d" % (result_h, result_m, result_s))