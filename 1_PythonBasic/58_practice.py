#Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value-=val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

#Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value = min(100, self.value+val)
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

#Q4
a = list(filter(lambda a: a>=0, [1,-2,3,-5,8,-3]))
print(a)

#Q5
a = hex(234)
print(int(a, 16))

#Q6
a =list(map(lambda a: a*3, [1,2,3,4]))
print(a)

#Q7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a)+min(a))

#Q8
a = round(17/3, 4)
print(a)

#Q9
import sys
from functools import reduce
arr = sys.argv[1:]
print(reduce(lambda a,b: a+b, arr,0)) # lambda 누적자, 현재값: 누적 연산 , iteratable object, initial value

#10
import os
os.chdir("C:\Windows")
f = os.popen("dir")
print(f.read())

#11
import glob

print(glob.glob("C:\\Users\\skybl\\PycharmProjects\\pythonProject\\week1\\*\\*.py"))

#12
import time
print(time.strftime("%Y/%m/%d %X", time.localtime(time.time())))

#13
import random
a = list(a for a in range(1,46))
random.shuffle(a)
print(a[0:6])















