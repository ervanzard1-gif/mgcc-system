#operator dalam bentuk method

#merubah case dari string

#merubah semua ke upper case

data= 'guys!'
print('hasil='+data)

data=data.upper()
print('hasil=',data)

#lower
data='GUYS!!!!'
data=data.lower()
print('hasil='+data)

# pengecekan dengan is method

data='Data science'
apakah_lower=data.islower()
print(data,'adalah='+ str(apakah_lower))

data='EDINBURGH'
apakah_upper=data.isupper()
print(data,'adalah='+str(apakah_upper))

print('============================')

data='negeri para bedebah'
data=data.title()
print('hasilnya=',data)

data='Janji'
apakah_title=data.istitle()
print(data,'apakah title?=',apakah_title)


data='avengers1'
apakah_alpha=data.isalpha()
print(data,'apakah alpha?=',apakah_alpha)

data='ywatch8'
apakah_alnum=data.isalnum()
print(data,'apakah alnum?=',apakah_alnum)

data='67'
apakah_decimal=data.isdecimal()
print(data,'apakah decimal?=',apakah_decimal)

data='  \n'
apakah_space=data.isspace()
print(data,'apakah space?=',apakah_space)

#startswith dan endswith

cek_start='teknik informatika'.startswith("informatika")
print('start=',cek_start)

cek_end='mie ayam'.endswith('ayang')
print('end=',cek_end)

#combine component join() split()
pisah=['aku','benci','kamu']
gabung=','.join(pisah)
print(pisah)
print(gabung)

gabung=' '.join(pisah)
print(gabung)

gabung='akuosayangokamu'
print(gabung.split('o'))


#alokasi karakter rjust(), ljust(), center()

print(24*"=")

kanan='kamu'.rjust(10)
print("3"+kanan+"3")

kiri='hai'.ljust(20)
print("*"+kiri+"*")

tengah='fast'.center(20,"=")
print(" "+tengah+" ")


#kebalikan strip

tengah='======fast======='.strip("=")
print("0"+tengah+"0")

tengah='fast'
print(tengah)




#part2
data='evan'.upper()
print('hasil='+ data)

data='WaRwIcK'.lower()
print('hasil='+ data)

data='ACROSS SPIDER VERSE'.title()
print('hasil=',data)

data='diana67'.isalpha()
print('hasil=',data)

data='diana67'.isalnum()
print('hasil=',data)

data="95".isdecimal()
print('hasil=',data)

data='belly melly'.startswith("belly")
print('hasil=',data)

data='a mid anime'.endswith('mid')
print('hasil='+str(data))

data=['nadine','kei','inara']
data2=' '.join(data)

print(data2)

data= 'nadine kei inara'
print(data.split( ))


data=['syauqi','haidar','aqil']
data2=' '.join(data)
print(data2)

data= 'syauqi haidar aqil'
print(data.split( ))


data='windah'.center(20)
print('hasil='+str(data))

data="patrick".ljust(20)
print(data)

data="patrick".rjust(20)
print(data)


data='===bagas==='.strip('=')
print("*"+data+"*")

data='===bagas==='.strip('=')
print(data)

#part3

data='ayden victor haoken'
data2=data.upper()
print(data2)

data='jude victor william bellinGhaM'
data2=data.title()
print(data2)

data=data2
data22=data2.lower()
print(data22)

data='jericholiantono'
data2=data.isalpha()
print(data2)

data='erpan1945'
data2=data.isalnum()
print(data2)

data="784"
data2=data.isdecimal()
print(data2)

data='koci'
data2=data.rjust(29)
print('x='+data2)

data='33'
data2=data.ljust(21)
print('y='+data2)

data='biologi'
data2=data.center(30)
print('c=',data2)


data=['saya','sayang','kamu']
data2=' '.join(data)
print(data2)

data='saya orang ketiga'
data2=data.split()
print(data2)

data='   hai   '
data2=data.strip(" ")
print('x'+data2+'x')


data= 'tere liye'
data2=data.startswith("tere")
print(data2)

data= 'brian khrisna'
data2=data.endswith('krisna')
print(data2)



data= 'madagascar dan batu'
data2=data.capitalize()
print(data2)

data='BANGKAIIIII'
data2=data.casefold()
print(data2)

data= 'aKU cINTA kAMU'
data2=data.swapcase()
print(data2)

data= 'you\tare\tcrazy'
data2=data.expandtabs(6)
print(data2)

data='happy birthday'
data2=data.encode()
print(list(data2))

data=b'lomosonov'
data2=data.decode()
print(data2)

data=bytes([104, 97, 112, 112, 121, 32, 98, 105, 114, 116, 104, 100, 97, 121])
data2=data.decode()
print(str(data2))

data='hai'
data2=data.find('i')
print(data2)

data='hai'
data2=data.index('h')
print(data2)

data='Edinburg'
data2=data.encode()
print(list(data2))

data=bytes([69, 100, 105, 110, 98, 117, 114, 103])
data2=data.decode()
print(data2)

data='Warwick'
data2=data.find('i')
print(data2)

data= '===leeds==='
data2=data.strip('=')
print('x'+data2+'x')

data='imperial'
data2=data.capitalize()
print(data2)

data='tsinghua'
data2=data.islower()
print(data2)

data='aku \tdia'
data2=data.expandtabs(20)
print(data2)

data=243
data2=data,format(data,'08b')
print(data2)

data=['glory','glory','manchester','united']
data2=' '.join(data)
print(data2)

data= 'glory glory manchester united'
data2=data.split()
print(data2)
