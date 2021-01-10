# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   코드

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요
# 예제1
def hello(world):
    print("Hello", world)

hello("python!")
hello(22)

# 예제2
def hello_return(world):
    val = "Hello" + str(world)
    return val

str2 = hello_return("Python!!!!")
print(str2)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제3-1(다중리턴 -> 리스트로 변환)
def func_mul2(y):
    y1 = y * 100
    y2 = y * 200
    y3 = y * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt)

# 예제 4
# *args : 여러개의 parameter를 기입할 수 있음(사전에 몇개인지 안정해도 됨), *kwargs
def args_func(*args):
    print(args)

def args_func2(*args):
    for i , v in enumerate(args): # 형식은 튜플인데도, enumerate를 사용해서 인덱싱할 수 있음
        print(i,v) 

args_func2('kim','lee')

# kwargs
def kwargs_func(**kwargs): # 별표 두개는 딕셔너리
    print(kwargs)

kwargs_func(name1 = 'kim', name2 = 'han', name3 = 'park')

def kwargs_func2(**kwargs): # 별표 두개는 딕셔너리
    for k, v in kwargs.items():
        print(k,v)

kwargs_func2(name1 = 'kim', name2 = 'han', name3 = 'park')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10,20)
example_mul(10,20, 'park', 'kim', age1=24, age2=26) # 자동으로 튜플형태는 args, 딕셔너리형태는 kwargs로 변환

# 예제5
# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num): # (1) 일단  num에 10000을받고
        print('>>',num)       # (4) 11000을 넣은 값 프린트
    print("in func")        # (2) 실행
    func_in_func(num + 1000) # (3) num + 1000 을 파라미터로 func_in_func함수를 실행

nested_func(10000) 

# 예제6 -힌트
def func_mul3(x : int) -> list : # Int형태를 넣어야하고, 리스트로 리턴된다는것을 언지가능
    y1 = x *100
    y2 = x *200
    return [y1, y2]

print(func_mul3(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결함
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화


# 일반적 함수 -> 변수할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)  # mul_10에 이미 메모리가 할당된 상태
print(type(var_func))
print(var_func(10))

# 람다식
lambda_mul_10 = lambda num2 : num2*10 

print(lambda_mul_10(10))

#
def func_final(x,y,func):
    print(x * y * func(10))
func_final(10,10,lambda_mul_10)

print(func_final(10,10,lambda x : x * 1000))