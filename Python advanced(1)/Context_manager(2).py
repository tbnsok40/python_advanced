"""
Context Manager
i/o, external connection이 일어나는 작업에서
리소스가 제때 반환되지 않으면 에러, exception 등이 발생할 수 있다.
이걸 방지하고자 자원회수를 엄격한 타이밍에 지키고자, with문 사용
자원 회수 할당 뿐만 아니라 우리가 원하는 로직을 삽입하여 사용하고자 context manager 사용.

keyword - contextlib, __enter__, __exit__

Contextlib - Measure execution(timer제작)
"""

# Ex 1
# Use Class

# 예외와 에러의 차이를 말해보시오
# 에러: 하드에 물리적인 장애가 발생했을 때,
# 예외: 프로그램적으로 발생, 프로그램 흐름에 영향을 받지 않게, 예외처리 등을 통해 우리가 컨트롤 할 수 있는 부분

import time
class ExecuteTimer(object): # object는 안적어도 되지만, 모든 클래스는 object를 상속받는 다는 것을 엄격히 알린다.
    def __init__(self, msg):
        self._msg = msg
    def __enter__(self):
        self._start = time.monotonic()
        return self._start
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Loggin exception {}".format((exc_type, exc_val, exc_tb)))
        else:
            print("{} : {} s".format(self._msg, time.monotonic() - self._start))
        return True # 엄격히 명시하기 위해(with를 잘 빠져나왔음을 알린다.)

with ExecuteTimer('start') as v:
    print("Received start Monotonic ! : {}".format(v))
    # Execute job -> with문에 들어온 순간부터 __enter__ 동작 --> self._start에 시작시간 할당(monotonic)

    for i in range(10000000):
        pass
    # 강제 예외 발생
    raise Exception('Raise exception !!') # exc_val에 해당




