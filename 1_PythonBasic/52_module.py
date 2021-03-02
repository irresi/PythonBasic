#모듈명은 모듈 생성 규칙과 변수 생성 규칙을 모두 따라야 한다. 따라서 숫자로 시작할 수 없다.
"""
import mod1
print(mod1.add(3,4))
"""

from mod1 import add
print(add(3, 4))

#from mod1 import add,sub
#from mod1 import *

#클래스나 변수 등을 포함한 모듈
import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))

"""모듈을 벌러오는 또 다른 방법
1. sys.path.append 사용하기

import sys
sys.path : 파이썬 라이브러리가 설치되어 있는 디렉토리를 보여 준다.
만약 파이썬 모듈이 위 디렉토리에 들어있다면 모듈을 저장된 디렉토리로 이동하여 import할 필요가 없이 어느 곳에서나 import할 수 있다.

병령 프롴프트 창에서는 / 혹은 \든 상관없지만
**소스코드 안에서는  반드시 / 또는 \\기호를 사용해야 한다.

2. PYTHONPATH 환경 변수 이용하기
모듈파일의 기본 검색 경로를 보강하는 환경변수

set PYTHONPATH = 모듈이 있는 디렉터리(...../1_PythonBasic)



"""



