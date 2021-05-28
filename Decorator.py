def trace(func):  # 호출할 함수를 매개변수로 받음 => 여기선 hello(), world() 에 해당
    def wrapper():
        print(func.__name__, '함수 시작')
        func()  # 매개변수로 받은 함수를 호출: hello(), world()
        print(func.__name__, '함수 끝')
    return wrapper  # wrapper 함수 반환 => closure : 함수 안에서 함수 만들고 반환하는 클로저 형태


@trace  # @데코레이터
def hello():
    print('hello')


@trace  # @데코레이터
def world():
    print('world')


hello()  # 함수를 그대로 호출
world()  # 함수를 그대로 호출
