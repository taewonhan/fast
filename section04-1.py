# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name " : "Han",
    "age" : 28
}

v_list = [3, 5, 7]
v_tuple = 3,5,7 # ( 튜플 )로 정의하기도 함
v_set = {7, 8, 9}
print(type(v_str1))
print(type(v_tuple))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999
big_int2 = 777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2) # type이 저절로 실수로 바뀌게 됨!

a = 5.
b = 4
c = 10

print(type(a))
print(type(b))
result2 = a + b
print(type(result2))  # 실수로 자동 변환!

# type 변환 (유연한 형변환 가능)
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(int(True))
print(float(True))
print(int('3'))

y = 100
y +=100 # y = y + 100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# https://docs.python.org/3/library/math.html

print(abs(-7))
n, m = divmod(100, 8) # 몫과 나머지를 각각 할당
print(n, m)

import math

print(math.ceil(5.1)) # 5.1보다 큰 가장작은정수
print(math.floor(3.8)) # 3.8보다 작은 가장큰정수