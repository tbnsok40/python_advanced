
> ### 메소드 오버라이딩
- 오버라이딩은 부모 클래스의 메소드를, 자식 클래스에서 재정의 하여 사용하는 것을 의미한다.
- 예를 들어 부모클래스에서 add()라는 메서드는 2개의 인자밖에 더할 수 없지만, 자식 클래스의  add() 메소드는 오버라이딩되어 3가지의 인자까지 받도록 재정의 할 수 있다.

1. 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용가능
3. 부모클래스의 메소드를 추상화 후 사용가능 (구조적 접근 가능)
4. 확장 가능 + 다형성(다양한 방식으로 동작 -> 부모에서 메소드 하나를 만들지만,사용하는 자식에 따라 다양하게 사용될 수 있다)
5. 가독성 증가, 오류가능성 감소, 메소드 이름 절약(부모가 메소드 이름을 이미 정의해놨기에)


> #### dir(),\__dict__ 객체 내부 검사 메서드
- dir() : 클래스와 인스턴스 내부에서 사용할 수 있는 정보를 확인 
- \__dict\__ : 인스턴스 내부에 어떤 속성이 있는지 확인 
	- 자식 클래스가 부모클래스를 상속받는다 하더라도, 인스턴스화 되기 전엔 \__dict__ 의 결과가 다르다. (인스턴스화 시점에 내부 속성까지 상속)    
- 내용이 어려우니 코드로 확인해보자
    
``` python
# 기본 Overriding 예제
class ParentEx1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx1(ParentEx1):  # ParentEx1 상속 갱
	# 오버라이딩(재정의)하지 않았다.
    pass
```

```python
# ChildEx1()는 c1 변수에게 할당하기 전까진, 인스턴스화된 것 아니다.
c1 = ChildEx1() 

# ParentEx1()도 마찬가지
p1 = ParentEx1()

print('Ex 1 >', c1.get_value())
>>> 5
# 메소드 재정의(오버라이딩)가 없었기 때문에 부모클래스에서 지정한 값을 그대로 출력


# c1의 모든 속성 출력
print(dir(c1))  # get_value, value를 가지고 있다.

# 부모 & 자식의 모든 속성값 출력
print('Ex 1 > ', dir(ParentEx1))
print('Ex 1 > ', dir(ChildEx1))  
# 메소드가 같다 -> 부모 클래스의 get_value() 메소드를 상속받는다.

print('Ex 1 >', ParentEx1.__dict__)
print('Ex 1 >', ChildEx1.__dict__)

```

