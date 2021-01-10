# Section 05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :",v1)
    v1 +=1

for v2 in range(10):
    print("v2 is:",v2)

for v3 in range(1,100):
    print("v3is:",v3)

# 1~ 100 합
sum1 = 0
cnt1 = 1

while cnt1 <=100:
    sum1 +=cnt1
    cnt1 +=1

print("1~100:",sum1)
print("1~100:",sum(range(0,101))) # 얘도 꿀팁!!
print("1~100:",sum(range(0,101,2)))

# 시퀀스 (순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴함수: range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho","Choi", "Yoo"]

for name in names :
    print("You are :", name)

word = "dreams"

for s in word:
    print("Word is:", s)  # 문자열도 순서대로 나열함. 만약 dreams만 나타내고 싶으면 ["dreams"] 이렇게해야함

my_info = {
    "name" : "Kim",
    "age" : "33",
    "city" : "seoul"
}

for key in my_info:
    print("my_info",key)  # 기본값은 키다!

for value in my_info.values():
    print("my_info",value) # value는 따로 .values로 지정해야함

for key, value in my_info.items():
    print("my_info",key,value) # itmes는 따로 .items로 지정해야함


name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else :
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found: 33")
        break  # 조건만족시 for문 끔

    else:
        print("not found")

else : 
    print("Not found 33...") # for문에서도 else를 쓸 수 있음 break를 만났기 때문에 else문이 실행 x


# continue

lt = ["1",2,5,True,4.3,complex(4)]
for v in lt:
    if type(v) is float :
        continue  # if 문을 만족하면 pass하게됨(아래 결과문 실행 x) -> 다시 for문으로 돌아감
    print("타입:",type(v))