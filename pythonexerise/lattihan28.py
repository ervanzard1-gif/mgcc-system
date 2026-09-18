data='*'

while True:
    print(f'{data}')
    data+='*'
    if data==10*'*':
        break


sisi=9
count=1
for i in range(sisi):
    print("*"*count)
    count+=1


sisi=10
count=1
while True:
    print('*'*count)
    if sisi==count:
        break
    count+=1


sisi=15
count=1
while True:
    print('*'*count)
    if sisi==count:
        break
    count+=2
print('=======================')
sisi=13
count=1
for i in range(sisi):
    print("*"*count)
    count+=2

print('=======================')

sisi=10
data=0
while True:
    data+=1
    if data==sisi:
        break
    if data%2==0:
        continue
    print('*'*data)


sisi=10
data=0
spasi=int(sisi/2)
while True:
    data+=1
    if data==sisi:
        break
    if data%2==0:
        continue
    spasi-=1
    print(' '*spasi,'*'*data)


sisi=0
data=8
spasi=int(sisi/2)
while True:
    data-=1
    if data==sisi:
        break
    if data%2==0:
        continue
    spasi+=1
    print(' '*spasi,'*'*data)


sisi=10
data=0
while True:
    data+=1
    if data==sisi:
        break
    if data%2==0:
        continue
    print('*'*data)


sisi=0
data=10
spasi=-2
while True:
    data-=1
    if data==sisi:
        break
    if data%2==0:
        continue
    spasi+=2
    print(f'{' '*spasi}{'*'*data}')

sisi=10
data=0
while True:
    data+=1
    if data==sisi:
        break
    if data%2==0:
        continue
    print('*'*data)


sisi=0
data=10
spasi=-2
while True:
    data-=1
    if data==sisi:
        break
    if data%2==0:
        continue
    spasi+=2
    print(' '*spasi,'*'*data)




nama='epan'
x='radit'
print(nama+x)
print(nama,x)
print(f'{nama}{x}')



data=30
sisi=10
spasi=0
for i in range(sisi):
    spasi+=2
    print(' '*spasi+'*'*data)
print('===================================')
data=10
sisi=0
spasi=10
while True:
    sisi+=1
    if 3==sisi:
        break
    if sisi%2==0:
        print(' '*spasi+'*'*data)
        continue
    print('*'*data)
    
print('==========================================================================================')
data=1
for i in range(10):
    print('*'*data)

data=2
tinggi=7
for i in range(tinggi):
    print('*'*data)

data='Ervanza'
for i in data:
    print(data)

data='Ervanza'
for i in data:
    print(i)

data=10
for i in range(10):
    print('*'*data)

bawah=10
atas=0
while True:
    atas+=1
    if atas==bawah:
        break
    print('*'*atas)


bawah=0
atas=10
while True:
    atas-=1
    if atas==bawah:
        break
    print('*'*atas)


atas=0
bawah=12
while True:
    atas+=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    print('*'*atas)


atas=10
bawah=0
while True:
    atas-=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    print('*'*atas)


atas=0
bawah=10
spasi=int((bawah/2)+1)
while True:
    atas+=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    spasi-=1
    print(' '*spasi+'*'*atas)


atas=12
bawah=0
spasi=-1
while True:
    atas-=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    spasi+=1
    print(' '*spasi+'*'*atas)


atas=0
bawah=10
while True:
    atas+=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    print('*'*atas)


atas=10
bawah=0
spasi=-1
while True:
    atas-=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    spasi+=2
    print(' '*spasi+'*'*atas)





atas=0
bawah=10
while True:
    atas+=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    print('*'*atas)


atas=10
bawah=0
spasi=-2
while True:
    atas-=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    spasi+=2
    print(' '*spasi+'*'*atas)


data=10
for i in range(10):
    print(i)

data=10
while data<10:
    print(data)

atas=0
bawah=10
spasi=10
while True:
    atas+=1
    if atas==bawah:
        break
    if data%2==0:
        print(' '*spasi+'*'*bawah)
    print('*'*bawah)
    

atas=0
bawah=10
spasi=12
while True:
    atas+=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    spasi-=2
    print(' '*spasi+'*'*atas)

atas=12
bawah=0
spasi=-2
while True:
    atas-=1
    if atas==bawah:
        break
    if atas%2==0:
        continue
    spasi+=2
    print(' '*spasi+'*'*atas)


data='ervanza'
for i in data:
    print(i)
data='ervanza'
for i in data:
    print(data)

lebar=2
tinggi=7
for i in range(tinggi):
    print('*'*lebar)


