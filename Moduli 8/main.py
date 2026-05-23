class student:
    def __init__(self,name,percentage):
        self.name = name
        self.percentage = percentage


    def show(self):
        print("Name is",self.name,"and the percentage is ",self.percentage)

studenti=student( "Ensar", 90)

studenti.show()

class MyClass:
    def __init__(self):
        self.pv =  "This is a public var"

my_class =MyClass()
print(my_class.pv)

class klasaime:
    def __init__(self):
        self._protected_var ="This is a protected vatiable"
    def _protectede_method(self):
        print("This is a protected variable")

klasa = klasaime()
print(klasa._protected_var)

class one_d:
    def __init__(self):
        self.__private_var ='this is a private var'

teacher=one_d()
print(teacher.__private_var)


