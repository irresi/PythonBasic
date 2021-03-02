def add(a,b):
    return a + b
def sub(a,b):
    return a - b
"""
print(add(1,4))
print(sub(4,2))
이렇게 사용할 경우 모듈을 import하는 파일에서 이 문장들이 실행된다.
"""

"""
대화형 인터프리터나 다른 파일에서 모듈을 불러서 사용 할 때는 수행 X
python mod1.py처럼 직접 이 파일을 불러서 실행할 때는 수행 O
"""
if __name__ == "__main__": #실행되고 있는 파일의 __name__변수에는 __main__이 저장된다. mod1이 실행될 때는 다른 파일의 __name__에 mod1이 저장된다.
    print(add(1,4))
    print(sub(4,2))
