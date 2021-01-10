# section07-1
# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요!
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명: 
    # 함수1
    # 함수2 

# 예제1
class UserInfo:
    def __init__(self, name):
        self.name = name
    
    def user_info_p(self):
        print("Name: ",self.name)
    

user1 = UserInfo("Han")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))

print(user1.__dict__)
print(user2.__dict__)

# 예제2 
# self의 이해

class SelfTest():

    def function1():
        print('function1 called!')
    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
# self_test.function1() # 얘는 오류 .func1은 인자가 없기 떄문에 호출 안됨 
SelfTest.function1() # 호출하려면 class단에서 호출해야함
self_test.function2()

print(id(self_test))  # self_test인자가 저절로 fucntion2의 self로 이동해서 프린트됨!


# 예제3 
# 클래스변수, 인스턴스변수
class WareHouse():
    stock_num = 0
    def __init__(self,name):
        self. name = name
        WareHouse.stock_num +=1
    def __del__(self):
        WareHouse.stock_num -=1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스 ,클래스 변수 공유
 
print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 원래는 클래스꺼지만, 클래스 변수는 공유하기때문에, 3이 도출됨!
print(user2.stock_num) # 원래는 클래스꺼지만, 클래스 변수는 공유하기때문에, 3이 도출됨!
print(user3.stock_num) # 원래는 클래스꺼지만, 클래스 변수는 공유하기때문에, 3이 도출됨!

del user1 # user1 인스턴스 삭제
print(user2.stock_num) # 원래는 클래스꺼지만, 클래스 변수는 공유하기때문에, 2가 도출됨!
print(user3.stock_num) # 원래는 클래스꺼지만, 클래스 변수는 공유하기때문에, 2가 도출됨!
