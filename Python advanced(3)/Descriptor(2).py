"""
Keyword - Descriptor vs Property, low level(descriptor) vs high level(property)

Descriptor
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. property 와 달리 reuse(재사용) 가능하다.
3. ORM 프레임워크 사용 가능

"""

# Ex 1
# Descriptor 예제 1
# 디스크립터 본연의 기능을 활용한다.
import os


class DirectoryFileCount:
    def __get__(self, instance, instancetype=None):
        print(os.listdir(instance.dirname))
        return len(os.listdir(instance.dirname))


# 이 클래스는 재사용이 가능하게 설계돼있다.


class DirectoryPath:
    # descriptor instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname  # 상위 클래스의 instance 로 넘어감 -> instance.dirname


# 현재 경로에 있는 파일의 갯수 가져오기
s = DirectoryPath('./')  # __init__(dirname)

# former directory
g = DirectoryPath('../')

# 헷갈릴 때 출력 용도
print('Ex 1 > ', dir(DirectoryPath))
print('Ex 1 > ', DirectoryPath.__dict__)
print('Ex 1 > ', dir(s))
print('Ex 1 > ', s.__dict__)

print(s.size)
print(g.size)

# Ex 2
# Descriptor (2)
import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)


# 이것을 공통 모듈로 빼서 관리 => for 재사
class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value

    def __set__(self, obj, value):
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value = value


class Student:
    # Descriptor instance
    score = LoggedScoreAccess()

    def __init__(self, name):
        # Regular instance attribute
        self.name = name


s1 = Student('Kim')
s2 = Student('Lim')

print('Ex 2 > ', s1.score)  # 로깅 클래스를 만들었기에 빨간색으로 출력된다.
s1.score += 20  # get, set에 접근했기에 로깅이 두번 찍힌다.
print('Ex 2 > ', s1.score)  # 이런식으로 설계를 하면 db 업데이트 칠 때마다 로깅이 출력된다.
print('Ex 2 > ', s2.score)
s2.score += 40
print('Ex 2 > ', s2.score)


# __dict__ 확인
print('Ex 2 > ', vars(s1))
print('Ex 2 > ', vars(s2))
print('Ex 2 > ', s1.__dict__)
print('Ex 2 > ', s2.__dict__)