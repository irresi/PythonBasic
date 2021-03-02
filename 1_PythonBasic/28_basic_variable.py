a=[1,2,3]
b=a
print (a is b) #둘이 가르키고 있는 객체가 동일 -> True

#다른 객체를 만들며 복사하는 방법
b=a[:]

from copy import copy
b= copy(a)

#변수를 만드는 여러 가지 방법

a,b=('python', 'life')

(a,b)='python', 'life'
[a,b]=['python', 'life']

a=b='python'
print(a is b) # True

a=3
b=5

a,b=b,a

a=(1,2,3,)
a=a+(4,)
print(a)

a=['Life', 'is', 'too', 'short']

a=[1,1,1,2,2,2,3,3,3]
a=set(a)
print(a)