class MyError(Exception):
    def __init__(self,msg):
        self.msg=msg


try:
    raise MyError('you are wrong')
except MyError as e:
    print(e.msg)

try:
    f=open('/Users/finup/logs/dict.txt','r')
finally:
    print('文件是否关闭',f.closed)
    if not f.closed:
        print('close the file')
        f.close()

