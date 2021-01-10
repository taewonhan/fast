# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('Hello python!')
print("Hello python!")
print("""Hello python!""")
print('''Hello python!''')

print()

# Separator

print('T', 'E', 'S', 'T', sep ='')
print('2019', '02', '19', sep='-') # 문자열간 사이에 -를 넣는것임
print('cnrncjwo', 'naver.com', sep='@')

#end 옵션 사용
print('Welcome To', end='') # 끝을 공백으로해서 print간 줄바꿈이 발생 x
print('the black paradise', end=' ') # 끝을 띄어쓰기로해서 print간 띄어쓰기만 발생 
print('hi guys')

print()
# format 사용 [], {}, ()
print('{} and {}'.format('You', 'I')) 
print("{0} and {1} and {0}".format('You', 'I')) # you가 0 / i가 1
print("{a} are {b}".format(a='You', b='I')) # a가 you / b가 I

# %s : 문자 / %d : 정수 , %f : 실수
print("%s's favorite number is %d" % ('Taewon', 10)) 

print("Test1: %5d, Price: %4.2f" % (7123,6534.123)) # %5d -> 5자리를 확보한 후 오른쪽정렬 정수 / %4.2f -> 4자리확보한후정수 + 최대2자리소수점
print("Test1: {0:5d}, Price: {1:4.2f}".format(7123,6534.123))
print("Test1: {a: 5d}, Prince{b: 4.2f}".format(a=7123,b=6534.123))

# "참고 : Escape 코드

# \n : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \r : 캐리지 리턴
# \f : 폼 피드
# \a : 벨 소리
# \b : 백 스페이스
# \000 : 널 문자"

print("'you'")
print('\'you\'')
print('\"you\"')
print("""'you'""")
print('\\you\\\n') # \n을 통해 줄바꿈 생성
print('\t\tyou\t') # \t 를 통해 탭키 효과 적용