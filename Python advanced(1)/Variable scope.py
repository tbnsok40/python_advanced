# EX1
a = 10  # global variable


def foo():
    # read global variable
    print("Ex1 > ", a)


foo()
print('EX1 > ', a)
# a는 함수 안팍에서 모두 읽기 가능

# Ex2
b = 20


def bar():
    b = 30
    print('Ex2', b)


bar() # 30 return
print("Ex2", b)  # 20 return ,  global과 local 차이

# Ex3
c = 40


def foobar():
    # c = c + 10
    print("Ex 3> ", c)
    return


foobar()  # UnboundLocalError: local variable 'c' referenced before assignment

# Ex 4
d = 50


def barfoo():
    # global 선언을 자제하자, 코드 유지보수에서 좋지 않아. 아예 쓰지 말자는 말은 아니다.
    global d
    d = 5
    d += 10
    print("ex 4 > ", d)


print('ex 4 >> ', d)  # 50
barfoo()


# Ex5
def outer():
    e = 70  # 파이썬 클로져

    def inner():
        # e += 10 # 상위의 e를 그냥 가져다 쓰지 못한다.
        nonlocal e
        e += 10
        print('Ex 5 > ', e)

    return inner


in_test = outer()  # closure --> outer()함수 리턴하여 in_test변수에 저장 --> 곧 바로 inner()함수 호출
# 결과적으로 in_test에는 inner()함수 가 호출되어 할당된 상태
in_test()
in_test()
in_test()


# ex 6
def func(var):
    x = 10

    def printer():
        print('ex 6', 'printer func inner')

    print('func inner >>>', locals())  # locals()라는 함수안에, printer라는 함수와 var, x변수가 딕셔너리 형태로 저장돼있음을 볼 수 있다.


func('hi')

# ex 7
print('ex 7', globals())
globals()['test_variable'] = 100  # globals 딕셔너리에 'test_variable'이란 변수를 할당
print('ex 7', globals())

# ex 8 ( local -> global variable generate)
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k
print(globals())  # globals() dictionary 에 위의 이중 for 문으로 key-value 할당
# 재밌는 사실은 plus_5_5는 key 값 처럼 저장됐지만, globals()에 저장됐기에, plus_5_5만으로 value 를 리턴할 수 있다.
# print('Ex 8 > ', plus_5_5)  # unresolved reference 라고 뜨지만, 작동은 한다.

# 전역변수는 변하지 않는 고정 값에 사용 --> 함수형 프로그래밍에 자주 사용
# 지역변수 사용 이유: 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시
# 전역변수를 지역내에서 수정는 것은 권장 x
