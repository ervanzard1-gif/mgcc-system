data1=[1,2]
data=[3,4]
datag=[data1,data]
print(datag)

p1=['azka','oxford','enginering science']
p2=['ayden','harvard','applied math and economics']
p3=['kei','uc berkeley','data science and business administration']
p4=['ben','nus','computer science and math']
p5=['thomas','ntu','environmental enginering'] 
p6=['kemal','cuhk','computasional science']
p7=['ervanza','budapest of uni technology and economics','enviromental engginering']

data=[p1,p2, p3, p4, p5,p6,p7]
for peserta in data:
    print(f'nama=',peserta[0])
    print(f'univ=',peserta[1])
    print(f'major=',peserta[2],'\n')

databaru=data.copy()

print(databaru)

p1[0]='Adziman'

print(data)

print(databaru)

print('============================')

data0=[1,2]
data1=[3,4]

datax=[data0,data1,7]

data=datax[0][1]
print(data)

datacopy=datax.copy()
print(datacopy)
print(datax)

data1[0]=5
datax[2]=6
print(datacopy)
print(datax)


from copy import deepcopy

datadeep=deepcopy(datax)
print(datadeep)
print(datax)

data0[0]=3
datax[2]=30
print(datadeep)
print(datax)
print(datacopy)


print('============================')


data0=[1,2]
data1=[3,4]
datag=[data0,data1,9]
print(datag)


data=datag[1][1]
print(data)

data=datag.copy()

print(data)
print(datag)

data0[0]=5
print(data)
print(datag)

datag[2]=11
print(data)
print(datag)

print(f'addres data=',hex(id(data)))
print(f'addres datag=',hex(id(datag)))

print(f'addres data=',hex(id(data[0][0])))
print(f'addres datag=',hex(id(datag[0][0])))

from copy import deepcopy
datadeep=deepcopy(datag)

print(datag)
print(datadeep)
print(f'address datag=',hex(id(datag[0][0])))
print(f'address datag=',hex(id(datadeep[0][0])))
datag[0][0]=17
datag[2]=187

print(datag)
print(datadeep)

print(f'address datag=',hex(id(datag)))
print(f'address datag=',hex(id(datadeep)))

print(f'address datag=',hex(id(datag[0][0])))
print(f'address datag=',hex(id(datadeep[0][0])))
