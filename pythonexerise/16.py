#1.menyambung string
nama_awal = 'Ervanza'
nama_tengah= 'Radithya'
nama_akhir= 'Djani'
nama_lengkap=nama_awal+" "+nama_tengah+" "+nama_akhir
print(nama_lengkap)

#2.menghitung panjang string
panjang=len(nama_lengkap)
print(panjang)
print('panjang dari nama_lengkap adalah = ', panjang)
print('panjang dari' + nama_lengkap + '='+ str(panjang))


#3.operator untuk string

d="e"
status=d in nama_lengkap
print('apakah e ada di'+nama_lengkap+ '='+ str(status))

d="e"
status=d not in nama_lengkap
print('apakah e tidak ada di'+nama_lengkap+ '='+ str(status))



print('ha'*10)
print(15*'ha')



print('index ke-0'+ nama_lengkap[0])
print('index ke-7'+ nama_lengkap[7])
print('index ke-(-1)'+nama_lengkap[-1])
print('index ke-(0:4)'+ nama_lengkap[0:5])
print('index ke-[0,2,4,6,8]'+nama_lengkap[0:9:2])

#item paling kecil
print('paling kecil='+min(nama_lengkap))
print('paling besar='+max(nama_lengkap))

ascii_code=ord(" ")
print('ascii code untuk spasi'+str(ascii_code))

data=67
print('char untuk ascii 67 adalah=' + chr(data))


#operator dalam bentuk method
data= "raiddzar putra tian"
jumlah= data.count('a')

print('jumlah a pada data='+ str(jumlah))



print("=========================")
print('=========================')

nama_awal='Dafina'
nama_tengah='Ayu'
nama_akhir='Maheswari'
nama_lengkap=(nama_awal+' '+nama_tengah+' '+nama_akhir)
print(nama_lengkap)

panjang=len(nama_lengkap)
print('panjang dari nama'+ nama_lengkap+'='+str(panjang))

x= "d"
data= x in nama_lengkap
print('apakah d ada di'+ nama_lengkap+'='+ str(data))

x='A'
data= x not in nama_lengkap
print('apakah A ada di'+nama_lengkap+'='+str(data))

print('index ke-1='+nama_lengkap[1])
print('index ke-7='+nama_lengkap[7])
print('index ke-2,4='+nama_lengkap[0:5:2])
print('index ke-(0:3)='+nama_lengkap[0:4])

print('data paling kecil=',min(nama_lengkap))
print('data paling beasr=',max(nama_lengkap))
print('data paling besar= '+ max(nama_lengkap))

data_ascii=ord('t')
print('hurut t memiliki nilai='+ str(data_ascii))

data=110
print('nilai 110 merupakan karakter ='+ chr(data))


nama='nadine kei inara'
data=nama.count('a')
print(data)

data=len(nama)
print(data)

print('huruf ke-2=',nama[2])
print('huruf ke-0=',nama[0])
print('huruf ke-1 dan 2=',nama[1:3])
print('huruf ke-2,4,6,8=',nama[2:9:2])

data=ord('m')
print('merupakan susunan ke=' ,data)

data=90
print('karakter=',data)

print('huruf minimal=',min(nama_lengkap))
data=max(nama_lengkap)
print('huruf max=',data)


#part kesekian
nama_awal='nadine'
nama_tengah='kei'
nama_akhir='inara'

nama_lengkap=nama_awal+' '+nama_tengah+' '+nama_akhir
print(nama_lengkap)

panjang_nama=len(nama_lengkap)
print(panjang_nama)

print('huruf ke-3=',nama_lengkap[3])
print('huruf ke-0',nama_lengkap[0])
print('huruf ke-1 sampai 4=',nama_lengkap[1:5])
print('huruf ke-(2,4,6,8)',nama_lengkap[2:9:2])

print('=============\n\n\n\n\n\n\n\n\n')
nama1='imperial'
nama2='college'
nama3='london'

namax=nama1+' '+nama2+' '+nama3
print(namax)

panjang_nama=len(namax)
print(panjang_nama)

data=max(namax)
print(data)

data=min(namax)
print(data)

data= 'f' in namax
print(data)

data='e' in namax
print(data)


print(f'huruf ke-0',namax[0])
print(f'huruf ke-2,4,6',namax[2:7:2])

kode=110
print(chr(kode))

kode=ord('y')
print((kode))