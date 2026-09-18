#konversi suhu celcius ke satuan lain

print('TEMPERATURE')

celcius=float(input('masukkan suhu dalam celcius : '))
print("suhu adalah",celcius,"celcius")

#reamur =4/5c
reamur=(4/5)*celcius
print('suhu dalam reamur adalah',reamur,'reamur')

#fahrenheit
fahrenheit=((9/5)*celcius)+32
print('suhu dalam fahrenheit adalah',fahrenheit,'fahrenheit')

#kelvin
kelvin=celcius+273
print('suhu dalam kelvin adalah',kelvin,'kelvin')

#fahrenheit to kelvin
fahrenheit=float(input('masukkan suhu dalam fahrenheit : '))
print('suhu adalah',fahrenheit,'fahrenheit')

kelvin= (5/9)*(fahrenheit-32)+273
print('suhu dalam kelvin adalah',kelvin,'kelvin')

#kelvin to fahrenheit
kelvin=float(input('masukkan suhu dalam kelvin : '))
print('suhu adalah', kelvin,'kelvin')

fahrenheit=(9/5)*(kelvin-273)+32
print('suhu dalam fahrenheit adalah',fahrenheit,'fahrenheit')



#pembelian game
cat_chess=float(input('masukan harga game cat chess= '))

stray_cat=(9/2)*cat_chess
print('harga stray cat= ',stray_cat,"ribu")

#float x int =float



#uang
rupiah=float(input('masukan jumlah rupiah='))

dolar=rupiah/16500
print('rupiah ke dolar='+str(dolar))
