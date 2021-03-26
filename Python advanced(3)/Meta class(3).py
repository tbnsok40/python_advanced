"""
Keyword - Type inheritance, Custom metaclass

metaclass 상속
1. type 클래스 상속 (metaclass를 상속한다는 뜻은 type class를 상속한다는 뜻)
2. metaclass 속성 사용
3. 커스텀 메타클래스 생성
 - class 생성의 hooking 가능 (intercept)
 - class 수정 (modify, 기능 추가)
"""


# Ex 1
# custom metaclass 생성 예제 (type 상속x)
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


# 남들이 사용하는 replace()메소드를 만든다고 생각해보자
def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new  #self는 list [1, 2, 3 .., 6] 자체가 된다.


# list를 상속받음, 메소드 2개 추가
CustomList1 = type('CustomList1',
                   (list,),  # list 클래스를 상속받는다 => CustomList1은 list의 모든 메소드를 사용할 수 있게된다.
                   {
                       'desc': '커스텀 리스트1',
                       'cus_mul': cus_mul,
                       'cus_replace': cus_replace
                   })
# CustomList1라는 클래스를 메타로 찍어놓은 것(위)(붕어빵 만드는 틀을 위에서 찍어놓은 것)
# (list)를 상속받았기에 가능한 일 => list 말고 다른 자료형을 사용하여 응용 가능


c1 = CustomList1([1, 2, 3, 4, 5, 6])  # 여기의 리스트가 곧 self가 된다.(초기화 값)
print('Ex 1 > ', c1)

c1.cus_mul(1000)
print('Ex 1 > ', c1)

c1.cus_replace(3000, 3)
print('Ex 1 > ', c1)
print('Ex 1 > ', c1.desc)
print('Ex 1 > ', dir(c1))


# 메소드를 클래스 내부보다 외부로 빼놓았을 때의 이점: 메소드를 컴포넌트식으로(조립식으로) 언제든지 끼우거나 빼서 사용할 수 있다.

# 메타클래스는 99%의 사용자는 전혀 고려할 필요가 없는 흑마법입니다.
# 당신이 이게 정말 필요할지에 의문을 갖는다면, 필요하지 않습니다.
# 이게 진짜로 필요한 사람은 그 필요를 알고 있으면서, 왜 필요한지에 대해 설명할 필요가 없는 사람들입니다.
# Tim Peris

# Ex 2
# 커스텀 메타클래스 생성 예제( type 상속 O )

# new -> init -> call (실행순서)
class CustomListMeta(type):
    # 생성된 인스턴스 초기화 <2>
    def __init__(self, object_or_name, bases, dict):
        print('__init__ -> ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)      # 부모한테 넘겨준다 3개의 인자를

    def __call__(self, *args, **kwargs):
        print('__call__ -> ', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)  # 부모한테 넘겨준다 3개의 인자를

    # 클래스 인스턴스 생성(메모리 초기화) <1>
    def __new__(metacls, name, bases, namespaces):
        print('__new__ -> ', metacls, name, bases, namespaces)
        namespaces['desc'] = 'customlist2'
        namespaces['cus_mul'] = cus_mul
        namespaces['cus_replace'] = cus_replace

        return type.__new__(metacls, name, bases, namespaces)
    # 25번줄의 내용이 내부에서 이런식으로 동작함을 보여준다. 즉 결과는 같다.


CustomList2 = CustomListMeta('CustomList2',
                             (list,),
                             {}
                             )

c2 = CustomList2([1,2,3,4,5])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)
print()
print('Ex 2 > ', c2)
print('Ex 2 > ', c2.desc)


# 상속 확인
print(CustomList2.__mro__)