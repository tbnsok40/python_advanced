> ## 파이썬 객체 복사
- 객체의 복사 종류: copy, shallow copy, deep copy


> ### 일반 복사, copy
- 원본 객체의 참조값까지 복사하기 때문에, 복사된 객체의 원소가 달라지면 원본 객체도 달라진다.
- 특별한 메서드 사용이 아닌, 그저 객체할당으로 복사. 

``` python
# Ex 1 - Copy
# call by value, call by refference, call by share

a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print('Ex 1 > ', id(a_list))
print('Ex 1 > ', id(b_list))  # b_list 는 a_list 를 할당받기 때문에
# 같은 주소 참조임을 확인 가능
>>> Ex 1 >  4384525248
>>> Ex 1 >  4384525248


b_list[2] = 100
print('Ex 1 > ', id(a_list), a_list)  # b_list[2] 에 할당했는데, a_list 도 변경된다.
print('Ex 1 > ', id(b_list), b_list)
# 여전히 같다 => call by reference

>>> Ex 1 >  4384525248 [1, 2, 100, [4, 5, 6], [7, 8, 9]]
>>> Ex 1 >  4384525248 [1, 2, 100, [4, 5, 6], [7, 8, 9]]

```

<hr />

> ### 얕은 복사, shallow copy
- 일반 copy와 달리, copy 라이브러리 임포트 후에, copy.copy() 메서드로 복사한다.
- shallow copy는 원본 객체와 다른 참조값을 생성한다. (일반 copy는 원본 객체와 같은 참조값 생성)

```python 
# Ex 2 - Shallow Copy: 얕은 복사
import copy
c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)
print('Ex 2 > ', id(c_list)) # Ex 2 >  4384526976
print('Ex 2 > ', id(d_list)) # Ex 2 >  4384527424

# 참조형의 주소값을 공유하던 이전과는 달리, 지금은 주소값이 다르다.
# 이 방법은 어느 객체의 사본을 만듦으로, 본 객체를 건드리지 않고 사본을 만들 수 있다.

d_list[1] = 100
print('Ex 2 > ', (c_list))  # Ex 2 >  [1, 2, 3, [4, 5, 6], [7, 8, 9]]
print('Ex 2 > ', (d_list))  # Ex 2 >  [1, 100, 3, [4, 5, 6], [7, 8, 9]]
# d_list에만 100 들어감

d_list[3].append(1000)
d_list[4][1] = 10000
print('Ex 2 > ', (c_list))  # Ex 2 >  [1, 2, 3, [4, 5, 6, 1000], [7, 10000, 9]]

print('Ex 2 > ', (d_list))  # Ex 2 >  [1, 100, 3, [4, 5, 6, 1000], [7, 10000, 9]]

# 얕은 복사이기 때문에, 중첩된 객체에 대해서 원복 객체도 그대로 변경이 일어났다.(원본을 지키지 못함: 원본의 의미가 없다)
# 얕은 복사는 세부 객체까지 복사하지 못한다 : call by reference

```

> #### 정리
1) 얕은 복사 - copy.copy(객체) 에 대해 1차 배열(리스트)는 원본 객체를 변경시키지 않는 사본을 생성해낸다.
2) **문제:** 2차 이상의 배열, 중첩된 객체는 원본객체를 지키지 못한다. 즉 완벽한 객체 복사를 하지 못한다. 


<hr />


> ### 깊은 복사, deep copy
- shallow copy는 중첩 객체(ex 2차 이상의 리스트)의 영역까지 복사를 하지 못한다. (그래서 shallow copy)
- 깊은 복사는 이런 한계점을 넘어 중첩 객체에 대해서도 완벽히 복사할 수 있다.
- copy.deepcopy() 메소드 사용.


``` python

# Ex 3 - Deep Copy : 깊은 복사
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)  # 얕은 복사는 copy.copy() <--> 깊은 복사는 copy.deepcopy()

f_list[3].append(1000)
f_list[4][1] = 10000

print('Ex3 > ', id(e_list), e_list)  # Ex3 > 4309846592 [1, 2, 3, [4, 5, 6], [7, 8, 9]]
print('Ex3 > ', id(f_list), f_list) # Ex3 > 4308765632 [1, 2, 3, [4, 5, 6, 1000], [7, 10000, 9]]

# 우선 서로다른 주소값 참조
# f_list 와 e_list 는 다른 형태를 갖게 된다. 깊은 요소까지 복사했기 때문이다.
```

> #### 전체 정리
- 그렇다면 왜 늘 deepcopy를 사용하면 안될까? (shallow copy보다 만능처럼 보이는데)
- **우선 메모리 소요**. 
만약 1억개의 원소 지닌 리스트를 deepcopy 한다면 메모리 소요가 심해진다.
상황을 고려하여 shallow copy 할 것인지 deep copy 할 것인지 개발자가 결정한다.