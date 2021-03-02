#패키지는 도트를 사용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해준다.
# 모듈 이름이 A.B인 경우 A는 패키지 이름 B는 A 패키지의 B모듈이 된다.

import game.sound.echo # 파일 자체를 import
game.sound.echo.echo_test()

from game.sound import echo #패키지로부터 파일을 import
echo.echo_test()

from game.sound.echo import echo_test #파일에서 해당 함수만 import
echo_test() # 해당 디렉토리 혹은 파일을 import 해야 한다.

"""
    import game은 불가
"""



