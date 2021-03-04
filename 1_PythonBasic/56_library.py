"""
sys 모듈
파이썬 인터프뢰터가 제공하는 변수와 함수를 직접 제어할 수 있게 해준다.
sys.argv 명령 행에서 인수 전달하기
sys.exit 강제로 스크립트 종료하기
sys.path 파이썬 모듈들이 저장되어 있는 위치로 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다

#pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다
#rb, wb ... 바이너리 파일 이진 파일로 파일을 열면 텍스트 파일처럼
# #인코딩 작업이나 줄바꿈 문자에 대한 변환이 없이 항상 1바이트 크기의 배열인 bytes 객체로 읽고 쓰기를 수행한다.
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data,f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
"""
"""
#os 환경변수나 디렉터리 파일 등의 OS자원을 제어할 수 있게 해준다.
import os
print(os.environ) # 내 시스템의 환경 변수값을 알고 싶을 때
os.chdir("C:\WINDOWS") # 현재 디렉터리 위치 변경하기
os.getcwd() #현재 디렉터리 확인
os.system("dir") #시스템 명령어 호출하기
f = os.popen("dir") # 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.
print(f.read())
os.mkdir(디렉터리) #디렉터리를 생성
os.rmdir(디렉터리) #빈 디렉터리를 삭제 
os.unlink(파일) #파일을 지운다.
os.rename(src, dst) # src라는 이름의 파일을 dst라는 이름으로 바꾼다.
"""
import shutil
shutil.copy("src.txt", "dst.txt") #src라는 이름의 파일을 dst로 복사한다. src-> dst

import glob
glob.glob("c:/doit/mark*")
#['c:/doit\\marks1.py', 'c:/doit\\marks2.py', 'c:/doit\\marks3.py'] 와 같이 메타 문자를 써서 원하는 파일 이름을 모두 읽어와 리스트로 반환한다.

import tempfile
filename = tempfile.mkstemp() # 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
print(filename)
f = tempfile.TemporaryFile() # 임시 공간으로 사용할 파일 객체를 돌려준다. 바이너리 쓰기 모드를 갖는다
f.close()

import time
time.time() #1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 돌려준다.
print(time.localtime(time.time()))
print(time.strftime('%d', time.localtime(time.time())))

import webbrowser
webbrowser.open("http://google.com")