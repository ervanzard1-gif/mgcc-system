#baris dan deret
import math
apa_aja_yang_ada_di_soal=input('masukan tiap data=')
if "u1" in apa_aja_yang_ada_di_soal:
         u1=float(input('masukan suku ke 1='))
if "u2" in apa_aja_yang_ada_di_soal:
         u2=float(input('masukan suku ke 2='))
if "u3" in apa_aja_yang_ada_di_soal:
         u3=float(input('masukan suku ke 3='))
if "un" in apa_aja_yang_ada_di_soal:
         un=float(input('masukan suku ke n='))
if "N" in apa_aja_yang_ada_di_soal:
         n=int(input('masukan n='))
         
dataderet=input('masukan geometri/aritmetika jika ada')


if u2-u1==u3-u2:
    print('aritmetika')
    rumus=input('masukan nama operasi')
    match rumus:
        case 'suku ke-i':
            i=int(input('masukan i='))
            b=u2-u1
            print(u1+(i-1)*b)

        case 'suku tengah':
            t=n/2
            b=u2-u1
            print((u1+un)/2)

        case 'hitung semua':
            b=u2-u1
            print((n/2)*(u1+un))

        case 'mencari n':
              b=u2-u1
              n=((un-u1)/b)+1
              print(n)

elif dataderet=='aritmetika':
    print('aritmetika')
    rumus=input('masukan nama operasi')
    match rumus:
        case 'suku ke-i':
            i=int(input('masukan i='))
            b=u2-u1
            print(u1+(i-1)*b)

        case 'suku tengah':
            t=n/2
            b=u2-u1
            print((u1+un)/2)

        case 'hitung semua':
            b=u2-u1
            print((n/2)*(u1+un))

        case 'mencari n':
              b=u2-u1
              n=((un-u1)/b)+1
              print(n)

elif u2/u1==u3/u2:
    print('geometri')
    rumus=input('masukan nama operasi')
    match rumus:
        case 'suku ke-i':
            i=int(input('masukan i='))
            r=u2/u1
            print(u1*r**(i-1))

        case 'suku tengah':
            t=n/2
            r=u2/u1
            print(math.sqrt(u1*un))

        case 'hitung tengah':
            r=u2/u1
            if -1<r<1:
                print((u1(1-r*n))/1-r)

            else: print((u1(r*n-1))/r-1)

        case 'jumlah tak hingga':
            if u2/u1<1:
                r=u2/u1
                print(u1/(1-r))

            else: print('tidak bisa')

        case 'mencari n':
              r=u2/u1
              n=math.log(un*r/u1,r)
              print(n)

elif dataderet=='geometri':
    print('geometri')
    rumus=input('masukan nama operasi')
    match rumus:
        case 'suku ke-i':
            i=int(input('masukan i='))
            r=u2/u1
            print(u1*r**(i-1))

        case 'suku tengah':
            t=n/2
            r=u2/u1
            print(math.sqrt(u1*un))

        case 'hitung tengah':
            r=u2/u1
            if -1<r<1:
                print((u1(1-r*n))/1-r)

            else: print((u1(r*n-1))/r-1)

        case 'jumlah tak hingga':
            if u2/u1<1:
                r=u2/u1
                print(u1/(1-r))

            else: print('tidak bisa')
        case 'mencari n':
              r=u2/u1
              n=math.log(un*r/u1,r)
              print(n)

else: print('deret tidak jelas')
    
    



