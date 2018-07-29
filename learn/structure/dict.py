import sys

m={'name':"wanglongfei",'age':29}
print(type(m))
print("dict.items()=",m.items())
print("键的总数=",len(m))
print("将字典字符串化：",str(m))
print(m['name'])
print(m['age'])
print("get 方法",m.get('name'))
m['name']="lilei"
print(m)
del m['name'] #删除属性
print(m)
print("name in dict:",'name' in m)

m.clear() #清空字典
print(m)
del m #删除字典，
try:
    print(m)
except (NameError,):
    print("已将字典删除了，打印出错了……")

try:
    print(m['school'])
except :
    print('you are wrong,no school',sys.exc_info()[0])
   # raise #往上抛出异常
