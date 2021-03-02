dic = {'name':'pey', 'phone': '0110003323', 'birth': '1118'}
a = {1:'hi'}
a = { 'a': [1,2,3]}
a= {1:'a'}
a[2]='b'

a['name'] = 'pey'
a[3]=[1,2,3]
del a[1]

grade = {'pey':10, 'julliet':99}
grade['pey']
grade['julliet']

#a={[1,2] : 'hi'} #불가
#튜플은 key값으로 사용할 수 있다.

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.keys()) #list(a.keys())를 하면 dict_keys가 아닌 list를 얻을 수 있음

print(a.values())

print(a.items())

a.get('name')

a.get('nokey') #None

a.get('foo', 'bar') #뒤에 값을 디폴트값

print('name' in a) #키값을 검색 (True)
print('pey' in a)
a.clear()

