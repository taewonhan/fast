# section11
# 파이썬 외부 파일 처리
# 파이썬 excel, csv파일 읽기 및 쓰기

# CSV : MIME - text/csv
import csv

# 예제 1
with open('./resource/sample1.csv', 'r') as f:
    reader =csv.reader(f)
    # next(reader) # 첫행 제외
    # 확인
    print(reader)
    print(type(reader))
    print()

    for c in reader:
        print(c)

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader =csv.reader(f, delimiter='|') # | 를 삭제하고 구분콤마 삽입
    # next(reader) # 첫행 제외
    # 확인
    print(reader)
    print(type(reader))
    print()

    for c in reader:
        print(c)

# 예제3(dict변환) 첫행을 key로 가정하고 바로바로 딕셔너리 만듦
with open('./resource/sample1.csv','r') as f :
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k,v)
        print('----------')


# 예제4 
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
with open('./resource/sample3.csv','w', newline='') as f: # 줄바꿈 추가로 안하고 쓰기
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v) # 한줄씩 쓰는 함수
# 예제5
with open('./resource/sample3.csv','w', newline='') as f: # 줄바꿈 추가로 안하고 쓰기
    wt = csv.writer(f)
    wt.writerows(w) # 얘는 for문 안써도 바로 한줄씩 쓸 수 있음. 별 조건 없이 모든 data를 쓸때는 이게 편함

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용함!
# pip install xlrd
# pip install openpyxl
# pip install pandas 

import pandas as pd

# sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자
xlsx = pd.read_excel('./resource/sample.xlsx')




# 상위 데이터 확인
print(xlsx.head())
print('---')
 
# 꼬리 데이터 확인
print(xlsx.tail())
print('---')

# 행, 열데이터 확인
print(xlsx.shape)

# 엑셀 or csv다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index =False)
xlsx.to_csv('./resource/result.csv', index =False)