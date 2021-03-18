"""
Chapter 2
Python Advanced(2) - Property(2) - Getter / Setter
Keyword - @Property

프로퍼티 사용 장점
1. 파이써닉한 코드
2. 변수 제약 설정
3. Getter, Setter 효과 동등(코드 일관성 지킬 수 있다)
 - 캡슐화 - 유효성 검사 기능 추가 용이
 - 대체 표현(속성 노출, 내부의 표현 은닉 가능)
 - 속성의 수명 및 메모리 관리 용이 -> 사용하지 않을 땐 클래스와 함께 소멸(클래스 내부에서 변수 선언, 사용하기에)
 - getter, setter 작동에 대해 설계된 여러 라이브러리 상호 운용성 증
"""

# Ex 1
# Propertry 활용 getter, setter 작성

# 캡슐화
class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0 # private

    # 만약 y뿐만 아니라 다수의 변수가 private으로 선언된다면, 각각에 대한 getter/setter 메소드를 일일이 구현해야한다.
    # 그런 귀찮은 일 대신 프로퍼티 어노테이션을 사용하면 된다.
    @property # 언더스코어를 제외한 변수 이름
    def y(self): # 이게 getter
        print('Called get method')
        return self.__y
    @y.setter
    def y(self, value):
        print('Called set method')
        self.__y = value
    @y.deleter # 메모리 절약
    def y(self):
        del self.__y
    # 위 세 메소드의 형태가 파이선 getter/setter의 표

    # 결국 getter, setter라는 거추장스러운 이름 사용대신, 어노테이션을 사용함으로
    # 직관적으로 y만 사용하여 메서드를 호출할 수 있다.(직관적으로 사용할 수 있음이 포인트)
a = SampleA()
a.x = 1
a.y = 2 # 자동으로 세터를 호출할 타이밍
print('Ex 1 > x: {}'.format(a.x))
print('Ex 1 > y: {}'.format(a.y))

## deleter
print('Ex 1 - 1 >', dir(a))
del a.y
print('Ex 1 - 2 >', dir(a)) # _SampleA__y 메소드가 사라진다.

print(' ')

class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0 # private

    @property # 언더스코어를 제외한 변수 이름
    def y(self): # 이게 getter
        return self.__y
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError('0 보다 큰 값을 입력하세요.')
        self.__y = value
    @y.deleter # 메모리 절약
    def y(self):
        del self.__y

b = SampleB()

b.x = 1
b.y = 10

print('Ex 2 > x: {}'.format(b.x))
print('Ex 2 > y: {}'.format(b.y))

b.y = -5 # 설계에 위반되는 값 => 예외 발생


# 위에서 배운 내용을 토대로, 내 입맛대로 커스터마이징하거, 제약조건을 추가하면서 수정할 수 있다.
# 내가 의도한 흐름에 맞게 프로그램을 설계할 수 있다.

# 있는 그대로를 사용하기보다, 있는 것을 개선하려는 노력이 개발력을 높인다.

class Lim:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.age
    @age.setter
    def age(self, value):
        self.age = value
