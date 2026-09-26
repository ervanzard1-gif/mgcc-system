
x=5
yabs=30
spasi=12
y=0
for i in range(x):
    print(' '*spasi+f'\x1b[31m{'*'*yabs}\x1b[0m'+f'\x1b[32m{'*'*y}\x1b[0m')
    
    spasi-=3
    y+=3

y1=30
y1abs=12
x1=9
for i in range(x1):
    print(f'\x1b[34m{'*'*y1}\x1b[0m'+f'\x1b[32m{'*'*y1abs}\x1b[0m')

x2=5
y2abs=30
y2=12
spasi2=0
for i in range(x2):
    print(' '*spasi+f'\x1b[34m{'*'*y2abs}\x1b[0m'+f'\x1b[32m{'*'*y2}\x1b[0m')
    spasi2+=3
    y2-=3
print('\n\n\n\n\n\n\n\n')


tinggi=5
hori=30
horiabs=30
verti=1
spasi=12
spasiabs=12
spasikecil=1
space=-1
horiabs2=30
for i in range(tinggi):
    if i==0:
        print(' '*spasi+'*'*hori)
    elif i in range(1,4):
        print(' '*spasi+'*'+' '*space +'*'+' '*(horiabs-2)+'*'+' '*(spasikecil-2)+'*')
    elif i==4:
        print('*'*horiabs2+' '*(spasiabs-1)+'*')
    spasi-=3
    hori+=3
    spasikecil+=3
    space+=3
    horiabs-=3


tinggi=9
verti=1
hori=12
horiabs=18
for i in range(tinggi):
    print('*'*verti+' '*(hori-1)+'*'+' '*(horiabs-2)+'*'+' '*(hori-1)+'*')


tinggi=5
hori=12
horiabs=30
verti=1
spasi=0
spasiabs1=12
spasiu=16
horiabs2=13
for i in range(tinggi):
    if i==0:
        print('*'+' '*(spasiabs1-1)+'*'+'*'*(horiabs-1)+' '*(hori-1))

    elif i in range(1,4):
        print('*'+' '*(hori-1)+'*'+' '*spasiu+'*'+' '*(horiabs2-2)+'*')
    elif i==4:
        print('*'*horiabs+' '*spasi)
    spasi+=3
    hori-=3
    spasiu+=3
    horiabs2-=3