def say(content):
    print(content)

say("hello")
say("world")


def area(width,height):
    return width*height

area1 = area(2, 5)
print("面积=",area1)


"""
关键词函数
"""
def f1(width,height):
    print("width=",width,'height=',height)
    return

f1(10,20)
f1(width=10,height=30)
f1(height=5,width=2)

'''
    默认参数
'''
def f2(name,age=10):
    print('name=',name,'age=',age)
    return

f2('hello')
f2('lilei',30)


'''
不定长参数，以元组的形式传入
'''
def f3(args,*vartuple):
    print(args)
    print(vartuple)

f3(1)
f3(1,2,3,2,'a')

'''
不定长阐述，以字典的形式传入
'''
def f4(args,**varDict):
    print(args)
    print(varDict)

f4(1)
f4(1,a=1,b=2,c=3)

'''
lambda表达式
'''
lam=lambda width,height:width*height
print(lam(10,2))

print('########## 变量作用域########')
glo=1;#全局变量
glo1=2
def g():
    glo=2;#局部变量
    print('内部 glo=',glo) #打印局部变量，输出2

    global glo1
    glo1=123
    print('内部glo1=',glo1)
g()
print('glo=',glo) #打印全局变量，输出1
print('glo1',glo1)