print('\n')
print('\x1b[34mselamat datang di program kalkulator sederhana \x1b[0m')

keperluan=input('apakah anda memerlukan 1 angka atau 2 angka? (1/2): ')
if keperluan=='1':
    data=input('float, int atau complex:')
    if data=='float':
        angka=float(input('masukkan angka : '))

    elif data=='int':
        angka=int(input('masukan angka: '))

    elif data=='complex':
        angka=complex(input('masukan angka: '))
        

elif keperluan=='2':
    data=input('float, int atau complex:')
    if data=='float':
        angka1=float(input('masukkan angka pertama : '))

    elif data=='int':
        angka1=int(input('masukan angka pertama : '))

    elif data=='complex':
        angka1=complex(input('masukan angka pertama: '))

    data=input('float, int atau complex:')
    if data=='float':
        angka2=float(input('masukkan angka kedua : '))

    elif data=='int':
        angka2=int(input('masukan angka kedua : '))

    elif data=='complex':
        angka2=complex(input('masukan angka kedua: '))


import math
import random
operator=input('masukkan operator yang ingin digunakan :')
match operator:
    case '+':
        hasil=angka1+angka2
        print('hasil dari',angka1,'+',angka2,'=',hasil)
    case '-':
        hasil=angka1-angka2
        print('hasil dari',angka1,'-',angka2,'=',hasil)

    case '*':
        hasil=angka1*angka2
        print('hasil dari',angka1,'*',angka2,'=',hasil)
    case '/':
        hasil=angka1/angka2
        print('hasil dari',angka1,'/',angka2,'=',hasil)
    case '^':
        hasil=angka1**angka2
        print('hasil dari',angka1,'^',angka2,'=',hasil)

    case 'pow':
        data=math.pow(angka1,angka2)
        print('hasil : ')

    case 'sqrt':
        hasil=math.sqrt(angka)
        print('hasil dari sqrt(',angka,')=',hasil)

    case 'log':#log.(angka, basis)
        basis=int(input('masukkan basis logaritma : '))
        hasil=math.log(angka,basis)
        print('hasil dari log(',angka,',',basis,')=',hasil)

    case 'sin':
        angkaradians=math.radians(angka)
        hasil=math.sin(angkaradians)
        print('hasil dari sin(',angka,')=',hasil)

    case 'cos':
        angkaradians=math.radians(angka)
        hasil=math.cos(angkaradians)
        print('hasil dari cos(',angka,')=',hasil)

    case 'tan':
        angkaradians=math.radians(angka)
        hasil=math.tan(angkaradians)
        print('hasil dari tan(',angka,')=',hasil)

    case 'hypot':
        hasil=math.hypot(angka1,angka2)
        print(hasil)

    case 'abs':
        print(abs(angka))

    case 'fabs':
        print(math.fabs(angka))

    case 'ceil':
        print(math.ceil(angka))

    case 'floor':
        print(math.floor(angka))

    case 'round':
        pembulatan=input('butuh angka koma belakangnya?')
        if pembulatan=='y':
            bulat=int(input('masukan berapa batas pembulatan='))
            print(round(angka,bulat))
        elif pembulatan=='n':
            print(round(angka))

    case 'modf':
        koma=input('untuk koma butuh pembulatan?')
        if koma=='y':
            bulat=int(input('masukan angka koma belakangnya'))
            y,x=math.modf(angka)
            print(round(y,bulat))
            print(x)

        if koma=='n':
            print(math.modf(angka))

    case 'derajat':
        print(math.degrees(angka))

    case 'radian':
        print(math.radians(angka))

 


        
