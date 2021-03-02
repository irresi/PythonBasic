print("Hello World")
print("%s 입니다" % "이순신")
print("%s원 입니다" % 5000)
print("이름은 %s 이고 %s에 삽니다" %("홍길동", "서울  "))

stock_price = 3900
print(stock_price)
stock_price = 4500
print(stock_price)
stock_price_type = type(stock_price)
print(stock_price_type)

#2-2. 문자열 자료형

"Hello World"
'Python is fun'
"""Life is too short, you need Python"""
'''Life is too short, you need python'''

food = "Python's favorite food is perl"
print(food)
multiline="""
Life is too short
You need python
"""
print(multiline)

#문자열 연산하기
head = 'Python'
tail = " is fun!"
print(head+tail)
a="python"
print(a * 2)
print("="*50)
print("My program")
print("="*50)

a="Life is too short"
print(len(a))
# 문자열 인덱싱과 슬라이싱
#...
a="Pithon"
#a[1]=y (X)
a=a[:1]+"y"+a[2:]

#문자열 포매팅
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("=" * 50)
#문자열 포맷 코드
print("I have %s apples" % 3)
print("rate is %s" % 3.234)

print("%10s" % "hi")
print("%-10sjane." % 'hi')
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

print("I eat {0} apples".format(3))

"I eat {0} apples".format("five")

number=3
"I eat {0} apples".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days".format(number, day)

'I ate {number} apples. so I was sick for {days} days.'.format(number=10, days=3)

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

"{0:<10}".format("hi")
"{0:>10}".format("hi")
"{0:^10}".format("hi")
"{0:=^10}".format("hi")
"{0:!^10}".format("hi")

y=3.42134234
print("{0:0.4f}".format(y))
"{0:10.4f}".format(y)

"{{ and }}".format()


# f 문자열 포매팅

name='홍길동'
age=30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
age=30
f'나는 내년이면 {age+1}살이 된다.'

d={'name':"홍길동", 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다'

f'{"hi":<10}'
f'{"hi":>10}'
f'{"hi":^10}'
f'{"hi":=^10}'
f'{"hi":!<10}'
y=3.42134234
f'' \
f'{y:0.4f}'
f'{y:10.4f}'

f'{{ and }}'

a="hobby"
a.count('b')
a="Python is the best choice"
a.find('b')
a.find('k')

a="Life is too short"
a.index('t')

#a.index('k') #오류가 난다.

",".join(['a','b','c','d'])
a="hi"
a.upper()

a="HI"
a.lower()

a=" hi "
a.rstrip()

a=" hi "
a.lstrip()

a=" hi "
a.strip()

a="Life is too short"
a.replace("Life", "Your leg") # 바뀐 문자열을 반환해 줄뿐 a를 바꾸는 것은 아니다.
print(a)
a="Life is too short"
a.split()

b="a:b:c:d"
b.split(':')
#########################




















