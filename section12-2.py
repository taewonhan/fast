# section12-2
# 파이썬 데이터베이스 연동

import sqlite3

# db파일 조회
conn = sqlite3.connect('C:/python_basic/resource/database.db') # 본인 db 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# # 지정 로우 선택 (커서 위치가 2번째부터이므로 ,2,3,4 data를 가져옴)
# print('Three -> \n', c.fetchmany(size=3))

# # 전체 로우 선택
# print('All -> \n', c.fetchall())

print()

# 순회 1
# rows = c.fetchall()
# for row in rows:
#     print('retrive1 > ', row)

# # 순회2
# for row in c.fetchall():
#     print('retreve2 > ', row)

# 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('rertrieve3 > ', row)

print()

# WHERE Retrive1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?',param1)
print('param1',c.fetchone()) # 3번하나 선택됨
print('param1',c.fetchall()) # 이미 3번 하나만 선택하고, 그걸 불러왔기 때문에 남아있는건 없음


# WHERE Retrive2
param2 = (4,)
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2',c.fetchone()) # 4번하나 선택됨
print('param2',c.fetchall()) # 이미 4번 하나만 선택하고, 그걸 불러왔기 때문에 남아있는건 없음


# WHERE Retrive3

c.execute('SELECT * FROM users WHERE id=:Id' ,{"Id":5})
print('param3',c.fetchone()) # 4번하나 선택됨
print('param3',c.fetchall()) # 이미 4번 하나만 선택하고, 그걸 불러왔기 때문에 남아있는건 없음

# WHERE Retrieve4 여러개 가져오기
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

# WHERE Retrieve5 여러개 가져오기
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,4))
print('param5', c.fetchall())

# WHERE Retrieve6 여러개 가져오기
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{"id1":2,"id2":5})
print('param6', c.fetchall())

# DUmp 출력
with conn:
    with open('C:/python_basic/resource/dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s \n' % line)
        print('Dump Print complete')

# f.close(), conn.close() 저절로 된것임 (with문을 사용했기 때문)