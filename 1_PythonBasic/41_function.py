#함수란? 공집합이 아닌 집합 X에 대하여 집합 X의 원소들이 집합 Y의 원소에 오직 하나씩 대응할 때의 이 대응
#함수를 사용하는 이유는 반복적으로 사용되는 부분을 간소화, 흐름을 쉽게 파악하기 위해

def add(a,b):
    return a+b

def add2(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(b=5,a=3)
add(3,5)

#입력값이 몇 개가 될지 모르는 경우

def add_many(*args):
    result=0
    for i in args:
        result=result+i
    return result
#*args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부모아서 튜플로 만들어준다.

def add_mul(choice, *args):
    if choice == "add":
        result=0
        for i in args:
            result=result+i
    elif choice == "mul":
        result=1
        for i in args:
            result= result*i
    return result

result = add_mul('mul',1,2,3,4,5)
print(result)

#key=value 형태로 args에 넣을 경우 딕셔너리 형태로 저장된다.
#**kwargs : 키워드 파라미터

#함수의 결괏값은 언제나 하나이다.
#return a,b와 같은 방법으로 반환할 경우 튜플로 반환된다.

#C에서의 void함수처럼 return울 단독으로 써서 즉시 함수를 나갈 수 있다.

#매개변수에 default값을 넣을 수 있다.
#default변수는 뒷 쪽에 사용해야 한다.

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27) # man에는 default값인 True가 들어간다.
say_myself("김선미", 28, False) #man에는 False가 들어간다.

#함수 안에서 함수 밖의 변수를 변경하는 방법
#1. return 사용하기
a=1
def vartest(a):
    a=a+1
    return a

a=vartest(a)
print(a)

#2. global 명령어 사용하기

a=1
def vartest():
    global a
    a=a+1

vartest()
print(a)

#lambda 간결한 함수

add =lambda a,b: a+b
result = add(3,4)
print(result)

