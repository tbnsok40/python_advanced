"""
lambda 장점: 익명, 힙 영역 사용 즉시 소멸, pythonic, python garbage collection
일반함수: 재사용성 위해 메모리 저장
시퀀스형: 전처리에 reduce, map, filter 사용 (3형제)
"""

"""
익명 함수
"""
cul = lambda a, b, c: a * b + c
print('Ex 1 > ', cul(10, 15, 20))

# Ex 2
digits1 = [x * 10 for x in range(1, 11)]  # 10개의 원소 가진 리스트 생성
# 한번 사용하고 마는, 일회용의, 즉시 사용하는 : lambda
result = map(lambda i: i ** 2, digits1)
print(result)
# >>> <map object at 0x1098b9370> 형 변환 필요
# --> list() casting
result = list(map(lambda i: i ** 2, digits1))
# map()으로 함수(lambda)를 인자로 받아들인다
print("Ex 2 >", result)

"""
def ex2_func(x):
    return x**2
result = list(map(ex2_func, digits1))

일반함수는 재사용성 위해 메모리에 저장되기 때문에 garbage collector 에서 필터링이 되지 않는다. (대충 메모리 잡아먹는단 얘기)
그러므로 메모리 잡지 않는 람다(익명함수)를 사용한다.어차피 일회성 함수라면.

람다의 장점은 즉, 메모리 효율성도 있다.
"""

# Ex 3
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, digits))
print("Ex 3 >", result)
# 람다의 조건식이 들어가면 filter 친다.
"""
filter를 사용하면, for if 구문을 사용하지 않아도 된다.
"""

# Ex 4 : reduce
# sequence 형 데이터에서 원소를 누적할 때 사용 가능
from functools import reduce
digits3 = [x for x in range(1, 101)]
result = reduce(lambda x, y: x + y, digits3) # 누적 합계: 문자형에 대해서도 reduce 가능
print('Ex 4 > ', result) # 1~100 누적 합


