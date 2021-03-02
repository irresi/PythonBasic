"""
is_odd = lambda num: "홀수" if num%2==1 else "짝수"
print(is_odd(1))

"""

"""
#2'
arr = list(map(int,input().split()))
result=0
for num in arr:
    result=result+num
print(result/len(arr))
"""

"""
def avg(*args):
    sum=0
    for num in args:
        sum+=num
    return sum/len(args)
print(avg(1, 2, 3, 4))
"""

"""
f = open("test.txt",'a')
inp = input()
f.write(inp)
f.close()

"""

f= open("test.txt","r")
str = f.read()

f.close()
str = str.replace("java", "python")

f= open("test.txt","w")
f.write(str)
f.close()