data='a','b','c'
print(data)

print(('hai',)*4)
print(('hai')*4)
print(['data']*4)

data=('ayam','kambing')
print(data)
del data

#print(data)#bakal error

data={
    'nama':'ervanza',
    'umur': 18,
    'agama':'islam',
    'kesukaan':'matematika'
}


print(data['kesukaan'])
del data['umur']
print(data)

data.clear()
print(data)

del data
#print(data)#bakal error

data={
    'nama':'ervanza',
    'umur': 18,
    'agama':'islam',
    'kesukaan':'matematika'
}
data0={
    'nama':'ervanza',
    'umur': 18,
    'agama':'islam',
    'kesukaan':'matematika'
}
data1={
    'nama':'caleey',
    'umur': 18,
    'agama':'kristen',
    'kesukaan':'kimia'
}

data2=data1==data
data3=data0==data
print(data2)
print(data3)

print(len(data))
print(type(data))
print(type(str(data)))
print(type(data['nama']))
print(type(data['umur']))
print(type(str(data['umur'])))

data={
    'nama':'ervanza',
    'umur': 18,
    'agama':'islam',
    'kesukaan':'matematika'
}
data['sekolah']='sma'
print(data)