"""
Method Overloading
Keyword - Overloading, OOP, Multiple dispatch
Method Overloading 이란 동일한 이름의 함수를 매개변수에 따라 다른 기능으로 동작하도록 설정하는 것

메소드 오버로딩 효과
1. 동일 메소드 재정의 -> 다형성 부여 (다양한 형태의 인자를 받을 수 있도록)
2. 네이밍 기능 예측
3. 코드 절약, 가독성 향상
4. 메소드 파라미터 기반 호출 방식 (메소드 오버라이딩과 큰 차이점)
"""


# Ex1
# 동일 이름 메소드 사용 예제
# 동적 타입 검사 -> 실행 시 타입 검사(타입 에러가 실행시에 발견) -> 기술면접에서 많이 물어본다.

class SampleA():
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    # Packing으로 해결 가능
    # def add(self, *args): # 인자를 언팩킹하여 인자가 몇개든 상관없이 사용할 수 있다.
    #     return sum(args)



a = SampleA()
# print('Ex 1 > ', a.add(2, 3)) # 바로 에러터진다 => 동일 메서드명이기에, 인자가 세개를 받는 add()가 호출된다.
# 파이썬에서는 메소드 오버로딩을 지원하지 않기 때문에 발생하는 에러

# 모든 속성 개체 확인
# print('Ex 1 > ', dir(a))

# Ex 2
# 동일 이름 메소드 사용 예제
# 자료형에 따른 분기 처리

class SampleB():
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)
        if datatype == 'str':
            return ''.join([x for x in args])

b = SampleB()
# Number
print('Ex 2 > ', b.add('int', 5, 6, 3))
print('Ex 2 > ', b.add('str', 'Hello', 'World'))

# Ex 3
# MultipleDispatch 패키지를 통한 메소드 오버로딩 -> pip install multipledispatch
from multipledispatch import dispatch
class SampleC():
    @dispatch(int, int)
    def product(self, x, y):
        return x * y

    @dispatch(int, int, int)
    def product(self, x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def product(self, x, y, z):
        return x * y * z

c = SampleC()
# 파라미터 2개
print("Ex 3 > ", c.product(3, 4))

# 파라미터 3개
print("Ex 3 > ", c.product(3, 4, 5))

# 파라미터 4개
print("Ex 3 > ", c.product(3.5, 4.0, 1.2))

# 각 상황에 맞게 dispatch, 오버로딩되어 메소드 호출
# 데이터 타입의 관점에서 메소드를 작성하여 구조성 있는 클래스 생

