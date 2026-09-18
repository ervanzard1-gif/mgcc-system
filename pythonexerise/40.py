data={
    'evan':'ervanza',
    'der':'dimas',
    'jan':'januar'
}

for i in data:
    print(i)

keys=data.keys()
print(keys)

for i in data.keys():
    print(i)

values=data.values()
print(values)

for i in data.values():
    print(i)

for i in data.items():
    print(i)

for i,j in data.items():
    print(i,j)

for key,value in data.items():
    print('key=',key,'value=',value)