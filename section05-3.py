# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k,v in q1.items():
    if k == "가을":
        print(v)



# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k , v in q2.items():
    if v == "사과":
        print("존재함")
        break
else:
    print("존재하지 않음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

grade = 77
if grade <= 100 and grade >=81:
    print("A학점")
elif grade >= 61:
    print("B학점")
elif grade >=41:
    print("C학점")
elif grade >=21:
    print("D학점")
else : 
    print("E학점")


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 62
c= 18
if a >b:
    if b>c:
        print(a)
    elif c>a:
        print(c)
elif b>c:
    print(b)
else :
    print(c)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:
    if v =="정":
        continue
    else:
        print(v,end='')

print()
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
q7 = range(1,101)
for s in q7:
    if s %2 == 1:
        print(s,end=' ')

print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for f in q4:
    if len(f) >=5:
        print(f, end= ' ')

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for h in q5:
    if h.islower():
        print(h,end='')

print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for b in q6:
    if b.islower():
        print(b.upper(),end='')
    else :
        print(b.lower(),end='')