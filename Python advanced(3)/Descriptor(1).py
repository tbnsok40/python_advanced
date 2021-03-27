"""
Keyword - descriptor, set, get, del, property

1. 객체에서 서로 다른 객체를 속성값으로 가지는 것
2. Read, Write, delete 등을 미리 정의 가능
3. date descriptor
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
"""

# Ex 1
# 기본적인 Descriptor 예제


class DescriptorEx1(object):
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, objtype):
        return 'Get method called. -> self : {}, obj : {}, objtype:: {}, name : {}'.format(self, obj, objtype,
                                                                                           self.name)

    def __set__(self, obj, name):
        print('Set method called')
        if isinstance(name, str):  # 정교하게 validation을 체크가능
            self.name = name
        else:
            raise TypeError("Name should be string")

    def __delete__(self, obj):
        print('Delete Method called')
        self.name = None


# 클래스 내부 필드가 여러개일 때, 코드 재상용성 증가 (by Descriptor 처리)
class Sample1(object):
    name = DescriptorEx1()  # 여기의 name을 handling 하기 위해선 상위에서 정의한 메소드를 호출하게 된다.


s1 = Sample1()
# __set__ 호출
s1.name = 'Descriptor Test1'

# 예외 발생
# s1.name = 10

# attr 확인
# __get__ 호출
print("EX 1 > ", s1.name)

#  __del__ 호출
del s1.name

# 삭제됐음을 확인
print('Ex 1 > ', s1.name)


# Ex 2
# property class 사용 descriptor 직접 구현
# class property(fget = None, fset=None, fdel=None, doc=None) 공식문서에 있는 내용

class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value

    def getVal(self):
        return 'Get method called  -> self : {}, name : {}'.format(self, self._name)

    def setVal(self, value):
        print('Set method called')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name should be String")

    def delVal(self):
        print('Delete method called')
        self._name = None

    name = property(getVal, setVal, delVal, 'Property 테스트를 하는 네임 필드, 의미는 없습니다.')


s2 = DescriptorEx2('Descriptor Test2')

# 최초 값 확인
print('Ex 2 > ', s2.name)

# setVal 호출
s2.name = 'Descriptor Test2 Method'

# 예외 발생
# s2.name = 10

# getVal 호출
print("Ex 2 > ", s2.name)

# delVal 호출
del s2.name


# 재확인
# getVal 호출
print("Ex 2 > ", s2.name)

# Doc 확인
print('Ex 2 > ', DescriptorEx2.name.__doc__)