kalimat='dia anak ITB FITB seangkatan sama saya dan nama tiktoknya caleyy'
print(kalimat[1])
print(kalimat[0:3])
print(kalimat[:3])
print(kalimat[:3:2])

#import winsound
#winsound.Beep(1000,500)

print('peringatan \a')


print('aku  \bdan  \bkamu')
print('aku\tdan\tkamu')

print('halaman1\fhalaman2\fhalaman3')

print('halo\nkamu')

print('schumblenger\r.....p')

print('halo\skamu')

print('halo\vkamu')

print('halo\tkamu')


print('\x1b[31m kampang \x1b[0m')
#Daftar Kode Ringkas Tampilan Terminal:

#Gaya: 0 (Reset), 1 (Bold), 2 (Redup), 4 (Garis bawah), 7 (Invert warna).
#
#Warna Teks (Foreground): 30 (Hitam), 31 (Merah), 32 (Hijau), 33 (Kuning), 34 (Biru), 35 (Ungu), 36 (Sian), 37 (Putih).
#
#Warna Latar (Background): 40 (Hitam), 41 (Merah), 42 (Hijau), 43 (Kuning), 44 (Biru), 45 (Ungu), 46 (Sian), 47 (Putih).

print('\774')
print('\x76')

print('mbeekk\tkambing')
print(r'mbeekk\tkambing')
print(R'mbeekk\tkambing')


data=('ervanza radithya djani')
print(list(data))

data=('ervanza radithya djani')
data1=data.split()
print(data1)


data=(1,2,3,4,5)
print(list(data))

data=[1,2,3,4,5]
print(tuple(data))

data=['beautiful','caleey','fitb','i hope a something good to her','itb']
print(data[1])
print(data[-1])
print(data[1:])
print(data[:2])
print(data[::2])

ckck=['ervanza','caleey','fitb','itb']
print(ckck[1:3])
data[2]='caleeyy'
print(data)


print(max(data))
print(min(data))

data=['ayam','bebek','cacing']
data.append('doflaminggo')
print(data)

data1=data.count('ayam')
print(data1)

data2=('rusa','kucing')
data.extend(data2)
print(data)

data3=data.index('cacing')
print(data3)

data.insert(4,'zebra')
print(data)

data.pop()
print(data)

data.remove('cacing')
print(data)

data.reverse()
print(data)

data=[4,23,6,2]
data.sort()
print(data)

data=[4,23,6,2]
data.sort(reverse=True)
print(data)

data=['ayam','kambing','cing']
#data.sort()
#print(data)
#data.sort(reverse=True)
#print(data)
#data.sort(key=len)
#print(data)
data.sort(key=len,reverse=True)
print(data)
data[2]='dog'
print(data)


for i in [1,2,3]:
    print('cok')
data=('ervanza','caleey','fitb','itb')
print(list(data))

data=['ervanza','caleey','fitb','itb']
print(tuple(data))
data={'nama':'ervanza','umur':18,'agama':'islam'}
print(tuple(data))
print(list(data))