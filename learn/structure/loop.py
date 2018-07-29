count=0
sum=0
while count<=100:
    sum+=count
    count+=1
else :
    print("超过100啦")
print('0到100的和=',sum)

c=0
while True:
    c+=1
    if c==100:
        break
    if c<20 and c>10:
        continue
    print(c,end=',')
else:
    print("有break语句，else不会执行")

print("\nfor loop……")
list=[1,2,3,4,5]
for x in list:
    print(x,end=',')


for x in range(100):
    print(x,end=',')
print('\n')

for x in range(2,9,1):
    print(x,end=',')
print('\n')

for x in range(len(list)):
    print(x,list[x])