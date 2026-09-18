#import datetime 
#
#hari_ini=datetime.date.today()
#print(hari_ini)
#print(f'hari ini adalah hari= {hari_ini:%A}')
#
#import datetime as dt
#
#hari_ini2=dt.date(2007,11,11)
#print(hari_ini)
#data=f'hari itu adalah hari= {hari_ini2:%A}'
#print(data)
#
#
#print('silahkan masukkan tanggal,\nbulan,\ntahun')
#tanggal=int(input('tanggal \t:'))
#bulan=int(input('bulan \t\t:'))
#tahun=int(input('tahun \t\t:'))
#
#tanggal_lahir=dt.date(tahun,bulan,tanggal)
#print(f'hari itu adalah hari= {tanggal_lahir:%A}')
#
#print(f'hari ini adalah hari= {hari_ini:%A}')
#
#umur_hari=hari_ini-tanggal_lahir
#umur_tahun=umur_hari.days//365
#umur_bulan_sisa=(umur_hari.days%365)//30
#print(f'umur= {umur_tahun}, {umur_bulan_sisa}')
#
##part2
#
#import datetime as dt
#data=dt.date.today()
#print(f'hari ini adalah hari= {data:%A}')
#
#data1='masukan tanggal, bulan, tahun'
#tanggal = int(input('tanggal :'))
#bulan = int(input('bulan :'))
#tahun= int(input('tahun :'))
#
#tanggal_lahir=dt.date(tahun,bulan,tanggal)
#print(tanggal_lahir)
#
#umur_hari=data - tanggal_lahir
#umur_tahun=umur_hari.days//365
#umur_sisa_bulan=(umur_hari.days%365)//30
#
#print(umur_tahun,umur_sisa_bulan)
#
#
##part3
#import datetime as dt
#
#hari_ini=dt.date.today()
#print(hari_ini)
#
#print('masukan data tanggal,bulan,tahun')
#tanggal=int(input('tanggal :'))
#bulan=int(input('bulan :'))
#tahun=int(input('tahun :'))
#
#tanggal_tertentu=dt.date(tahun,bulan,tanggal)
#print(tanggal_tertentu)
#
#umur_hari=hari_ini-tanggal_tertentu
#
#umur_tahun=umur_hari.days//365
#umur_sisa_bulan=(umur_hari.days%365)//30
#
#data= umur_tahun, umur_sisa_bulan
#print(data)
#
#hari=f'hari= {tanggal_tertentu:%A}'
#print(hari)


import datetime as dt

data=dt.date.today()
print(data)

print(f'{data:%A}')

tanggal=int(input('masukan tanggal tertentu='))
bulan=int(input('masukan bulan tertentu='))
tahun=int(input('masukan tahun tertentu='))

data1=dt.date(tahun,bulan,tanggal)
print(data)

umur= data-data1
print(umur)
umurtahun=umur.days//365
print(umurtahun)
sisabulan=(umur.days%365)//30
print(sisabulan)