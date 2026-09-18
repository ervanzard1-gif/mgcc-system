data=[4,2,5,3,3,2,7,9,6,0,8,7]

for i in data:
    print(f'angka= {i}')

data=['aaron','steve','aeron']

for i in data:
    print(f'nama={i}')

print('===============================')

data=[4,7,5,3,6,8,7,5,3,2,5,7,9,7,5,4]

panjang=len(data)

for i in range(panjang):
    print(f'angka={data[i]}')
print('===============================')
for i in range(panjang):
    print(f'angka={i}')

print('===============================')
data=[4,7,5,3,6,8,7,5,3,2,5,7,9,7,5,4]


panjang=len(data)

i=0

while i < panjang:
    print(f'angka={data[i]}')
    i+=1

data=['jsj',2,5,3,'ancf']

[print(i) for i in data]

[print('x=',i) for i in data]


data=['ervanza',11,'radithya',2007]

for index,hasil in enumerate(data):
    print('index=',index,'hasil=',hasil)



data=[4,7,3,2,7]

data=[i*2 for i in data]
print(data)

print('================================')

data=[3,7,4,7,9]
for i in data:
    print(f'angka={i}')

data=[3,5,5,3,7,9,6]

panjang=len(data)

for i in range(panjang):
    print('angka=',{data[i]})
print('\n')
for i in range(panjang):
    print('angka=',{i})

print('\n')
data=[3,6,9,6,5,3,7]

panjang=len(data)
i=0

while i <panjang:
    print(f'angka={data[i]}')
    i+=1

print('\n')

data=['suckle','your',67,95]
[print('hasil=',i)for i in data]

data=[4,7,9,6,4]
data=[i+1 for i in data]
print(data)


print('\n')
data=['fitb','fara',2008,5]
for index,data in enumerate(data):
    print('index=',index,'data=',data)


print('===============================')

data=[1,4,6,8,54,3,65]
for i in data:
    print(f'angka={i}')


data=['ayam','buaya','pilot']

panjang=len(data)
for i in range(panjang):
    print(f'hasil={data[i]}')


data=[2,6,3,1,7,0,7,4]
i=0
panjang=len(data)
while i<panjang:
    print(f'angka={data[i]}')
    i+=1


data=[3,7,4,3,3,5,2,5,98]
[print(f'angka={i}')for i in data]

data=['fara','hartini','fitb','jepang',5]

for index,hasil in enumerate(data):
    print(f'index={index}',f'hasil={hasil}')


print('=============================\n\n\n\n\n\n\n\n')

data=[2,4,7,4,3,7,9]
for i in data:
    print(i)


data=[4,6,83,5,8,5,3]
panjang=len(data)
for i in range(panjang):
    print(data[i])

data=[4,7,8,5,3,5,8]
panjang=len(data)
i=0
while i<panjang:
    print(data[i])
    i+=1


data=[4,5,8,6,4,3,54,6,8]
[print(i)for i in data]


data=['china','hungaria','romania']

for index,hasil in enumerate(data):
    print(index,hasil)

data=[2,6,89,5]
data=[i+1 for i in data]
print(data)