atas=17
samping=5
spasi=-1
for i in range(samping):
    spasi+=1
    print(' '*spasi,'*'*atas)

print('\n')

lebar=20
tinggi=5
kuping=int(lebar/2)
for i in range(tinggi):
    print('*'*(kuping)+' '*20+'*'*(kuping))



lebar=40
tinggi=15
for i in range(tinggi):
    if i==3 or i==4 or i==5 or i==6:
        print('*'*5+' '*10+'*'*10+' '*10+'*'*5)
        continue

    if i==12:
        print('*'*10+' '*20+'*'*10)
        continue
    print('*'*lebar)
  

data=len('*'*(kuping)+' '*20+'*'*(kuping))
print(data)

datax='15'
for i in datax:
    print(i)


print('\n')
tinggi=5
isi=2
kuping=int(isi/2)
spasi=38
for i in range(tinggi):
    print('*'*kuping+' '*spasi+'*'*kuping)
    kuping+=2
    spasi-=4


tinggi=12
isi=40
mata=int(isi/4)
for i in range(tinggi):
    if i==3 or i==4 or i==5 or i==6:
        print('*'*5+' '*mata+'*'*10+' '*mata+'*'*5)
        continue
    if i==10:
        print('*'*9+' '*22+'*'*9)
        continue

    print('*'*isi)


tinggi=3
isi=40
spasi=0
for i in range(tinggi):
    print(' '*spasi+'*'*isi)
    spasi+=6
    isi-=12

isi=16
tinggi=1
spasi=12
for i in range(tinggi):
    print(' '*spasi+'*'*isi)

isi=16
tinggi=4
spasi=12
for i in range(tinggi):
    print(' '*spasi+'*'*isi)
    spasi-=3
    isi+=6


isi=40
tinggi=22
for i in range(tinggi):
    print('*'*isi)


isi=20
tinggi=8
kaki=int(isi/2)
x=7
p=4
q=3
for i in range(tinggi):
    if i==5 or i==6 or i==7:
        kaki+=2
        x-=2
        print(' '*x+'*'*kaki+' '*6+'*'*kaki+' '*x)
        continue

    if i==0 or i==1 or i==2:
        p-=1
        q+=1

        print('*'*p+' '*q+'*'*kaki+' '*6+'*'*kaki+' '*q+'*'*p)
        continue
    print(' '*7+'*'*kaki+' '*6+'*'*kaki+' '*7)


atas=1
spasi=31
while True:
    print(' '*spasi+'*'*atas)
    atas+=2
    spasi-=1
    if atas==21:
        break


body=63
spasi=0
while True:
     print(' '*spasi+'*'*body)
     body-=4
     spasi+=2
     if body==31:
         break

data=37
tinggi=11
spasi=13
spasi1=12
spasi2=1
spasi3=13
kaki=19
for i in range(tinggi):
    if i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8 or i==9 or i==10:
        print(' '*spasi1+'*'*kaki+' '*spasi2+'*'*kaki+' '*spasi3)
        spasi2+=6
        spasi1-=1
        spasi3-=1
        kaki-=2
        continue


    print(' '*spasi+'*'*data)

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

data1='/'
data2='\\'
spasi1=20
spasi2=0
baris=9
spasix=4
spasiy=10
e=0
f=0
g=0
h=4
for i in range(baris):
    if i==0 or i==1 :
        print(' '*spasi1+data1+' '*spasi2+data2)

    if  i==3 :
        print(' '*spasi1+data1+' '*e+data2+' '*spasix+data1+data2)

    if i==4:
        e+=2
        spasix-=2
        print(' '*spasi1+data1+' '*e+data2+' '*spasix+data1+' '*e+data2)
       

    if i==6 :
        print(' '*spasi1+data1+' '*f+data2+' '*h+data1+g*' '+data2+' '*h+data1+' '*f+data2)
    if i==7 :
        f+=2
        spasiy-=2
        h-=2
        g+=2
        print(' '*spasi1+data1+' '*f+data2+' '*h+data1+g*' '+data2+' '*h+data1+' '*f+data2)
        
       
    if i==2 : 
        spasi1-=0
        spasi2+=0
        print(' '*spasi1+data1+'_'*spasi2+data2)

    if  i==5: 
        e+=2
        print(' '*spasi1+data1+'_'*e+'\/'+'_'*e+data2)


    if  i==8: 
        f+=2
        print(' '*spasi1+data1+'_'*e+'\/'+'_'*e+'\/'+e*'_'+data2)

        
    spasi1-=1
    spasi2+=2
    

