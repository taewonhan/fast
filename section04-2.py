# section04-2 
# 문자열, 문자열연산, 슬라이싱

str1 = "I am a boy."
str2 = 'Niceman'
str3 = ' '
str4 = str('ddd')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\t"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'  # r'~'을 통해 그대로 출력 가능
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인 \를 통해 다음줄에도 계속 이어지게 함
multi = \
    """
    문자열
    나열
    테스트
    """

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100) # * 백번
print(str_o2 + str_o3) #문자 합쳐서 나열
# print(str_o1 + 3) -> 얘는 오류
print('a' in str_o4) # -> str_o4에 a가 있는지?
print('f' in str_o4)

# 문자열 형 변환
print(str(77)+'a') # 77이 문자화되었기때문에 77a로 프린트됨
print(str(10.4))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'

# print(a.islower()) # a가 소문자인지 테스트
# print(b.endswith('e')) # 마지막글자가 e로 끝나는지
# print(a.capitalize()) # 첫글자 대문자로하여 프린트
# print(a.replace('nice', 'good')) # nice를 good으로 변환하여 프린트
# print(list(reversed(b))) # b를 역순으로 리스트화

a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[:4])
print(a[0:])
print(a[0:len(a)])
print(a[:])

print(b[0:4:2]) # 점프기능
print(b[1:-2])
print(b[::-1])