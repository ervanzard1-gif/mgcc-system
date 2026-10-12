import random
dataangka=list(range(1, 101))

datasaya=[]
databot=[]

jalan=random.choice(['saya','komputer'])
datajalan='pertama kali'
while True:

    if datajalan=='pertama kali':
        print('yang jalan duluan = ',jalan)
        datajalan='sudah jalan'

    if jalan=='saya':
        print('giliran anda')
        masukandataanda=input('masukan angka (1-3) = ')
        if masukandataanda=='1':
            datasaya.append(dataangka[0])
            print(datasaya)
            print(dataangka[0])
            del dataangka[0]
        elif masukandataanda=='2':
            datasaya.append(dataangka[0])
            datasaya.append(dataangka[1])
            print(datasaya)
            print(dataangka[0],dataangka[1])
            del dataangka[0:2]
        elif masukandataanda=='3':
            datasaya.append(dataangka[0])
            datasaya.append(dataangka[1])
            datasaya.append(dataangka[2])
            print(datasaya)
            print(dataangka[0],dataangka[1],dataangka[2])
            del dataangka[0:3]
        

    elif jalan=='komputer':
        print('giiliran komputer')
        masukandatabot=random.choice(['1','2','3'])
        if masukandatabot=='1':
            databot.append(dataangka[0])
            print(databot)
            print(dataangka[0])
            del dataangka[0]
        elif masukandatabot=='2':
            databot.append(dataangka[0])
            databot.append(dataangka[1])
            print(databot)
            print(dataangka[0],dataangka[1])
            del dataangka[0:2]
        elif masukandatabot=='3':
            databot.append(dataangka[0])
            databot.append(dataangka[1])
            databot.append(dataangka[2])
            print(databot)
            print(dataangka[0],dataangka[1],dataangka[2])
            del dataangka[0:3]

    if 21 in datasaya:
        print('anda kalah')
        break
    elif 21 in databot:
        print('anda menang')
        break

    if datajalan=='sudah jalan' and jalan=='saya':
        jalan='komputer'

    elif datajalan=='sudah jalan' and jalan=='komputer':
        jalan='saya'