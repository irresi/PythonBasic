odd=[1,3,5,7,9]

a=[1,2,3,['a','b','c']]
#a[-1][0]: 'a'

a[0:2] #[1,2]

a=[1,2,3]
b=[4,5,6]
a+b
a*3

len(a)
str(a[2])+"hi"

a = [1, 2, 3]
a[2]=4

del a[1]

a = [1, 2, 3, 4, 5]
del a[2:]

a=[1, 2, 3]
a.append(4)

a.append([5,6])

a=[1,4,3,2]
a.sort()
a.reverse()

a = [1, 2, 3]
a.index(3)
a.index(0) #오류

a.insert(0, 4) #0번째 위치에 4 삽입

a =[1, 2, 3, 1, 2, 3]
a.remove(3) #첫번째로 나오는 3 삭제

a=[1,2,3]
a.pop() # 마지막 원소 삭제
a=[1,2,3,1]
a.count(1) #1의 개수 출력

a=[1,2,3]
a.extend([4,5])
#혹은
a+=[4,5]


































