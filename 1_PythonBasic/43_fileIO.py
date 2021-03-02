#파일 생성하기
f = open("새파일.txt",'w')
f.close()
#r : 읽기모드  w : 쓰기모드  a : 추가모드(파일의 마지막에 새로운 내용을 추가시킬 때 사용)

#파일을 쓰기 모드로 열어 출력값 적기

f = open("./새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
#readline() 함수 이용하기

f = open("새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
print('-'*30)

#readlines 함수 이용하기
f = open("새파일.txt",'r')
lines = f.readlines() #파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
for line in lines:
    print(line)
f.close()
print('-'*30)

# read 함수 이용하기
f = open("새파일.txt", 'r')
data = f.read() #파일의 전체 내용을 문자열로 돌려준다.
print(data)
f.close()

#파일에 새로운 내용 추가하기
f = open("새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#with문과 함께 사용하기

with open("새파일.txt", 'w') as f: #자원을 획득한다.
    f.write("Life is too short, you need python")#자원을 사용한다.
#자원을 반납한다. with 문은 자원(객체)을 해당 부분에서 사용할 때 쓰는 것

#sys모듈로 매개변수(argv) 받기
#명령프롬프트로  python sys1.py aaa bbb ccc 와 같은 방식으로 argv[0]~argv[2]로 매개변수를 전달한다.

import sys

args = sys.argv[1:]
for i in args:
    print(i)













