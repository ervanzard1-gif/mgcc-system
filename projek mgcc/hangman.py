import random
datahangman=['''
=========
  |     |
        |
        |
        |
---------
''','''
=========
  |     |
  0     |
        |
        |
---------
''','''
=========
  |     |
  0     |
  |     |
        |
---------
''','''
=========
  |     |
  0     |
  |\\    |
        |
---------
''','''
=========
  |     |
  0     |
 /|\\    |
        |
---------
''','''
=========
  |     |
  0     |
 /|\\    |
 /      |
---------
''','''
=========
  |     |
  0     |
 /|\\    |
 / \\    |
---------
'''
]


katahewan=['kucing','anjing','monyet','jerapah','kambing','kangguru']

angkanyawa=0
nyawa=datahangman[angkanyawa]

tebak=random.choice(katahewan)
tebakan1=list(tebak)
panjangdata=len(tebakan1)
data1=random.choice((list(tebakan1)))
data1index=tebakan1.index(data1)
print(data1index)
del tebakan1[data1index]
print(data1)

tebakan2=list(tebak)
while True:
       data2=random.choice((list(tebakan2)))
       if data2==data1:
               continue
       
       elif data2!=data1:
               data2index=tebakan2.index(data2)
               print(data2index)
               del tebakan2[data2index]
               print(data2)
               break

tebakan1=list(panjangdata*'_')
tebakan1[int(data1index)]=data1
tebakan1[int(data2index)]=data2

while True:    
        print(' '.join(tebakan1))

        print(nyawa)
        if angkanyawa==6:
                print('kalah')
                exit()

        jawaban=input('masukan jawaban anda = ')
        if jawaban==tebak:
                print('benar')
                break

        elif jawaban!=tebak:
                print('salah')
                angkanyawa+=1
                nyawa=datahangman[angkanyawa]
                #tebakan1.insert(data1index,data1)
                #tebakan2.insert(data2index,data2)
                continue
        

        
    
    
    
    
