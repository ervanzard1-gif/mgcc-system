#list

#kumpulan data
list_number=[1,2,3,4,5]
print(list_number)

list_str=['nadine', 'kei', 'inara']
print(list_str)

data=' '.join(list_str)
print(data)

list_bool=[False,True]
print(list_bool)

#bisa campuran
list_campur=[1,True,'lakaka']
print(list_campur)

list_angka=range(1,10)
data=list(list_angka)
print(data)

list_angka=range(1,10,2)
data=list(list_angka)
print(data)



#list pake for
data=[i*10 for i in range(1,10)]
print(data)

data=[i for i in range(1,10,2)]
print(data)

data=[i for i in range(1,7)if i!=5]
print(data)


data=[i*100 for i in range(1,10)if i%2==0]
print(data)


print('======================================')
for i in range(9):
    print(i)

for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)

data='evan'
for i in data:
    print(data)

data='evan'
for i in data:
    print(i)

data=['tepung','telur','gula']
for i in data:
    print(data)

data=('tepung','telur','gula')
for i in data:
    print('-'+i)

data='tepung''telur''gula'
for i in data:
    print(i)

data='tepung''telur''gula'
for i in data:
    print(data)

data='tepung','telur','gula'
for i in data:
    print(i)

data=['tepung','telur','garam']
data=' '.join(data)
print(data)

data='naerotika'
print(list(data))

data=data.encode()
print(list(data))

data_list=['evan',7,True]
print(data_list)
#tidak bisa dijoin karena hanya bisa str saja

data=range(1,10)
data=list(data)
print(data)

data=range(1,10,2)
data=list(data)
print(data)

data='Ervanza'
print('huruf ke-6=',data[6])

data=range(1,29,7)
data=list(data)
print(data)

data=(i for i in range(1,10))
print(list(data))

data=(i for i in range(1,10)if i!=3)
print(list(data))

print('\n')
data=(i*3 for i in range(1,10)if i!=2)
print(list(data))

data=range(1,10,2)
print(list(data))

data=['aku',2,True]
print(list(data))


print('================================')
data=['six'+'seven']
panjang=len(data)
data=['six','seven']
print(panjang)
for i in data:
    print(i)

data=['evan','radit','djani']
for i in data:
    print(data)

data='evan','radit','djani'
for i in data:
    print(i)

data='evan','radit','djani'
for i in data:
    print(data)

data='evan''radit''djani'
for i in data:
    print(data)

data='evan''radit''djani'
for i in data:
    print(i)

data='epan'
print(list(data))

x=data.encode()
print(list(x))

data=[101, 112, 97, 110]
print(bytes(data))

data=bytes([101, 112, 97, 110])
x=data.decode()
print(x)



data=(i for i in range(1,10) if i!=2)
print(list(data))

data=(i for i in range(2,14,3)if i!=5)
print(list(data))



data=range(1,10)
print(list(data))

print('================================')

data=[2,5,3,2,6,4,4,7,4]
print(data)
print(list(data))



data=['ayam','jago']
for i in data:
    print(i)

data=['ayam','jago']
for i in data:
    print(data)

data=['ayam''jago']
for i in data:
    print(data)

data='ayam''jago'
for i in data:
    print(data)

data='ayam''jago'
for i in data:
    print(i)


data='edinburgh'
x=data.encode()
print(list(x))


data=bytes([101, 100, 105, 110, 98, 117, 114, 103, 104])
x=data.decode()
print(x)

data=101, 100, 105, 110, 98, 117, 114, 103, 104
print(bytes(data))


data=(i for i in range(1,17))
print(list(data))

data=(i for i in range(1,17,2)if i!=3 and i!=5)
print(list(data))


print('===========================')

data=3,6,8,4,2
print(list(data))

data=['fara','hartini']
for i in data:
    print(i)
data='fara''hartini'
for i in data:
    print(i)

data='fara','hartini'
for i in data:
    print(i)


data='fara','hartini'
for i in data:
    print(list(i))

data='fara''hartini'
for i in data:
    print(list(i))


data='fara'
print(list(data))


data='fara'
x=data.encode()
print(list(x))

data=bytes([102, 97, 114, 97])
x=data.decode()
print(x)

data=102, 97, 114, 97
print(bytes(data))

data=[102, 97, 114, 97]
print(bytes(data))

data=range(2,9)
print(list(data))

data=[i for i in range(1,17,3)if i!=4]
print(data)