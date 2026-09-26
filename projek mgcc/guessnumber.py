import random
angka_tebakan=random.randrange(1,50)
#print(angka_tebakan)
angkayangsudahdicoba=[]
while True:
    masukantebakan2=int(input('masukan tebakan anda = '))
    angkayangsudahdicoba.append(masukantebakan2)
    print('angka yang sudah dicoba = ',angkayangsudahdicoba)
    if masukantebakan2==angka_tebakan:
        print('benar',f'\x1b[32m {angka_tebakan}\x1b[0m')
        exit()

 
    while 0<masukantebakan2<=25 and 0<angka_tebakan<=25:
        print('salah tapi benar berada di 0<x<=25 ')
        masukantebakan3=int(input('masukan tebakan anda = '))
        angkayangsudahdicoba.append(masukantebakan3)
        print('angka yang sudah dicoba = ',angkayangsudahdicoba)
        if masukantebakan3==angka_tebakan:
            print('benar',f'\x1b[32m {angka_tebakan}\x1b[0m')
            exit()
        while 0<masukantebakan3<=12 and 0<angka_tebakan<=12:
            print('salah tapi benar berada di 0<x<=12 ')           
            masukantebakan4=int(input('masukan tebakan anda = '))
            angkayangsudahdicoba.append(masukantebakan4)
            print('angka yang sudah dicoba = ',angkayangsudahdicoba)
      
            
            if masukantebakan4==angka_tebakan:
                print('benar',f'\x1b[32m {angka_tebakan}\x1b[0m')
                exit()
            while 0<masukantebakan4<=6 and 0<angka_tebakan<=6:
                print('salah tapi benar berada di 0<x<=6 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
    
            while 6<masukantebakan4<=12 and 6<angka_tebakan<=12:
                print('salah tapi benar berada di 6<x<=12 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
        while 12<masukantebakan3<=25 and 12<angka_tebakan<=25:
            print('salah tapi benar berada di 12<x<=25 ')
            masukantebakan4=int(input('masukan tebakan anda = '))
            angkayangsudahdicoba.append(masukantebakan4)
            print('angka yang sudah dicoba = ',angkayangsudahdicoba)
              
            if masukantebakan4==angka_tebakan:
                print('benar',f'\x1b[32m {angka_tebakan}\x1b[0m')
                exit()
            while 12<masukantebakan4<=18 and 12<angka_tebakan<=18:
                print('salah tapi benar berada di 12<x<=18 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
            while 18<masukantebakan4<=25 and 18<angka_tebakan<=25:
                print('salah tapi benar berada di 18<x<=25 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
            else:print('salah')    
    while 25<masukantebakan2<=50 and 25<angka_tebakan<=50:
        print('salah tapi benar berada di 25<x<=50 ')
        masukantebakan3=int(input('masukan tebakan anda = '))
        angkayangsudahdicoba.append(masukantebakan3)
        print('angka yang sudah dicoba = ',angkayangsudahdicoba)
        if masukantebakan3==angka_tebakan:
            print('benar',f'\x1b[32m {angka_tebakan}\x1b[0m')
            exit()
        while 25<masukantebakan3<=37 and 25<angka_tebakan<=37:
            print('salah tapi benar berada di 25<x<=37 ')
            masukantebakan4=int(input('masukan tebakan anda = '))
            angkayangsudahdicoba.append(masukantebakan4)
            print('angka yang sudah dicoba = ',angkayangsudahdicoba)
    
            if masukantebakan4==angka_tebakan:
                print('benar',f'\x1b[32m {angka_tebakan}\x1b[0m')
                exit()
            while 25<masukantebakan4<=31 and 25<angka_tebakan<=31:
                print('salah tapi benar berada di 25<x<=31 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
            while 31<masukantebakan4<=38 and 31<angka_tebakan<=38:
                print('salah tapi benar berada di 31<x<=38 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
        while 37<masukantebakan3<=50 and 37<angka_tebakan<=50:
            print('salah tapi benar berada di 37<x<=50 ')
            masukantebakan4=int(input('masukan tebakan anda = '))
            angkayangsudahdicoba.append(masukantebakan4)
            print('angka yang sudah dicoba = ',angkayangsudahdicoba)
            if masukantebakan4==angka_tebakan:
                print('benar',f'\x1b[32m {angka_tebakan}\x1b[0m')
                exit()
            while 38<masukantebakan4<=44 and 38<angka_tebakan<=44:
                print('salah tapi benar berada di 38<x<=44 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
            while 44<masukantebakan4<=50 and 44<angka_tebakan<=50:
                print('salah tapi benar berada di 44<x<=50 ')
                masukantebakan5=int(input('masukan tebakan anda = '))
                angkayangsudahdicoba.append(masukantebakan5)
                print('angka yang sudah dicoba = ',angkayangsudahdicoba)
                if masukantebakan5==angka_tebakan:
                    print('BENAR!!!!!',f'\x1b[32m {angka_tebakan}\x1b[0m')
                else:print('SALAH!!!!!')
            else:print('salah')
        else:print('salah')    
       
            
    