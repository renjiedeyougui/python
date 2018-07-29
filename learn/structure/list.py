cla=[123,'2',1233,[0,1,2]]
print(len(cla))
del cla[0]
for x in cla:
    print(x)

list=[]
i=0
while i<100:
    list.append(i)
    i+=1
print(list)