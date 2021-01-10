#section009
# 파일 읽ㄱ, 쓰기
# 읽기모드 : r , 쓰기모드(기존 파일 삭제) :w , 추가 모드 : a
# .. : 상대경로 , .: 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open


# 파일 읽기
# 예제 1
f = open('./resource/review.txt','r')
content = f.read()
print(content)

# 반드시 close로 리소스를 반환해야함
f.close()
print()
# 예제2  with는 따로 close 안해도 됨
with open('./resource/review.txt','r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print()

# 예제3
with open('./resource/review.txt','r') as f:
    for c in f:
        print(c)  # 한 line단위로 출력됨
        print(c.strip())
print()
# d예제4
with open('./resource/review.txt','r') as f:
    content = f.read()
    print(">", content)  # 얘는 프린트 가능
    content = f.read()
    print(">", content) # 이후에는 커서가 문서의 맨 마지막으로 가있기 때문에 추가적으로 읽어올 내용 없음

# 예제5
with open('./resource/review.txt','r') as f:
    line = f.readline()
    # print(line) # 한 줄 읽음
    while line :
        print(line, end='')
        line = f.readline()
print()
# 예제6
with open('./resource/review.txt','r') as f:
    contents = f.readlines() # 리스트형태로 가지고 있음
    print(contents)
    for c in contents:
        print(c, end='****')
print()
# 예제 7
score = []
with open('./resource/score.txt','r') as f:
    
    for line in f:
        score.append(int(line))
    print(score)

print('average: {:6.5}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('Niceman\n')

# 예제2
with open('./resource/text1.txt','a') as f:
    f.write('goodman\n')

# 예제3
from random import randint
with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(0,46)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제5 
with open('./resource/text4.txt','w') as f:
    print('Test Contests1', file=f) # print문을 파일로 직접 저장가능
    print('Test Contests2', file=f)