# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

#딕셔너리(Dict) : 순서x , 중복x(키는 중복 x, 값은 중복 가능), 수정o, 삭제o

# Key, Value로 구성됨

# 선언
a = {'name' : 'Han', 'phone' : '010-8834-2202', 'birth' : 930619}
b = {0:'Hello python', 1: 'Hello coding'}
c = {'arr' : [1,2,3,4,5], }

print(a['name'])
print(a.get('name'))
print(a.get('name1')) # 오류가 발생하지 않고, None으로 조회됨
print(c['arr'][1])

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3)
print(a)

# keys, values, items(키와 밸류 한쌍)
print(a.keys())
# print(a.keys()[0]) # 인덱싱은 안됨
print(list(a.keys())[1]) # 따로 keys를 리스트화 한 후 인덱싱 가능

print(a.items()) # key와 value를 한쌍으로 묶어서
print(list(a.items())) # 리스트 안에 튜플형태로 묶어서

# 집합(Sets) 순서x, 중복x
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c) # 중복이 안되니, 6 한번만 뜸

# Set의 형변환
t = tuple(b)
print(t)
l = list(b)
print(l)

print()

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 교집합

print(s1 | s2) # 합집합
print(s1.union(s2)) # 합집합

print(s1 - s2) # 차집합
print(s1.difference(s2)) # 차집합

# 추가 & 제거
s3 = set([7,8,10,15])

s3.add(18)

print(s3)

s3.remove(15)
print(s3)