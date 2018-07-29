list=[]
c=0
while c<100:
    list.append(c)
    c+=1
print("list lendth=",len(list))

it=iter(list)
for x in it:
    print(x,end=',')

print('\n')
it=iter(list)
while True:
    try:
        print(next(it),end=',')
    except:
        print("\n迭代结束了")
        break