class Person:
    living='上海'
    __sex='male'#私有变量
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def getSex(self):
        return self.__sex

class Male(Person):
    grade=''
    def __init__(self,name,age,address,grade):
        Person.__init__(self,name,age,address)
        self.grade=grade


person=Person('lili',23,'beijing')
print('Person:name={},age={},address={}'.format(person.name,person.age,person.address))
print(person.living)
print(person.getSex())

male=Male('zhangsan',25,'北京','三年级')
print('male:name={},age={},address={},grade={}'.format(male.name,male.age,male.address,male.grade))

