a=['ari','rehan','febri']
print(f'a={a}')

b=a
print(f'b={b}')

a[1]='raijar'
print('b=',b)
print('a=',a)

print(f'addres=',(hex(id(a))))
print(f'addres=',(hex(id(b))))

b.remove('ari')
print(a)

print('\n\n\n\n\n\n\n\n\n\n\n')

c=a.copy()
print(a)
print(c)

c.insert(1,'ijar')
print(c)
print(a)

print(f'addres=',(hex(id(a))))
print(f'addres=',(hex(id(b))))
print(f'addres=',(hex(id(c))))


print('\n\n\n\n')

data_baru=['aca','repan']
a.extend(data_baru)
print(a)

x=sorted(a)
print(x)

a.reverse()
print(a)

x=b.pop()
print(b)
print(x)

data=[4,7,3,6,3,2,5,7,4,3,6,8,5]

jumlah=data.count(2)
print(jumlah)


data.sort()
print(data)


data=[4,7,3,6,3,2,5,7,4,3,6,8,5]

jumlah=data.pop()
print(jumlah)


data.sort()
print(data)



print('==========================')
data=['snore','shiver','snezee','suckle','slap']

datax=data.index('snore')
print(datax)

datak1=data[1]
print(datak1)

data.insert(2,'sweep')
print(data)
x=data.pop(2)
print(data)

print(x)
#data.remove('sweep')
#print(data)


databaru=['reconcile','reprimand','reminisce']
data.extend(databaru)
print(data)

data.append('groan')
print(data)

print('================================')
angka=[4,6,3,2,2,4,6,6,8,54,2,156,8,90,65,3,4]
#angka.sort()
#print(angka)

x=sorted(angka)
print(x)

angka.pop(7)
print(angka)