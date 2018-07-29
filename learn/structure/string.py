# -*- coding: utf-8 -*-

print('I\'m ok')
print("I'm ok")
print(r'\'\\\\n')

print('''
sasdasd\n234
sdfsdfsd,123123123'
123123"
''')


print(r'''asdasd\n12312''')
print("我是谁")
#获取字符的整数表示
print(ord('A'))
#把编码转换为字符
print(chr(ord('A')))

#编码转换为字节
enc='中文'.encode('utf-8')
print(enc)
#将字节转换为字符
dec=enc.decode('utf-8')
print(dec)

print('str()')
s='hello world'
print(str(s))
print(repr(s))
print(repr(1/2))
print(repr('hello 123 \t \n'))#转义

#字符串的format函数
print('a={},b={}'.format('name','age'))
print('0={0},1={1}'.format('0','1'))
print('0={1},1={0},2={other}'.format('0','1',other='address'))
print('name={name},age={age}'.format(name='wanglongfei',age='30'))