- 딕셔너리로 네임스페이스내의 속성들을 확인하는데, 부모에게는 있지만, 자식에게는 없다.
- 인스턴스가 되는 시점에 자식에게 담기는 것이다(c1=ChildEx1 이렇게 할당하는 것이 인스턴스화 시점, 그렇기 때문에 dir()과 \__dict__로 찍을때 다르게 나온다.


> ### 메소드 오버라이딩 예제
- 아래 예제에선 메소드 오버라이딩이 일어나, get_value라는 메소드에서 기존 self.value에 10을 곱하여 리턴하게 된다.

``` python
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

# Ex1 과 달리 Ex2에선 메소드 오버라이딩이 일어났기 때문에, 5가 아닌 50이 출력된다.
```

<br />

> ### 메소드 오버라이딩 다형성 예제

``` python
import datetime

# 부모 클래스
class Logger():
    def log(self, msg):
        print(msg)

# Logger의 TimestampLogger라는 자식 (자식1)
class TimestampLogger(Logger):
    def log(self, msg):
        message = '{ts} {msg}'.format(ts=datetime.datetime.now(), msg=msg)
        super().log(message) # 부모클래스의 log() 메소드로 message인자를 넘겨벌임
        # super(TimestampLogger, self).log(message) # 위 코드와 다를 바 없지만 더 명확하다, # fm style 로 코딩한 것


# Logger의 DateLogger라는 자식 (자식2) ==> 여러 자식 생김 : 다형성
class DateLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime('%Y-%m-%d'), msg=msg)
        super().log(message)

```

<br/>


> #### 다형성
하나의 부모(Logger 클래스)를 정하고,
다양한 형태(TimestampLogger, DateLogger 클래스)로 상속을 받는다.

```python
# 뼈대는 부모가 제공 <출력 기능 print(msg)> => 출력할 메세지의 형태는 자식이 결정
l = Logger()
t = TimestampLogger()
d = DateLogger()
# 인스턴스 생성되면서, 부모클래스의 속성 상속 완료


l.log('test1')
t.log('test2')
d.log('test3')

>>> test1
>>> 2021-04-06 21:12:30.730855 test2
>>> 2021-04-06 test3
```
분명 하나의 부모클래스에서 log() 메소드를 상속받았지만, 자식 클래스에선 다양한 형태로 출력됨을 확인 할 수 있다. 이렇듯 메소드 오버라이딩을 통해 다형성 구현이 가능하다.

<hr />

> ### 파이썬 메소드 오버로딩
- 동일 클래스 내에서, 매개변수의 개수 또는 자료형(int, float 등)이 다른 동명의 메소드를 정의하는 것.
즉, 클래스 내에서 **같은 이름의 메소드를 여러 개 선언**하는 것을 의미한다.
- Q. 왜 이런 것을 만드느냐?.! 
- A. 다양한 매개변수를 받아 처리할 수 있도록 하기 위함이다.
ex) 더하기 메소드를 만들 때, 두개의 매개변수만 받는 메소드와, 세개의 매개변수, 혹은 그 이상 개수의 매개변수를 받을 수 있는 더하기 메소드를 만들 수 있다 (동일한 메소드 이름으로)


> #### Ex 1
- 동일 이름 메소드 사용 예제
- 동적 타입 검사 -> 실행 시 타입 검사(타입 에러가 실행시에 발견) -> 기술면접에서 많이 물어본다.

``` python
class SampleA():
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    # def add(self, *args): # 인자를 언팩킹하여 인자가 몇개든 상관없이 사용할 수 있다.
    #     return sum(args)

a = SampleA()
```
이렇게 동일 네이밍으로 서로 다른 개수의 매개변수를 받지만, 아래에서 보면 (Java와 달리) 바로 에러 터진다.

```python
print('Ex 1 > ', a.add(2, 3)) 
>>> TypeError: add() missing 1 required positional argument: 'z'

# 바로 에러터진다 => 동일 메서드명이기에, 인자가 세개를 받는 add()가 호출된다.
```
- 파이썬에서는 메소드 오버로딩을 지원하지 않기 때문에 발생하는 에러
- 자바에서는 오버로딩 가능하기 때문에, 동일한 네임이면서 여러개 만들어 서로 다른 인자 갯수를 받는 메서드를 만들 수 있다.

<br/>

> #### Ex 2
- 동일 이름 메소드 사용 예제
- 자료형에 따른 분기 처리

``` python
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
```


> #### Ex3
- MultipleDispatch 패키지를 통한 메소드 오버로딩 ➡️ pip install multipledispatch ➡️ 메소드에 @dispatch 어노테이션을 붙여 적용 ➡️ 이제 자바에서 처럼 오버로딩 가능


```python
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
>>> Ex 3 >  12

# 파라미터 3개
print("Ex 3 > ", c.product(3, 4, 5))
>>> Ex 3 >  60

# 파라미터 3개 자료형 float
print("Ex 3 > ", c.product(3.5, 4.0, 1.2))
>>> Ex 3 >  16.8
```
- 각 상황에 맞게 dispatch, 오버로딩되어 메소드 호출
- Ex2와 다르게 일일이 데이터 타입을 명시할 필요없이, @dispatch 어노테이션 덕분에 자동으로 처리된다.
- 데이터 타입의 관점에서 메소드를 작성하여 구조성 있는 클래스 생성