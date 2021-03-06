"""
파이썬에서 정규 표현식을 지원하는 re모듈
"""
import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m) # 부합하므로 match객체를 돌려준다.
m = p.match("3 python")
print(m) #부합하지 않으면 None을 돌려준다.

m = p.search("python")
print(m)
m = p.search("3 python")
print(m) # search는 문자열 전체를 검색하기 때문에 3이후의 python에 매칭한 결과를 반환한다

result = p.findall("life is too short")
print(result) #['life', 'is', 'too', 'short']와 같이 리스트로 매칭되는 것을 반환

result = p.finditer("Life is too short")
print(result) #findall과 동일하지만 그 결과로 iteratable object를 돌려준다. 각각의 요소는 match객체이다

#match 객체의 메서드
m = p.search("3 python")
print(m.group()) # 매치된 문자열 리턴
print(m.start()) # 매치된 문자열의 시작 위치 반환
print(m.end()) # 매치된 문자열의 끝 위치를 돌려줌
print(m.span()) # 매치된 문자열의 (시작, 끝) 에 해당하는 튜플을 돌려준다.

# p = re.compile() m = p.match를 축약하여
# m=re.match로 수행할 수 있따

# 컴파일 옵션
#.는 \n을 제외한 모든 문자와 매칭되는 규칙이 있다.

# re.DOTALL 혹은 re.S: \n문자도 포함하여 매치
p=re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m) # match

#re.IGNORECASE 혹은 re.I : 대소문자 구별없이 매치를 수행할 때 사용하는 옵션

# re.MULTILINE 혹은 re.M :
# ^str 은 str이 처음으로 등장하는 것 검색
# str$은 str이 마지막으로 등장하는 것 검색
#다음 옵션은 모든 줄에 대해 이 옵션을 확인해 본다.

p = re.compile("^python\s\w+")

data ="""python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # ['python one']
#컴파일 옵션으로 re.MULTILINE 넣으면 one two three다 검색됨

#re.VERBOSE, re.X 옵션은 문자열에 사용된 whitespace제거 ,주석 사용 가능

#\ 백슬래시를 정규표현식에서 찾으려면 연속으로 두 개를 써서 표현한다 \\
# 만약 re.compile(r'\section') 과 같이 raw string임을 알려주면 그 뒤의 string이 \\section 과 같아진다