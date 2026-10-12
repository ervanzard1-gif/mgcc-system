import random
a='a'
b='b'
c='c'
d='d'
e='e'
f='f'
g='g'
h='h'
i='i'

board=f'''
 {a} | {b} | {c}
-----------
 {d} | {e} | {f}
-----------
 {g} | {h} | {i}
'''
print(board)

data='pertama kali'

datainputboard=[]

jalan=random.choice(['saya','komputer'])
while True:
        
    if jalan=='saya' and data=='sudah jalan':
        jalan='komputer'
    elif jalan=='komputer' and data=='sudah jalan':
        jalan='saya'
    if data=='pertama kali':
        print('yang jalan duluan = ',jalan)
        data='sudah jalan'

    

    if jalan=='saya':
        pilihan=input('pilih posisi (a-i) : ')
        while pilihan in datainputboard:
            print('posisi sudah diisi, pilih posisi lain')
            pilihan=input('pilih posisi (a-i) : ')
            if pilihan not in datainputboard:
                break
            elif pilihan in datainputboard:
                continue

        if pilihan=='a':
            a='\x1b[32mX\x1b[0m'
        elif pilihan=='b':
            b='\x1b[32mX\x1b[0m'
        elif pilihan=='c':
            c='\x1b[32mX\x1b[0m'
        elif pilihan=='d':
            d='\x1b[32mX\x1b[0m'
        elif pilihan=='e':
            e='\x1b[32mX\x1b[0m'
        elif pilihan=='f':
            f='\x1b[32mX\x1b[0m'
        elif pilihan=='g':
            g='\x1b[32mX\x1b[0m'
        elif pilihan=='h':
            h='\x1b[32mX\x1b[0m'
        elif pilihan=='i':
            i='\x1b[32mX\x1b[0m'

        board=f'''
 {a} | {b} | {c}
-----------
 {d} | {e} | {f}
-----------
 {g} | {h} | {i}
'''
   
        print(board)
        datainputboard.append(pilihan)
        

    elif jalan=='komputer':
        pilihan=random.choice(['a','b','c','d','e','f','g','h','i'])
        while pilihan in datainputboard:
            print('posisi sudah diisi, pilih posisi lain')
            pilihan=random.choice(['a','b','c','d','e','f','g','h','i'])
            if pilihan not in datainputboard:
                break
            elif pilihan in datainputboard:
                continue
        if pilihan=='a':
            a='\x1b[31mO\x1b[0m'
        elif pilihan=='b':
            b='\x1b[31mO\x1b[0m'
        elif pilihan=='c':
            c='\x1b[31mO\x1b[0m'
        elif pilihan=='d':
            d='\x1b[31mO\x1b[0m'
        elif pilihan=='e':
            e='\x1b[31mO\x1b[0m'
        elif pilihan=='f':
            f='\x1b[31mO\x1b[0m'
        elif pilihan=='g':
            g='\x1b[31mO\x1b[0m'
        elif pilihan=='h':
            h='\x1b[31mO\x1b[0m'
        elif pilihan=='i':
            i='\x1b[31mO\x1b[0m'

        board=f'''
 {a} | {b} | {c}
-----------
 {d} | {e} | {f}
-----------
 {g} | {h} | {i}
'''
   
        print(board)
        datainputboard.append(pilihan)

    if 'X' in a and 'X' in b and 'X' in c or 'X' in d and 'X' in e and 'X' in f or 'X' in g and 'X' in h and 'X' in i or 'X' in a and 'X' in d and 'X' in g or 'X' in b and 'X' in e and 'X' in h or 'X' in c and 'X' in f and 'X' in i or 'X' in a and 'X' in e and 'X' in i or 'X' in c and 'X' in e and 'X' in g:
        print('saya menang')
        break
    elif 'O' in a and 'O' in b and 'O' in c or 'O' in d and 'O' in e and 'O' in f or 'O' in g and 'O' in h and 'O' in i or 'O' in a and 'O' in d and 'O' in g or 'O' in b and 'O' in e and 'O' in h or 'O' in c and 'O' in f and 'O' in i or 'O' in a and 'O' in e and 'O' in i or 'O' in c and 'O' in e and 'O' in g:
        print('komputer menang')
        break
    else: print('belum ada yang menang')
