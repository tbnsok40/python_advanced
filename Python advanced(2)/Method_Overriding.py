"""
Method Overriding
Keyword - Overriding, OOP, 다형성

-

메소드 오버라이딩 효과
1. 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용가능
3. 부모클래스의 메소드를 추상화 후 사용가능 (구조적 접근 가능)
4. 확장 가능 + 다형성(다양한 방식으로 동작 -> 부모에서 하나를 만들었지만, 사용하는 자식에 따라 다양하게 사용될 수 있다)
5. 가독성 증가, 오류가능성 감소, 메소드 이름 절약(부모가 메소드 이름을 이미 정의해놨기에)
"""


# Ex 1
# 기본 Overriding 예제
class ParentEx1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx1(ParentEx1):  # 상속 갱
    pass


c1 = ChildEx1()
p1 = ParentEx1()

print('Ex 1 >', c1.get_value())

# c1의 모든 속성 출력
print('Ex 1 >', dir(c1))  # get_value, value를 가지고 있다.

# 부모 & 자식의 모든 속성값 출력
print('Ex 1 > ', dir(ParentEx1))
print('Ex 1 > ', dir(ChildEx1))  # 메소드가 같다.

print()

print('Ex 1 >', ParentEx1.__dict__)
print('Ex 1 >', ChildEx1.__dict__)
print("---------------------------")


# 딕셔너리로 네임스페이스내의 속성들을 확인하는데, 부모에게는 있지만, 자식에게는 없다.
# 인스턴스가 되는 시점에 자식에게 담기는 것이다. 그렇기 때문에 dir()과 __dict__로 찍을때 다르게 나온다.
# dir(), __dict__ 객체 내부 검사 메서드
# dir() - 클래스와 인스턴스 내부에서 사용할 수 있는 정보를 확인 / __dict__ :  인스턴스 내부에 어떤 속성이 있는지 확인

# Ex 2
# 기본 Overriding 메소드, 재정의

class ParentEx2():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx2(ParentEx2):
    def get_value(self):  # 메소드 변경 => 메소드 오버라이딩
        return self.value * 10


c2 = ChildEx2()
print("Ex 2 >", c2.get_value())

# Ex3 - 오버라이딩 다형성 예제
import datetime


class Logger():
    def log(self, msg):
        print(msg)


class TimestampLogger(Logger):
    def log2(self, msg):
        message = '{ts} {msg}'.format(ts=datetime.datetime.now(), msg=msg)
        super().log(message)

        # 자식클래스의 프로토타입, 인스턴스를 super()의 인자로 넘긴 것
        # super(TimestampLogger, self).log(message) # 위 코드와 다를 바 없지만 더 명확하다, # fm style 로 코딩한 것

    # def log()는 결국 부모에게서 상속받은 메서드 => 같은 이름을 사


class DateLogger(Logger):
    def log2(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime('%Y-%m-%d'), msg=msg)
        super().log(message)
        # super(TimestampLogger, self).log(message) # 에러 나니까 위 코드로 실행 -> 편하다


# 하나의 부모를 정하고 다양한 형태로 상속을 받는다.

# 뼈대는 부모가 제공 (출력 기능) => 출력할 메세지의 형태는 자식이 결정
l = Logger()
t = TimestampLogger()
d = DateLogger()

# 메소드 재정의 실습
print('========= Ex 3 =========')
print('Ex 3 > ', l.log('Called logger'))
print('Ex 3 > ', t.log('Called Timestamp logger'))
print('Ex 3 > ', d.log('Called Datetime logger'))

# l.log('test1')
# t.log('test2')
# d.log('test3')