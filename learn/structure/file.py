import pickle
file='/Users/finup/logs/file.log'
f=open(file,'w')
count=0
while count<100:
    f.write(str(count)+'\n')
    count+=1
f=open(file,'r')
#print(f.readline())#读取一行
#print(f.readlines())
#print(f.read())#读取全部内容

#迭代读取文件
for l in f:
    print(l,end='')
f.close()

'''
对象序列化
'''
dict={'name':'wanglongfei','age':'12','address':'beijing'}
list=[123,34,5,67]
dictFile=open('/Users/finup/logs/dict.txt','wb')
listFile=open('/Users/finup/logs/list.txt','wb')
pickle.dump(dict,dictFile)
pickle.dump(list,listFile)
dictFile.close()
listFile.close()
'''
对象反序列化
'''
dictFile=open('/Users/finup/logs/dict.txt','rb')
listFile=open('/Users/finup/logs/list.txt','rb')
dictObj=pickle.load(dictFile)
listObj=pickle.load(listFile)
print(dictObj)
print(type(dictObj))
print(listObj)
print(type(listObj))
