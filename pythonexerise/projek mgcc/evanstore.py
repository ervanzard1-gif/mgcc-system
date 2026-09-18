print('selamat datang di evan store')

produk={
    'a':['buku tulis',12000],
    'b':['pensil',3000],
    'c':['pulpen',6000],
    'd':['penghapus',3500],
    'e':['penggaris',10000],
    'f':['tip-x',8500],
    'g':['rautan',6500]
}

databelanja=[]
while True:
    kodeproduk=input('masukan kode barang = ')
    prosesdata=produk.get(kodeproduk)
    if prosesdata==None:
        print('data salah')

    elif prosesdata!=None:
        databelanja.append(prosesdata)
        print(databelanja)

    lanjutan=input('lanjutkan belanja? = ')
    if lanjutan=='y':
        continue
    elif lanjutan=='n':
        break
print(f'{'no':<5}',f'{'barang':<20}',f'{'harga':<10}')
for index,i in enumerate(databelanja):
    print(f'{index+1:<5}',f'{i[0]:<20}',f'{i[1]:<10}')

hargatotal=(sum(i[1] for i in databelanja))
print(hargatotal)

total=0
for i in databelanja:
    total +=i[1]
print(total)

harga=[]
for i in databelanja:
    harga.append(i[1])
print(sum(harga))
    


