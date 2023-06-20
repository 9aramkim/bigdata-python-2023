# 문자열 

value = "Hello World"
print(value)
print('Hello World')

# "", '' 둘다 사용가능
print('저는 "아무개"입니다')
print("저는 '아무개' 입니다")

# 여러줄, 문장 쓰기 => ''' ~ '''  / """ ~ """
value = '''
안녕하세요
저는 프로그래머입니다
배우는 중입니다
'''

print(value)

'''
얘는 여러줄 주석으로 대체합니다.
파이썬에는 여러줄 주석이 없어서 
여러줄 문자열로 이 역할을 대신합니다.
'''

# 두개의 문자열 붙이기
print('Hello' + ' World!') # * 문자열은 안됨
# hello 3번 반복하라 
print('Hello' * 3)
# 예외 + 숫자는 안됨
# print('Hello' + 4)

print(len('Life is short')) # 13자리
print(len('인생은 짧아요.')) # 8자리

origin = 'Life is short, You need Python'
print(origin[1])
print(origin[0] + origin[16] + 
      origin[19] + origin[20] + 
      origin[0].lower() + origin[15].lower()) # lower() : 대문자를 소문자로 바꾸기
print(origin[0:4]) # Life, 0,1,2,3 이필요... +1 하기 == print(origin[:4])
print(origin[8:13])

print(origin[15:]) # index 15부터 끝까지 
print(origin[15:-7]) # 음수는 뒤에서부터 인덱스 -1부터 시작 

# 문자열 포맷팅
print('I ate %s apples' % ('three')) # % string formating
print('I ate %d apples' % (3))
print('pi is %f' % 3.14159265359)
print('pi is %10.2f' % 3.14159265359)

# 날짜 문자열 포맷팅
import datetime as dt

curr_dt = dt.datetime.now()
print(curr_dt)
fmt_dt = curr_dt.strftime('%Y년 %m월 %d일')
print('오늘 날짜는 %s 입니다.' % curr_dt.strftime('%Y년 %m월 %d일'))
# C#/Java yyyy년 MM월 dd일

# 최신 포맷팅
apple_num = 3 
print(f'I ate {apple_num:0.4f} apples')
apple_num = 'three'
print(f'I ate {apple_num} apples')

print(f'오늘 날짜는 {fmt_dt} 입니다.')

# 문자열 함수
# 'Life is short, You need Python'
print(origin.count('need')) # 문자, 문자열의 개수
print(origin.find('Python')) # 문자, 문자열찾기 => 찾는 시작 index를 알려준다, -1은 없음.

print('/'.join(origin)) # 문자(열) join에 있는 문자열이랑 하나씩 합치는 함수
print(origin.upper()) # 전부 대문자
print(origin.lower()) # 전부 소문자
print(origin.capitalize()) # 문자열의 첫번째 단어만 대문자로
print(origin.title()) # 단어의 첫번째 글자만 대문자로 

print('start'+'    Hello    '+'end') # 기본 
print('start'+'    Hello    '.lstrip()+'end') # 왼쪽 공백 지우기
print('start'+'    Hello    '.rstrip()+'end') # 오른쪽 공백 지우기
print('start'+'    Hello    '.strip()+'end') # 양쪽 공백 지우기
 
result = origin.replace(',', '').split(' ') # 공백으로 자르기 -> 배열(리스트)
print(result)