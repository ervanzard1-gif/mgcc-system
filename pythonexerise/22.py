#ELIF= else if
nama=input('masukan nama=')
if nama=='evan':print('oke masuk')
elif nama=='raijar':print('oke masuk')
else:print('jgn masuk')

a=2
b=2
angka=input('a...b=4,masukan tanda perhitungan yang tepat')
if angka=='+':print('benar')
elif angka=='x':print('benar')
else:print('salah')



try:
    angka=int(input('masukan angka=')) 
    if angka%2==0:print('genap')
    else:print('ganjil')
except:print('masukin angka kocak bukan yang lain')
