import os
import glob
from datetime import date

print('当前工作目录：',os.getcwd())



print(glob.glob('/Users/finup/logs/*.txt'))
print(date.today())

