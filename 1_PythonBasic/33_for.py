#1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#2. 다양한 for 문의 사용
a=[(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

#range(a,b) a부터 b미만까지 숫자를 데이터로 갖는 객체

#리스트 내포 사용하기

a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)

a=[1,2,3,4]
result=[num*3 for num in a]
print(result)

a=[1,2,3,4]
result=[num*3 for num in a if num%2==0]
# 리스트내포 사용하기
# [표현식 for 항목 in 반복가능객체 if 조건문]

# for문을 중첩해서 사용할 경우의 문법
"""
[표현식 for 항목1  in 반복가능객체1 if 조건문1
    for 항목2 in 반복가능객체 if 조건문2
    ...]
"""

result=[x*y for x in range(2,10)
            for y in range(1,10)]

print(result)
# 연습문제
result=[n for n in range(1,6) if n%2==1]
print(result)