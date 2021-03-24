"""

Meta class(1)
keyword - class of class, type, meta class, custom meta class

메타클래스
1. 클래스를 만드는 역할 (메타 클래스니까) -> 의도하는 방향으로 클래스를 커스텀 하겠다.
2. 프레임우크 작성 시 필수
3. 동적 생성, 커스텀 생성 가능하게 함 (by type())
4. 커스텀 클래스 -> 검증 클래스 등
5. 엄격한 class 사용 요구, 메소드 오버라이드 요
6.

"""

# Ex 1
# type 예제
class SampleA():
    pass

obj1 = SampleA() # obj에 할당한 순간, 클래스를 인스턴스화 한 것

print("Ex 1 > ", obj1.__class__) # instance의 속성
print('Ex 1 > ', type(obj1)) # >>> SampleA
print("Ex 1 > ", obj1.__class__.__class__) # type: #python 에서 모든 클래스의 원형, 메타 클래스가 if 된다:
# 그렇기 때문에 우리가 type함수를 손볼 수 있다면, 동적으로 클래스를 만들 수 있고, 필요할 때마다 클래스를 만들어 낼 수 있다.
print("Ex 1 > ", obj1.__class__ is type(obj1))
print("Ex 1 > ", obj1.__class__.__class__ is type(obj1).__class__)
print("Ex 1 > ", type.__class__) # 핵심: type()의 클래스도 type()이다

# The one thing: 모든 클래스의 메타 클래스는 type 함수!!

# 현실의 사물을 클래스 형태로 제작하는 것: 객체지향
# 파이썬에선 클래스와 객체를 같이 사용 ( class == object )


# Ex2
# type meta(EX1 증명)

# int , dict

n = 10
d = {'a': 10, 'b': 20}
class SampleB():
    pass
obj2 = SampleB()

for o in (n, d, obj2):
    print('Ex2 > {}, {}, {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))
    # 표현 할 수 있는 모든 것의 메타클래스는 type()이다.
print(' ')
for t in int, float, list, tuple:
    print('Ex 2 > ', t, ' : ', type(t))
print(' ')
print('Ex 2 > ', type(type))

# 어떤 변수, 클래스, 인스턴스의 원형 : type. 원형의 원형: type