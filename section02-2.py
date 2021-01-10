# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding) # 입력 기본
print(sys.stdout.encoding) # 출력 기본

# 출력문
print("My name is HTW!")

# 변수 선언
myName = 'HTW'

# 조건문
if myName == 'HTW':
    print('OK')

# 반복문
for i in range(1,10) :
    for j in range(1,10) :
        print('%d * %d = ' % (i,j),i*j)

# 함수 선언 (함수이름 한글도 가능)

def greeting():
    print("안녕하세요. 반갑습니다.")

greeting()

# 클래스
class Cooking():
    pass

# 객체 생성(인스턴스)
cookie = Cooking()

print(id(cookie))
print(dir(cookie))