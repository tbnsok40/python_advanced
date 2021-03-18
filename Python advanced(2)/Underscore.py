"""
Chapter2

Keyword - access modifier(접근지정자), underscore

"""
"""
다양한 언더스코어활용
파이썬 접근지정자 설명
"""

# EX 1
# Use underscore
# 1. 인터프리터, 2.값 무시, 3.네이밍(국제화, 자릿수)

# Unpacking - packing(*)
x, _, y = (1,2,3)
print(x,y)

a, *_, b = (1,2,3,4,5)
print(a, b)

print('Ex 1 > ', x, y, a, b)

for _ in range(10): #무시할 때 사용
    pass

for _, val in enumerate(range(10)):
    pass

# EX 2
# 접근 지정자
# name: public 변수
# _name: protected
# __name: private (instance)
# 파이썬 -> public: 강제성 x : 약속된 규약에 따라 코딩을 장려(강제적이지 않다, 자유도, 책임감 장려)
# 타 언어 : 클래스 변수, 인스턴스 변수 값 쓰기 장려 안함: 타 언어 -> Naming Mangling
# 타 클래스: __로 시작하는 변수에는 접근하지 않는 것이 원칙 : 파이썬은 접근함으로써 프로그램의 흐름을 조작하거나 다른 활용 가능

# When No use Property
class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0 # private instance
        self._z = 0

a = SampleA()
a.x = 1
# a.__y = 3
print('0: ', dir(a))
print('Ex 2 > x: {}'.format((a.x)))
# print('Ex 2 > y:{}'.format((a.__y))) # attributeError발생
print('Ex 3 > z: {}'.format((a._z)))

print('Ex 2 > ', dir(a)) # __y는 형태가 바뀌어 저장된 것을 확인할 수 있다.

a._SampleA__y = 2 # 수정 가능(강제성이 없다 but 룰로써는 지켜야한다)

print('Ex 2 > y : {}'.format(a._SampleA__y))
print(" ")

# Ex 3
# 메소드 활용, Getter, Setter
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0 # _SampleB__y = 0
    def get_y(self): # get_y를 통해 y를 가져가 -> 바로 윗줄처럼 직접 가져갈 필요 없도
        return self.__y

    def set_y(self, value):
        self.__y = value

b = SampleB()
b.x = 1
b.set_y(200) # y의 값을 2로 세팅한다

print('Ex 3 > x : {}'.format(b.x))
print('Ex 3 > y : {}'.format(b.get_y()))

print("Ex 3 > dir(b) : ", dir(b))
# 자동으로 변환된 메서드명과 우리가 직접 만든 메서드(getter/setter)가 추가됐음을 확인할 수 있다.








