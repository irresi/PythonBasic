all(x) #반복가능한 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 있으면 False를 돌려준다.
any(x) #반복가능한 자료형 x를 입력 인수로 받으며 이 x의요소 중 하나라도 참이 있으면 True 모두 거짓일 때만 False
chr(i) #i: num -> char
dir([1,2,3]) #객체가 자체적으로 가지고 있는 변수나 함수
divmod(7,3) # (몫, 나머지)를 튜플로 돌려주는 함수

for i, name in enumerate(['body', 'foo', 'bar'])
    print(i,name)
#(인덱스, 요소)로 반환
eval('1+2') #실행가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수

def positive(x):
    return x>0

print(list(filter(lambda x: x>0, [1,-3,2,0,-5,6])))
#filter값이 True인 것만 골라서 반환해준다.

hex(234) #정수 값-> 16진수

a=3
id(3)
id(a) #같은 주소를 참조한다. 3은 int 타입의 객체이다.

input() #문자열 입력함수

int() #문자열 형태의 숫자 혹은 실수-> 정수

class Person: pass
a = Person()
isinstance(a, Person)
#isinstace(인스턴스, 객체) 앞의 인스턴스가 클래스의 인스턴스인지 판단함

len("python")
len([1,2,3]) #입력값의 길이 혹은 요소의 전체 개수를 반환

list("python") #['p', 'y','t', 'h', 'o', 'n']
#반복가능한 자료형 s를 받아 리스트로 만들어 돌려주는 함수

#map(f, iterable) # f와 iterable한 자료형을 입력받아 요소 각각에 f를 적용하여 수행한 결과를 반환한다.
#max(iterable)
#min(iterable)
#oct
#open

ord('a') # 97
#ASCII -> number

pow(2,4) #x의 y제곱한 결괏값

#range(start, stop, step) #입력받은 숫자에 해당하는 값을 반복가능한 객체로 만들어서 반환
#round(x) x를 반올림해서 리턴
#sorted(iterable) 입력값을 정렬한 후 리턴해주는 함수
#str(object) 문자열 형태로 객체를 변환하여 반환
#sum(iterable) 입력받은 리스트나 튜플의 합을 반환
#tuple(iterable)
#type(object)
list(zip([1,2,3],[4,5,6])) #[(1,4),(2,5),(3,6)]
#동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수
