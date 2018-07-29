import sys

emptySet=set();#空集合
emptyDict={};#空字典
print(type(emptySet))
print(type(emptyDict))

set1={1,1,2,3,4,4}
print(set1)
set2=set('112345')#返回-{'4', '5', '1', '2', '3'}
print(set2)
set3=set(('a','b','c'))
print(set3)
set3.add('d')
print(set3)
set3.update(['e','f'])
print(set3)
set3.update(('g','h'))
print(set3)
set3.update({'i':1,'j':2})
print(set3)
set3.remove('i')#移除元素，如果元素不存在，则发生异常
set3.remove('j')
try:
    set3.remove('m')
except :
    print("移除元素m发生异常：",sys.exc_info())
print(set3)
set3.discard('m')#移除元素，如果元素不存在，不会抛出异常
set1.pop()#随机删除一个元素
print(set1)
set1.clear()#清空集合
print(set1)
print(0 in set1)#判断元素是否在集合中