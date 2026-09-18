#pilihan='caleyy'
#
#match pilihan:
#    case 'caleyy':print('edinburgh')
#    case 'fara':print('kyushu')
#
#
#
#
## Match dengan struktur data
#def proses_command(command):
#    match command.split():
#        case ["quit"]:
#            print("Keluar dari program")
#        case ["hello", nama]:
#            print(f"Halo, {nama}!")
#        case ["tambah", x, y]:
#            print(f"Hasil: {int(x) + int(y)}")
#        case _:
#            print("Command tidak dikenal")
#
#proses_command('quit')
#proses_command('hallo ervanza')
#
#
#data=80
#
#status='lulus' if data>=76 else 'tidak lulus'
#print(status)
#
#
#
#a=2
#while a<100:
#    b=2
#    while b<=a/b:
#        if not(a%b):
#            break
#        b+=1
#
#    if b>(a/b):
#        print(a,'is prima')
#
#    a+=1
#
#while True:
#    data=input('masukan kode')
#
#    while data:
#        print('i want to study in china, hunmgary, or taiwan ')
#
#    print('sekian')
#    break
#
#while True:
#    data=int(input('masukan kode'))
#
#    while data:
#        print('i want to study in china, hunmgary, or taiwan ')
#
#    print('sekian')
#    break
#
#
#
#pilihan='caleyy'
#match pilihan:
#    case 'caleyy':print('fitb')
#    case 'fara':print('fitb too')
#
#
#a=2
#while a<100:
#    b=2
#    while b<=(a/b):
#        if not (a%b):
#            break
#        b+=1
#
#    if b>(a/b):
#        print(a,'is prime')
#        
#
#    a+=1
#
#
#
#def command(command):
#    match command.split():
#        case['quit']:
#            print('keluar')
#        case['hello',nama]:
#            print(f'hello {nama}')
#        case['jumlah', x, y]:
#            print(f'jumlah {int(x)+int(y)}')
#        case _:
#            print('fault input')
#command('hello world')
#command('jumlah 5 9')
#    
#
#def x(text):
#    match text.split():
#        case['quit']:
#            print('keluar')
#        case['hello',nama]:
#            print(f'hello {nama}')
#        case['jumlah', x, y]:
#            print(f'jumlah {int(x)+int(y)}')
#        case _:
#            print('salah input')
#x('hello ervanza')
#x('jumlah 5 6')
#
#
#a=2
#while a<100:
#    b=2
#    while b<=(a/b):
#        if not (a%b):
#            break
#        b+=1
#
#
#    if b>(a/b):
#        print(a,'is prime')
#
#    a+=1
        
def x():
    print('halo')

x()

def x(data):
    print(f'halo {data}')
x('evan')
x('syauqi')



def x(data):
    print(data,'*',data,'=',data*data)

x(2)

def x(data):
    print(f'{data}*{data}={data*data}')

x(2)

#print((2+'ayam')) #error


def x(data):
    match data.split():
        case ['quit']:
            print('keluar')
        case ['hallo',nama]:
            print('hallo',nama)

        case ['penjumlahan',data1,data2]:
            print('penjumlahan',int(data1)+int(data2))

x('quit')
x('hallo evan')
x('penjumlahan 1 4')


data='saya evan'

match data.split():
    case ['saya',nama]:
        print('saya',nama)


#prima project
a=2
while a<100:
    b=2
    while b<=(a/b):
        if not (a%b):
            break
        b+=1
    if b>(a/b):
        print(a,'is prime')

    a+=1


