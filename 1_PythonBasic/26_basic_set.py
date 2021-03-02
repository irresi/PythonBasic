s1=set([1,2,3]) #{1,2,3}
s2=set("Hello") # {'e','H','l','o'}

#set의 특징
#중복을 허용하지 않는다
#순서가 없다 -> 인덱싱 불가t6

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

l1=list(s1)
t1=tuple(s1)

s1 & s2 #교집합
s1.intersection(s2) #교집합

s1 | s2 #합집합
s1.union(s2) #합집합

s1-s2 #차집합
s1.difference(s2) #s1-s2

s1=set([1,2,3])
s1.add(4) #값 1개 추가하기

s1.update([4,5,6]) # 값 여러 개 추가하기

s1.remove(2) #특정값 제거하기
