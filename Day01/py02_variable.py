# 변수
import sys

number = 210000000000
value = sys.maxsize # sys.maxsize 파이썬 시스템에서 제공하는 최고숫자 ( but, 더 더하기 가능 => for문 사용해서 어디까지 되는지 test!)

print(number)
print(value)
print(value + 1) # overflow 없다

value2 = 0o12 # 8진수
print(value2)

value2 = 0xFF # 16진수
print(value2)

value2 = 'Hello, Python'
print(value2)

value2 = False
print(value2 == False)

# 사칙연산, 수학식
print(14 / 2) # 소숫점 나누기
print(14 // 2) # 정수로 나누기
print(2 ** 10) # 승수 2의 10승
print(10 % 3) # 나머지, 3의 배수