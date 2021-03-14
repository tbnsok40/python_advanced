"""
Context Manager
Keyword - contextlib, __enter__, __exit__, exception

컨텍스트 매니저: 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환 하는 역할
가장 대표적인 with 구문 이해
"""

# Ex 1

file = open('../testfile1.txt', 'w') # w: write
try:
    file.write('Context Manager Test1\nContextlib Test1.') # 이런 내용을 텍스트 파일로 저장
finally:
    file.close() # 닫아준다. 자원할당받았기 때문에 다시 자원을 돌려준다 -> 메모리 낭비 방

# Ex 2
# with는 try, catch, finally 이후에 나
with open('../testfile2.txt', 'w') as f:
    f.write('Context Manager Test2\nContextlib Test2.')
# Ex1, 2는 동일한 기능 -> finally 기능까지 with는 이미 가지고 있다. -> 자동 리소스 반환(메모리 낭비 줄인다)

# Ex 3
# Use class -> Context Manager with Exception handling.

class MyFileWriter():
    # class에는 초기 함수가 있어야한다.
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name, method)
    def __enter__(self):
        print('MyFileWriter started: __enter__')
        return self.file_obj
    def __exit__(self, exc_type, exc_val, exc_tb):
        #tb : trace_back
        print("MyFileWriter started : __exit__")
        if exc_type: # exc_type: true/false의 불린 값 : error 존재 시 true
            print('Logging exception {}'.format((exc_type, exc_val, exc_tb)))
        self.file_obj.close() # file_obj: 오픈 함수 --> 에러가 안나면 close를 해준다.
        # close로 resource를 반환하면 무엇보다 안전하다.

with MyFileWriter('../testfile3.txt', 'w') as f:
    f.write('Context Manager Test3\nContextlib Test3.')





