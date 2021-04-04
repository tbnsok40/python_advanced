"""
객체의 복사 종류: Copy, shallow copy, deep copy

파이썬에선 모든 걸 객체라 부른다 str, int, float, etc

python 의 가변형: list, set, dict
불변형: 위 3가지 제외 나머지

정확한 이해 후 사용 -> 프로그래밍 개발 중요(문제 발생 요소)

immutable: int, str, float, bool, unicode ...
"""

# Ex 1 - Copy
# call by value, call by refference, call by share

a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print('Ex 1 > ', id(a_list))
print('Ex 1 > ', id(b_list))  # b_list 는 a_list 를 할당받기 때문에
# 같은 주소 참조임을 확인 가능

b_list[2] = 100
print('Ex 1 > ', id(a_list), a_list)  # b_list[2] 에 할당했는데, a_list 도 변경된다.
print('Ex 1 > ', id(b_list), b_list)
# 여전히 같다 => call by reference

b_list[3][2] = 100
print('Ex 1 > ', id(a_list), a_list)
print('Ex 1 > ', id(b_list), b_list)
# 마찬가지로 여전히 같다.
print(' ')

# Ex 2 - Shallow Copy: 얕은 복사
import copy
c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)
print('Ex 2 > ', id(c_list))
print('Ex 2 > ', id(d_list))  # copy 를 해버린다 => 본 객체를 건드리지 않고
# 참조형의 주소값을 공유하던 이전과는 달리, 지금은 주소값이 다르다.
# 이 방법은 어느 객체의 사본을 만듦으로, 본 객체를 건드리지 않고 사본을 만들 수 있다.

d_list[1] = 100
print('Ex 2 > ', (c_list))
print('Ex 2 > ', (d_list)) # d_list에만 100 들어감
print(' ')
d_list[3].append(1000)
d_list[4][1] = 10000
print('Ex 2 > ', (c_list))
print('Ex 2 > ', (d_list))
# 얕은 복사이기 때문에, 중첩된 객체(내부 객체)에 대해서 원복 객체도 그대로 변경이 일어났다.(원본을 지키지 못함: 원본의 의미가 없다 => 얕은 복사는 그럼 왜 하는 거임?)
# 얕은 복사는 세부 객체까지 복사하지 못한다 : call by reference
print(' ')

# Ex 3 - Deep Copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

f_list[3].append(1000)
f_list[4][1] = 10000

print('Ex 3 > ', id(e_list), e_list)
print('Ex 3 > ', id(f_list), f_list) # 우선 서로다른 주소값 참조
# f_list 와 e_list 는 다른 형태를 갖게 된다. 깊은 요소까지 복사했기 때문이다.

# 왜 늘 deepcopy를 사용하면 안될까 만능처럼 보이는데.
# => 우선 메모리 소요. 만약 1억개의 원소 지닌 리스트를 deepcopy 한다면 메모리 소요가 심할 것
# 상황 고려하여 shallow copy할 것인지 deep copy할 것인지 결정해야한다.

