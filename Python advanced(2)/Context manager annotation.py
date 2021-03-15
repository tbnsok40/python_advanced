"""
annotation을 이용하여, 클래스형태가 아닌 함수형태로 사용해보자
Keyword - @Contextlib.contextmanager, __enter__, __exit__

가장 대표적인 with 구문 이해
Contextlib 데코레이터 사용
코드가 직곽적이며, 예외처리가 용이해진다.
"""

# Ex1
# Use decorator <-- 복잡한 클래스형태로 할 필요가 없어진다.
import contextlib
import time

@contextlib.contextmanager
def my_file_writer(file_name, method):
    # class 형과 달리, 바로 여기서부터 __enter__이다.
    f = open(file_name, method) # 여기서도 굳이 __init__할 필요없고,
    yield f # yield f가 __enter__에 해당된다.
    f.close() # __exit__

#실행해보자.
with my_file_writer('../testfile4.txt', 'w') as f: # __enter__에서 넘어온 f
    f.write('Context Manager Test4. \n Contextlib Test4')
# 어느 부분이 엔터인지, 어느부분이 exit인지 직관적으로 확인할 수 있다.

# Ex2
# Use decorator
@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try: # __enter__
        yield start
    except BaseException as e:
        print('Logging exception {}: {}'.format(msg, e))
        raise
    else: #__exit__
        print('{}: {}s'.format(msg, time.monotonic() - start))

with ExcuteTimerDc('Start job') as v:
    print('Received start monotonic2 : {}'.format(v))
    #execute job
    for i in range(10000000):
        pass
    raise ValueError('occured')


from itertools import count # 어떻게 쓰는거야?