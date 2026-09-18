import math
import random
x=input('memerlukan 2 angka?=')
if x=='y':
    angka1=float(input('masukan input angka1='))
    angka2=float(input('masukan input angka2='))
if x=='n':
    angka=float(input('masukan input angka='))
     
pilihan=input('masukan pilihan analisi=')

match pilihan:
    case 'absolute':print(abs(angka))
    case 'absolute2':print(math.fabs(angka))
    case 'pembulatan ke atas':print(math.ceil(angka))
    case 'pembulatan ke bawah':print(math.floor(angka))
    case 'pembulatan koma':
        batas=int(input('masukan input batas='))
        print(round(angka,batas))
    case 'logaritma':
        while True:
                loginput=input('masukan logx=')
                if loginput=='log2':print(math.log2(angka))
                elif loginput=='log10':print(math.log10(angka))
                break

    case 'pangkat':print(pow(angka1,angka2))
    case 'hypot':print(math.hypot(angka1,angka2))
    case 'uniform':print(random.uniform(angka1,angka2))
    case 'modf':
          bulat=input('butuh pembulatan?=')
          if bulat=='y':      
                batas1=int(input('masukan input batas='))   
                pecahan,bulat=(math.modf(angka))
                print(round(pecahan,batas1),bulat)

          elif bulat=='n':
                 pecahan,bulat=(math.modf(angka))
                 print(pecahan,bulat)
     
     