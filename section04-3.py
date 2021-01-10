# Section04-3
#파이썬 데이터타입(자료형)
# 리스트 ,튜플

# 리스트(순서o , 중복o, 수정o, 삭제o)
# 선언 대괄호

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'banana', 'orange']
e = [10, 100, ['pen', 'banana', 'orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱]
print(d[0:3])
print(e[2][1:3])

#연산
print(c + d) # c 다음에 d 리스트 추가
print(c * 3) # 리스트 세번 반복
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 1000] # c 1~2 사이에 리스트 삽입!
print(c)

c[1] = ['a', 'b', 'c'] # c[1]에 리스트 대체!
print(c)

del c[1]
print(c)
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 끝부분에 추가
print(y)
y.sort()
print(y) # 오름차순정렬
y.reverse()
print(y)
y.insert(2,7) # 2번 인덱스에 삽입(대체가 아님!)
print(y)
y.remove(2) # 숫자 2를 삭제
print(y)
y.pop() # 맨마지막 인덱스를 꺼냄(후입선출)
print(y)
ex = [88, 77]
y.extend(ex) # 리스트 안에 인덱스로 연장
print(y)
y.append(ex) # 리스트 안에 리스트로 추가
print(y)


# 튜플 (순서o, 중복 o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1,2,3,4)
d = (10,100,('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)
print()
# 튜플 함수

z = (5,2,1,3,4)

print(z)
print(3 in z)
print(z.index(5)) # 5가 있는 인덱스값
print(z.count(1)) # 1의 갯수