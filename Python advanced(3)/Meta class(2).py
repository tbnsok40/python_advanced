"""
Meta class(2)
Keyword - Type(name, base, dct), Dynamic Metaclass

메타클래스
1. 메타클래스 동적 생성 중요
2. 동적 생성한 메타클래스 -> 커스텀 메타클래스를 생성할 수 있다.
3. 의도하는 방향으로 직접 클래스 생성에 관여할 수 있는 큰 장점
"""


# Ex 1
# type 동적 클래스 생성 예제

# Name(이름) Bases(상속), Dct(속성, 메소드) <- type함수는 세가지 인자를 받는다
class Sample1():
    pass


s1 = type('Sample1', (), {})  # base, dct를 빈값으로 넣었다
print('Ex 1 > ', s1)
print('Ex 1 > ', type(s1))  # type meta class의 meta class
print('Ex 1 > ', s1.__base__)  # 클래스의 base는 object --> 모든 클래스는 object를 상속받는 것을 증명
print('Ex 1 > ', s1.__dict__)
print()


# dynamic 생성 + 상속
class Parent1:
    pass


s2 = type('Sample2', (Parent1,), dict(attr1=100, attr2='hi'))
# 2번째 인자: 튜플형태 -> 여러인자를 받을 수 잇따.
# key-value형식으로 넣은 것이 아니기 때문에, key에 따옴표 안붙인다.
print('Ex 2 > ', s2)
print('Ex 2 > ', type(s2))
print('Ex 2 > ', s2.__base__)
print('Ex 2 > ', s2.__dict__)
print('Ex 2 > ', s2.attr1, s2.attr2)  # 100, hi에 접근 가능
# 위와 같은 방식으로 클래스를 생성할 수 있다.

# 아래 형태의 클래스를 위에서 만든
# class Sample2():
#     attr1 = 10
#     attr2 = 'hi'
print()


# Ex2
# type 동적 클래스 생성 + 메소드
class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n


ex = SampleEx()
print('Ex 2 > ', ex.attr1)
print('Ex 2 > ', ex.attr2)
print('Ex 2 > ', ex.add(100, 200))
print('Ex 2 > ', ex.mul(10, 20))

print()

# 위 내용을 아래처럼 동적으로 생성할 수 있다.
s3 = type('Sample3',
          (object,),
          dict(attr1=30, attr2=100, add=lambda x, y: x + y, mul=lambda x, y: x * y)
          # {'attr1': 30, 'attr2': 100, 'add':lambda x, y: x + y, 'mul':lambda x, y: x * y}
          )
print('Ex 2 > ', s3.attr1)
print('Ex 2 > ', s3.attr2)
print('Ex 2 > ', s3.add(100, 200))
print('Ex 2 > ', s3.mul(10, 20))

# python low level에서 메소드를 조작하기 위해 배운다.
