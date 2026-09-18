#LISZZZZZZT
#
#p1=['tanah para bandit','novel','tere liye']
#p2=['janji','novel','tere liye']
#p3=['seporsi mie ayam sebelum mati','novel','brian khrisna']
#p4=['sebuah seni untuk bersikap bodo amat','self-improvement','mark manson']
#p5=['physics->principle and application edision 7 jilid 1','science','giancoli']
#p6=['basic physics edisi 7 jilid 1','science','halliday/resnick/walker']
#p7=['basic physics edisi 7 jilid 2','science','halliday/resnick/walker']
#p8=['how to solve it','education','G.POLYA']
#
#databuku=[p1,p2,p3,p4,p5,p6,p7,p8]
#
#for i in databuku:
#    print('judul buku=',i[0])
#    print('tipe=',i[1])
#    print('penulis=',i[2],'\n\n\n')
#
#
#print('===================================\n\n\n\n\n')
#
#list_rank=[]
#while True:
#    nama=input('masukan nama=')
#    ranking=input('masukan ranking=')
#    
#    data=[nama,ranking]
#    list_rank.append(data)
#    print(f'{'NO':<5}|{'NAMA':<20}|{'RANK':<10}')
#    for index,i in enumerate(list_rank):
#        print(f'{index:<5}|{i[0]:<20}|{i[1]:<10}')
#
#    x=input('apakah dilanjutkan?')
#    if x=='no':
#        print('terima kasih')
#        break
#
#
#    elif x=='ya':
#        continue


datasb=[]
while True:
    nama=input('masukan nama=')
    klub=input('masukan klub pemain=')
    dt=[nama,klub]

    datasb.append(dt)

    for index,i in enumerate(datasb):
        print(f'{index:<5}',f'|{i[0]:<20}',f'|{i[1]:<10}')

    data=input('lanjut?=')
    if data=='y':
        continue
    elif data=='n':
        print('terimakasih')
        break





