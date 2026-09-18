# continue,pass,break
#pass berfungsi sebagai dummy,tidak akan dieksekusi

data=4

while data<7:
    data+=1
    if data==5:
        pass
        print('toto')
    print(f'sekarang-->{data}')

print('kelar')



data=0

while data<5:
    data+=1
    print(f'angka sekarang-->{data}')
    if data==3:
        print('goks')
        continue

    print('evan')
print('done')

data=0

while data<5:
    data+=1
    if data==3:
        print('goks')
        continue

    print(f'angka sekarang-->{data}')
    print('evan')
print('done')


data=0

while data<5:
    print('evan')
    data+=1
    print(f'angka sekarang-->{data}')
    if data==3:
        print('goks')
        continue

print('done')