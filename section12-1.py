# Section 12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now:', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime:',nowDatetime)

# sqlite3
print('sqlite3.version:',sqlite3.version)
print('sqlite3.sqite_version:', sqlite3.sqlite_version)

# DB생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type: ', type(c))

# 테이블 생성(Data Type : Text, Numeric Integer, Real, Blob)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입 물음표 처리하고, 뒤쪽에서 튜플형태로 함수나 변수로 설정 가능
c.execute("INSERT INTO users VALUES(1, 'Kim', 'cnrncjwo@naver.com','010-8834-2202', 'han.com', ?)", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",(2, 'Park', 'park@daum.net', '010-0000-2222','park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3,'Lee','Lee@naver.com','010-2222-3333', 'lee.com',nowDatetime),
    (4, 'Cho','Chow@daum.net','010-3333-4444','chow.com', nowDatetime),
    (5, 'yoo','yoo@google.com','010-4444-5555','yoo.com', nowDatetime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount) # 몇줄의 db를 지웠는지도 알려줌

# Commit : isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()