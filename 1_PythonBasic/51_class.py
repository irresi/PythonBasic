# 클래스 : 과자 틀, 객체 : 과자
"""
class Cookie:
    pass
a=Cookie() # a객체는 Cookie의 인스턴스이다. a는 객체이다.
b=Cookie()

class FourCal:
    def setdata(self, first, second): #self는 a.setdata할 때의 a이다. 첫 번째 변수는 객체 자신이 전달된다. 주로 self라는 이름을 관례적으로 사용한다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a=FourCal()
b=FourCal() #a 와 b는 다른 객체이다. (주솟값도 다름)
a.setdata(4,2)
# 잘 사용하지는 않지만 FourCal.setdata(a,4,2)와 같은 방식으로도 호출 가능하다.
"""

"""생성자"""
#객체가 생성될 때 자동으로 생성되는 메서드

class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = Fourcal(4,2)

"""클래스의 상속"""
#어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
class MoreFourCal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.add())
print(a.pow())

"""메서드 오버라이딩"""
#부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 어버라이딩이라고 한다.
#이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
class SafeFourCal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a=SafeFourCal(4,0)
print(a.div())

"""클래스 변수"""
#객체 변수는 각각 객체마다 생성되는 변수, 클래스 변수는 여러 객체에서 접근하는 1개의 변수

class Family:
    lastname = "김"

a = Family()
b = Family()
print(a.lastname, b.lastname) # 값이 같다.
print(id(a.lastname), id(b.lastname)) # 주솟값이 같다. -> 클래스 변수는 공유된다.

































