# section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 에외 처리도 중요
# linter : 코드스타일 ,문법체크

# SyntaxError : 잘못된 문법
# print('Test)
# if True
#     pass
# x => y

# NameError : 참조변수가 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0나누기에러
# print(10/0)

# IndexError : 인덱스 범위 오버
# x = [10,20,30]
# print(x[3])

# KeyError
# dic = {'name': 'kim', 'age':33, 'city': 'seoul'}
# # print(dic['hobby']) # 키에러 발생
# print(dic.get('hobby')) # 얘는 None으로 산출

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month()) # month는 import하지 


# # ValueError : 참조값이 없을 때 발생
# x = [1,5,9]
# x.remove(10)
# x.index(10)

# FileNotfoudError 
# f = open('test.txt','r')

# TypeError
x = [1,2]
y = (1,2)
z = 'test'
# print(x + y)
# print(x + z)

# 예외처리기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행


# 예제1
name = ['kim','lee','park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError:
    print('Not Found it - occurred ValueError')
else:
    print("ok, else")

# 예제2
name = ['kim','lee','park']

try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError:
    print('Not Found it - occurred Error')
else:
    print("ok, else")

# 예제3
name = ['kim','lee','park']

try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError:
    print('Not Found it - occurred Error')
else:
    print("ok, else")
finally:
    print("ok")

# 예제4
# 예외처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('try')
finally:
    print('ok finnaly')

# 예제5
name = ['kim','lee','park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError:
    print('Not Found it - valueError')
except IndexError:
    print('Not Found it - indexError')
except Exception:
    print('Not Found it - occurred Error') # 순서적으로 협의 - > 광의 에러로 나아가야함
else:
    print("ok, else")
finally:
    print("ok")


# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생시키기
try :
    a = 'kim'
    if a == 'kidm':
        print('ok')
    else:
        raise ValueError
except ValueError:
    print('문제발생')
except Exception as f:
    print(f)
else:
    print('ok')