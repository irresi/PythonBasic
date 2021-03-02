"""
오류 예외 처리 기법
try, except 문
1. try, except만 쓰는 방법
try:
    ...
except:
    ...
오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.,

2. 발생 오류만 포함한 except문
try:
    ...
except 발생오류:
    ...

3. 발생 오류와 오류 메시지 변수까지 포함한 except문
try:
    4/0
except ZeroDivisionError as e:
    print(e)

"""
"""
try finally

try:
    #무언가를 수행한다.
finally:
    f.close()
    
try의 오류 여부와 상관없이 finally 안에 있는 문장은 수행된다.

"""

"""
여러 개의 오류
try:
     a = [1,2]
     print(a[3])
     4/0
except (ZeroDivisionError, IndexError) as e: # 2개 이상의 오류가 처리된다.
    print(e)
else:
    #오류가 없으면 수행된다.
"""

"""
오류 일부러 발생시키기(raise)

class Bird:
    def fly(self):
        raise NotImplementedError
"""

class MyError(Exception):
    def __str__(self): # 클래스 자체의 내용을 출력하고 싶을 때 형식을 지정하는 메서드
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)