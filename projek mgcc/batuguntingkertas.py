#permainan batu gunting kertas
import random

pilihan=['batu','gunting','kertas']

while True:
    pilihanbot=random.choice(pilihan)
    kodepilihansaya=int(input('masukan pilihan kode anda = '))
    pilihansaya=pilihan[kodepilihansaya-1]

    print('saya = ',pilihansaya)
    print('melawan')
    print('komputer = ',pilihanbot)

    if pilihansaya==pilihan[0] and pilihanbot==pilihan[1]:
        print('anda menang')
    elif pilihansaya==pilihan[1] and pilihanbot==pilihan[0]:
        print('anda kalah')
    elif pilihansaya==pilihan[2] and pilihanbot==pilihan[0]:
        print('anda menang')
    elif pilihansaya==pilihan[0] and pilihanbot==pilihan[2]:
        print('anda kalah')
    elif pilihansaya==pilihan[1] and pilihanbot==pilihan[2]:
        print('anda menang')
    elif pilihansaya==pilihan[2] and pilihanbot==pilihan[1]:
        print('anda kalah')
    elif pilihansaya==pilihan[2] and pilihanbot==pilihan[2] or  pilihansaya==pilihan[1] and pilihanbot==pilihan[1] or  pilihansaya==pilihan[0] and pilihanbot==pilihan[0] :
        print('draw')

    data=input('ingin main lagi? = ')
    if data=='y':
        continue
    elif data=='n':
        print('keluar dari permainan')
        break


