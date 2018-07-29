tup=('q','g');
tup1=(1)
tup2=(1,)
tup3=tup+tup2
print(type(tup))
print(type(tup1))
print(type(tup2))
print(tup3)

for x in tup3:
    print(x,end=" ,")
