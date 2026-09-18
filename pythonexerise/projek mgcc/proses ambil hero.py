import random
import math
kishin={'lancelot','lunox','franco','karrie','angela','dyrroth'}#
dragoncaller={'badang','gusion','clint','eudora','balmond','zilong'}#
bruiser={'badang','dyrroth','yin','paquito','aldous','bellerick'}#
dauntless={'franco','uranus','hilda','lolita','alice','balmond'}#
marksman={'karrie','miya','granger','melissa','irithel','wanwan'}#
starballe={'fanny','lolita','cici','miya','edith','zhuxin'}#
weapon_master={'zilong','thamuz','cici','franco','martis','suyou'}#
zodiac={'odette','hilda','martis','minotour','irithel','karina'}#
scavengger={'angela','sora','phoveus'}#
echomancer={'harley','vale','natalia','tigreal','sora','thamuz'}#
spectre={'phoveus','granger','paquito','alice','saber','gord'}#
mistbender={'nana','uranus','aldous'}
stargazer={'nana','lunox','mathilda','luo yi','eudora','karina'}
swiftblade={'karina','yin sun-shin','natalia','saber','gusion','fanny'}#
mage={'odette','vale','gord','vexana','zhuxin','kadita'}#
defender={'hylos','minotour','baxia','tigreal','edith','atlas'}#
phasewarper={'kadita','harley','lancelot','clint'}#
shadeweaver={'hylos','melissa','kadita'}#
dragonaltar={'baxia','suyou','luo yi','wanwan','yin sun-shin','yin'}#
enchanted_tales={'atlas','vexana','bellerick','mathilda'}#
gold1=['yin sun-shin','vale','phoveus','dyrroth','uranus','cici','minotour','eudora']
gold2=['angela','balmond','bellerick','granger','miya','zhuxin','martis','harley','natalia','luo yi','hylos']
gold3=['franco','clint','aldous','paquito','hilda','wanwan','edith','karina','tigreal','saber','mathilda','kadita']
gold4=['karrie','lunox','gusion','yin','lolita','irithel','zilong','suyou','sora','gord','vexana','atlas']
gold5=['lancelot','badang','thamuz','melissa','nana','baxia','odette','fanny','alice']
gold7=['alpha']


#print(tuple(kishin & bruiser))
heroprotagonis={'atlas','vexana'}
gold=2
protagonis=random.choice(('atlas','vexana'))
print(f'protagonis pada game ini adalah={protagonis}')


heroyangdipunya=[]
kemenangan=[]
stackechomancer=0
stackenchanted_tales=0

granger_sudah=False
paquito_sudah=False
gord_sudah=False
alice_sudah=False
alpha_sudah=False

while True:
    menu=input('pilih menu= ')
    datahero0=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero1=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero2=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero3=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero4=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    herostore=[datahero0,datahero1,datahero2,datahero3,datahero4]
    if menu=='store':
            while True:
                    print(herostore)
                    ambil=input('apakah anda ingin mengambil hero? (y/n) : ')
                    if ambil=='y':
                        kode=input('masukkan kode hero yang ingin diambil (1-5) : ')
                        hero=herostore[(int(kode)-1)]
                        if hero in gold1:
                            gold-=1
                            print('sisa gold=',gold)

                        elif hero in gold2:
                            gold-=2
                            print('sisa gold=',gold)
                            
                        elif hero in gold3:
                            gold-=3
                            print('sisa gold=',gold)
                            
                        elif hero in gold4:
                            gold-=4
                            print('sisa gold=',gold)
                            
                        elif hero in gold5:
                            gold-=5
                            print('sisa gold=',gold)
                

                        heroyangdipunya.append(hero)
                        herostore[int(kode)-1]=None
                        if None in heroyangdipunya:
                           data=heroyangdipunya.index(None)
                           del heroyangdipunya[data]
                        print(heroyangdipunya)


                        franco=heroyangdipunya.count('franco')
                        if franco==3:
                            print('franco 1 star ---> franco 2 star')
                            heroyangdipunya.remove('franco')
                            heroyangdipunya.remove('franco')
                            heroyangdipunya.remove('franco')
                            heroyangdipunya.append(f'franco{chr(9733)}2')
                            
                            print(heroyangdipunya)

                        franco_2=heroyangdipunya.count(f'franco{chr(9733)}2')
                        if franco_2==3:
                            print('franco 2 star ---> franco 3 star')
                            heroyangdipunya.remove(f'franco{chr(9733)}2')
                            heroyangdipunya.remove(f'franco{chr(9733)}2')
                            heroyangdipunya.remove(f'franco{chr(9733)}2')
                            heroyangdipunya.append(f'franco{chr(9733)}3')
                            print(heroyangdipunya)

                        alice=heroyangdipunya.count('alice')
                        if alice==3:
                            print('alice 1 star ---> alice 2 star')
                            heroyangdipunya.remove('alice')
                            heroyangdipunya.remove('alice')
                            heroyangdipunya.remove('alice')
                            heroyangdipunya.append(f'alice{chr(9733)}2')
                            print(heroyangdipunya)

                        alice_2=heroyangdipunya.count(f'alice{chr(9733)}2')
                        if alice_2==3:
                            print('alice 2 star ---> alice 3 star')
                            heroyangdipunya.remove(f'alice{chr(9733)}2')
                            heroyangdipunya.remove(f'alice{chr(9733)}2')
                            heroyangdipunya.remove(f'alice{chr(9733)}2')
                            heroyangdipunya.append(f'alice{chr(9733)}3')
                            print(heroyangdipunya)

                        phoveus=heroyangdipunya.count('phoveus')
                        if phoveus==3:
                            print('phoveus 1 star ---> phoveus 2 star')
                            heroyangdipunya.remove('phoveus')
                            heroyangdipunya.remove('phoveus')
                            heroyangdipunya.remove('phoveus')
                            heroyangdipunya.append(f'phoveus{chr(9733)}2')
                            print(heroyangdipunya)

                        phoveus_2=heroyangdipunya.count(f'phoveus{chr(9733)}2')
                        if phoveus_2==3:
                            print('phoveus 2 star ---> phoveus 3 star')
                            heroyangdipunya.remove(f'phoveus{chr(9733)}2')
                            heroyangdipunya.remove(f'phoveus{chr(9733)}2')
                            heroyangdipunya.remove(f'phoveus{chr(9733)}2')
                            heroyangdipunya.append(f'phoveus{chr(9733)}3')
                            print(heroyangdipunya)

                        granger=heroyangdipunya.count('granger')
                        if granger==3:
                            print('granger 1 star ---> granger 2 star')
                            heroyangdipunya.remove('granger')
                            heroyangdipunya.remove('granger')
                            heroyangdipunya.remove('granger')
                            heroyangdipunya.append(f'granger{chr(9733)}2')
                            print(heroyangdipunya)

                        granger_2=heroyangdipunya.count(f'granger{chr(9733)}2')
                        if granger_2==3:
                            print('granger 2 star ---> granger 3 star')
                            heroyangdipunya.remove(f'granger{chr(9733)}2')
                            heroyangdipunya.remove(f'granger{chr(9733)}2')
                            heroyangdipunya.remove(f'granger{chr(9733)}2')
                            heroyangdipunya.append(f'granger{chr(9733)}3')
                            print(heroyangdipunya)
        
                        paquito=heroyangdipunya.count('paquito')
                        if paquito==3:
                            print('paquito 1 star ---> paquito 2 star')
                            heroyangdipunya.remove('paquito')
                            heroyangdipunya.remove('paquito')
                            heroyangdipunya.remove('paquito')
                            heroyangdipunya.append(f'paquito{chr(9733)}2')
                            print(heroyangdipunya)

                        paquito_2=heroyangdipunya.count(f'paquito{chr(9733)}2')
                        if paquito_2==3:
                            print('paquito 2 star ---> paquito 3 star')
                            heroyangdipunya.remove(f'paquito{chr(9733)}2')
                            heroyangdipunya.remove(f'paquito{chr(9733)}2')
                            heroyangdipunya.remove(f'paquito{chr(9733)}2')
                            heroyangdipunya.append(f'paquito{chr(9733)}3')
                            print(heroyangdipunya)
        
                        saber=heroyangdipunya.count('saber')
                        if saber==3:
                            print('saber 1 star ---> saber 2 star')
                            heroyangdipunya.remove('saber')
                            heroyangdipunya.remove('saber')
                            heroyangdipunya.remove('saber')
                            heroyangdipunya.append(f'saber{chr(9733)}2')
                            print(heroyangdipunya)

                        saber_2=heroyangdipunya.count(f'saber{chr(9733)}2')
                        if saber_2==3:
                            print('saber 2 star ---> saber 3 star')
                            heroyangdipunya.remove(f'saber{chr(9733)}2')
                            heroyangdipunya.remove(f'saber{chr(9733)}2')
                            heroyangdipunya.remove(f'saber{chr(9733)}2')
                            heroyangdipunya.append(f'saber{chr(9733)}3')
                            print(heroyangdipunya)
                 
                        gord=heroyangdipunya.count('gord')
                        if gord==3:
                            print('gord 1 star ---> gord 2 star')
                            heroyangdipunya.remove('gord')
                            heroyangdipunya.remove('gord')
                            heroyangdipunya.remove('gord')
                            heroyangdipunya.append(f'gord{chr(9733)}2')
                            print(heroyangdipunya)

                        gord_2=heroyangdipunya.count(f'gord{chr(9733)}2')
                        if gord_2==3:
                            print('gord 2 star ---> gord 3 star')
                            heroyangdipunya.remove(f'gord{chr(9733)}2')
                            heroyangdipunya.remove(f'gord{chr(9733)}2')
                            heroyangdipunya.remove(f'gord{chr(9733)}2')
                            heroyangdipunya.append(f'gord{chr(9733)}3')
                            print(heroyangdipunya)
    


    


                            

                            
                        
            
                        sinergikishin=0
                        sinergibruiser=0
                        sinergidragoncaller=0
                        sinergidauntless=0
                        sinergimarksman=0
                        sinergistarballe=0
                        sinergiweapon_master=0
                        sinergizodiac=0
                        sinergienchanted_tales=0
                        sinergiphasewarper=0
                        sinergimistbender=0
                        sinergidragonaltar=0
                        sinergiswiftblade=0
                        sinergiscavengger=0
                        sinergispectre=0
                        sinergishadeweaver=0
                        sinergidefender=0
                        sinergiechomancer=0
                        sinergistargazer=0
                        sinergimage=0
            
            
            
                        sinergibruiser+=1*len(set(heroyangdipunya).intersection(bruiser))
                        if 0<sinergibruiser<=1:
                            print('sinergi bruiser anda adalah :',sinergibruiser)
                        elif 2<=sinergibruiser<4:
                            print(f'sinergi bruiser anda adalah :\x1b[31m  {sinergibruiser}  \x1b[0m')
                        elif 4<=sinergibruiser<6:
                            print(f'sinergi bruiser anda adalah :\x1b[34m  {sinergibruiser}  \x1b[0m')
                        elif sinergibruiser>=6:
                            print(f'sinergi bruiser anda adalah :\x1b[35m  {sinergibruiser}  \x1b[0m')
            
            
                        
                        sinergikishin+=1*len(set(heroyangdipunya).intersection(kishin))
                        if 0<sinergikishin<=1:
                            print('sinergi kishin anda adalah :',sinergikishin)
                        elif 2<=sinergikishin<4:
                            print(f'sinergi kishin anda adalah :\x1b[31m  {sinergikishin}  \x1b[0m')
                        elif 4<=sinergikishin<6:
                            print(f'sinergi kishin anda adalah :\x1b[34m  {sinergikishin}  \x1b[0m')
                        elif sinergikishin>=6:
                            print(f'sinergi kishin anda adalah :\x1b[35m  {sinergikishin}  \x1b[0m')
                        
                        sinergidragoncaller+=1*len(set(heroyangdipunya).intersection(dragoncaller))
                        if 0<sinergidragoncaller<=1:
                            print('sinergi dragoncaller anda adalah :',sinergidragoncaller)
                        elif 2<=sinergidragoncaller<4:
                            print(f'sinergi dragoncaller anda adalah :\x1b[31m  {sinergidragoncaller}  \x1b[0m')
                        elif 4<=sinergidragoncaller<6:
                            print(f'sinergi dragoncaller anda adalah :\x1b[34m  {sinergidragoncaller}  \x1b[0m')
                        elif sinergidragoncaller>=6:
                            print(f'sinergi dragoncaller anda adalah :\x1b[35m  {sinergidragoncaller}  \x1b[0m')
            
                        sinergidauntless+=1*len(set(heroyangdipunya).intersection(dauntless))
                        if 0<sinergidauntless<=1:
                            print('sinergi dauntless anda adalah :',sinergidauntless)
                        elif 2<=sinergidauntless<4:
                            print(f'sinergi dauntless anda adalah :\x1b[31m  {sinergidauntless}  \x1b[0m')
                        elif 4<=sinergidauntless<6:
                            print(f'sinergi dauntless anda adalah :\x1b[34m  {sinergidauntless}  \x1b[0m')
                        elif sinergidauntless>=6:
                            print(f'sinergi dauntless anda adalah :\x1b[35m  {sinergidauntless}  \x1b[0m')
            
                        sinergimarksman+=1*len(set(heroyangdipunya).intersection(marksman))
                        if 0<sinergimarksman<=1:
                            print('sinergi marksman anda adalah :',sinergimarksman)
                        elif 2<=sinergimarksman<4:
                            print(f'sinergi marksman anda adalah :\x1b[31m  {sinergimarksman}  \x1b[0m')
                        elif 4<=sinergimarksman<6:
                            print(f'sinergi marksman anda adalah :\x1b[34m  {sinergimarksman}  \x1b[0m')
                        elif sinergimarksman>=6:
                            print(f'sinergi marksman anda adalah :\x1b[35m  {sinergimarksman}  \x1b[0m')
            
                        sinergistarballe+=1*len(set(heroyangdipunya).intersection(starballe))
                        if 0<sinergistarballe<=1:
                            print('sinergi starballe anda adalah :',sinergistarballe)
                        elif 2<=sinergistarballe<4:
                            print(f'sinergi starballe anda adalah :\x1b[31m  {sinergistarballe}  \x1b[0m')
                            print(f' anda mendapatkan stickballe dengan sinergi :\x1b[33m {1} \x1b[0m')
                        elif 4<=sinergistarballe<6:
                            print(f'sinergi starballe anda adalah :\x1b[34m  {sinergistarballe}  \x1b[0m')
                        elif sinergistarballe>=6:
                            print(f'sinergi starballe anda adalah :\x1b[35m  {sinergistarballe}  \x1b[0m')
            
                        sinergiweapon_master+=1*len(set(heroyangdipunya).intersection(weapon_master))
                        if 0<sinergiweapon_master<=1:
                            print('sinergi weapon master anda adalah :',sinergiweapon_master)
                        elif 2<=sinergiweapon_master<4:
                            print(f'sinergi weapon_master anda adalah :\x1b[31m  {sinergiweapon_master}  \x1b[0m')
                        elif 4<=sinergiweapon_master<6:
                            print(f'sinergi weapon_master anda adalah :\x1b[34m  {sinergiweapon_master}  \x1b[0m')
                        elif sinergiweapon_master>=6:
                            print(f'sinergi weapon_master anda adalah :\x1b[35m  {sinergiweapon_master}  \x1b[0m')
            
                        sinergizodiac+=1*len(set(heroyangdipunya).intersection(zodiac))
                        if 0<sinergizodiac<=1:
                            print('sinergi zodiac anda adalah :',sinergizodiac)
                        elif 2<=sinergizodiac<4:
                            print(f'sinergi zodiac anda adalah :\x1b[31m  {sinergizodiac}  \x1b[0m')
                        elif 4<=sinergizodiac<6:
                            print(f'sinergi zodiac anda adalah :\x1b[34m  {sinergizodiac}  \x1b[0m')
                        elif sinergizodiac>=6:
                            print(f'sinergi zodiac anda adalah :\x1b[35m  {sinergizodiac}  \x1b[0m')
            
                        sinergimage+=1*len(set(heroyangdipunya).intersection(mage))
                        if 0<sinergimage<=1:
                            print('sinergi mage anda adalah :',sinergimage)
                        elif 2<=sinergimage<4:
                            print(f'sinergi mage anda adalah :\x1b[31m  {sinergimage}  \x1b[0m')
                        elif 4<=sinergimage<6:
                            print(f'sinergi mage anda adalah :\x1b[34m  {sinergimage}  \x1b[0m')
                        elif sinergimage>=6:
                            print(f'sinergi mage anda adalah :\x1b[35m  {sinergimage}  \x1b[0m')
            
                        sinergiswiftblade+=1*len(set(heroyangdipunya).intersection(swiftblade))
                        if 0<sinergiswiftblade<=1:
                            print('sinergi swiftblade anda adalah :',sinergiswiftblade)
                        elif 2<=sinergiswiftblade<4:
                            print(f'sinergi swiftblade anda adalah :\x1b[31m  {sinergiswiftblade}  \x1b[0m')
                        elif 4<=sinergiswiftblade<6:
                            print(f'sinergi swiftblade anda adalah :\x1b[34m  {sinergiswiftblade}  \x1b[0m')
                        elif sinergiswiftblade>=6:
                            print(f'sinergi swiftblade anda adalah :\x1b[35m  {sinergiswiftblade}  \x1b[0m')
            
                        sinergistargazer+=1*len(set(heroyangdipunya).intersection(stargazer))
                        if 0<sinergistargazer<=1:
                            print('sinergi stargazer anda adalah :',sinergistargazer)
                        elif 2<=sinergistargazer<4:
                            print(f'sinergi stargazer anda adalah :\x1b[31m  {sinergistargazer}  \x1b[0m')
                        elif 4<=sinergistargazer<6:
                            print(f'sinergi stargazer anda adalah :\x1b[34m  {sinergistargazer}  \x1b[0m')
                        elif sinergistargazer>=6:
                            print(f'sinergi stargazer anda adalah :\x1b[35m  {sinergistargazer}  \x1b[0m')



            
                        sinergispectre+=1*len(set(heroyangdipunya).intersection(spectre))
                        if 0<sinergispectre<=1:
                            print('sinergi spectre anda adalah :',sinergispectre)
                        elif 2<=sinergispectre<4:
                            print(f'sinergi spectre anda adalah :\x1b[31m  {sinergispectre}  \x1b[0m')
                        elif 4<=sinergispectre<6:
                            print(f'sinergi spectre anda adalah :\x1b[34m  {sinergispectre}  \x1b[0m')
                        elif sinergispectre>=6:
                            print(f'sinergi spectre anda adalah :\x1b[35m  {sinergispectre}  \x1b[0m')

                        if heroyangdipunya.count(f'phoveus{chr(9733)}2')==1 and not granger_sudah:
                            print('mendapatkan granger')
                            heroyangdipunya.append('granger')
                            print(heroyangdipunya)
                            granger_sudah=True

                        elif sinergispectre==2 and heroyangdipunya.count(f'granger{chr(9733)}2')==1 and not paquito_sudah:
                            print('mendapatkan paquito')
                            heroyangdipunya.append('paquito')
                            print(heroyangdipunya)
                            paquito_sudah=True
                        
                        elif sinergispectre==4 and (heroyangdipunya.count(f'paquito{chr(9733)}2')==1 or heroyangdipunya.count(f'saber{chr(9733)}2')==1) and not gord_sudah:
                            print('mendapatkan gord')
                            heroyangdipunya.append('gord')
                            print(heroyangdipunya)
                            gord_sudah=True

                        elif sinergispectre==6 and heroyangdipunya.count(f'gord{chr(9733)}2')==1 and not alice_sudah:
                            print('mendapatkan alice')
                            heroyangdipunya.append('alice')
                            print(heroyangdipunya)
                            alice_sudah=True

                        elif sinergispectre==6 and heroyangdipunya.count(f'alice{chr(9733)}2')==1 and not alpha_sudah:
                            print('mendapatkan alpha')
                            heroyangdipunya.append('alpha')
                            print(heroyangdipunya)
                            alpha_sudah=True
                            spectre.append(gold7)
                        
                        
                        


                        
            
                        sinergidefender+=1*len(set(heroyangdipunya).intersection(defender))
                        if 0<sinergidefender<=1:
                            print('sinergi defender anda adalah :',sinergidefender)
                        elif 2<=sinergidefender<4:
                            print(f'sinergi defender anda adalah :\x1b[31m  {sinergidefender}  \x1b[0m')
                        elif 4<=sinergidefender<6:
                            print(f'sinergi defender anda adalah :\x1b[34m  {sinergidefender}  \x1b[0m')
                        elif sinergidefender>=6:
                            print(f'sinergi defender anda adalah :\x1b[35m  {sinergidefender}  \x1b[0m')
            
                        sinergiechomancer+=1*len(set(heroyangdipunya).intersection(echomancer))
                        if 0<sinergiechomancer<=1:
                            print('sinergi echomancer anda adalah :',sinergiechomancer)
                        elif 2<=sinergiechomancer<4:
                            print(f'sinergi echomancer anda adalah :\x1b[31m  {sinergiechomancer}  \x1b[0m')
                        elif 4<=sinergiechomancer<6:
                            print(f'sinergi echomancer anda adalah :\x1b[34m  {sinergiechomancer}  \x1b[0m')
                        elif sinergiechomancer>=6:
                            print(f'sinergi echomancer anda adalah :\x1b[35m  {sinergiechomancer}  \x1b[0m')
            
                        sinergidragonaltar+=1*len(set(heroyangdipunya).intersection(dragonaltar))
                        if 0<sinergidragonaltar<=1:
                            print('sinergi dragonaltar anda adalah :',sinergidragonaltar)
                        elif 2<=sinergidragonaltar<4:
                            print(f'sinergi dragonaltar anda adalah :\x1b[31m  {sinergidragonaltar}  \x1b[0m')
                        elif 4<=sinergidragonaltar<6:
                            print(f'sinergi dragonaltar anda adalah :\x1b[34m  {sinergidragonaltar}  \x1b[0m')
                        elif sinergidragonaltar>=6:
                            print(f'sinergi dragonaltar anda adalah :\x1b[35m  {sinergidragonaltar}  \x1b[0m')
            
                        sinergienchanted_tales+=1*len(set(heroyangdipunya).intersection(enchanted_tales))
                        if 0<sinergienchanted_tales<=1:
                            print('sinergi enchanted_tales anda adalah :',sinergienchanted_tales)
                        elif 2<=sinergienchanted_tales<4:
                            print(f'sinergi enchanted_tales anda adalah :\x1b[36m  {sinergienchanted_tales}  \x1b[0m')
                        elif sinergienchanted_tales==4:
                            print(f'sinergi enchanted_tales anda adalah :\x1b[32m  {sinergienchanted_tales}  \x1b[0m')
                            
                        sinergishadeweaver+=1*len(set(heroyangdipunya).intersection(shadeweaver))
                        if 0<sinergishadeweaver<=1:
                            print('sinergi shadeweaver anda adalah :',sinergishadeweaver)
                        elif 2<=sinergishadeweaver<3:
                            print(f'sinergi shadeweaver anda adalah :\x1b[36m  {sinergishadeweaver}  \x1b[0m')
                        elif sinergishadeweaver==3:
                            print(f'sinergi shadeweaver anda adalah :\x1b[32m  {sinergishadeweaver}  \x1b[0m')
            
                        sinergiphasewarper+=1*len(set(heroyangdipunya).intersection(phasewarper))
                        if 0<sinergiphasewarper<=1:
                            print('sinergi phasewarper anda adalah :',sinergiphasewarper)
                        elif 2<=sinergiphasewarper<4:
                            print(f'sinergi phasewarper anda adalah :\x1b[36m  {sinergiphasewarper}  \x1b[0m')
                        elif sinergiphasewarper==4:
                            print(f'sinergi phasewarper anda adalah :\x1b[32m  {sinergiphasewarper}  \x1b[0m')
            
                        sinergimistbender+=1*len(set(heroyangdipunya).intersection(mistbender))
                        if sinergimistbender==1:
                            print(f'sinergi mistbender anda adalah :\x1b[33m {sinergimistbender} \x1b[0m')
                        elif sinergimistbender==2:
                            print(f'sinergi mistbender anda adalah :\x1b[36m  {sinergimistbender}  \x1b[0m')
                        elif sinergimistbender==3:
                            print(f'sinergi mistbender anda adalah :\x1b[32m  {sinergimistbender}  \x1b[0m')
                    
                        sinergiscavengger+=1*len(set(heroyangdipunya).intersection(scavengger))
                        if 0<sinergiscavengger<2:
                            print('sinergi scavengger anda adalah :',sinergiscavengger)
                        elif 2<=sinergiscavengger<3:
                            print(f'sinergi scavengger anda adalah :\x1b[36m  {sinergiscavengger}  \x1b[0m')
                        elif sinergiscavengger==3:
                            print(f'sinergi scavengger anda adalah :\x1b[32m  {sinergiscavengger}  \x1b[0m')
            
    
                        ambillagi=input('apakah anda ingin mengambil hero lagi ? (y/n) : ')
                        if ambillagi=='y':
                            continue
                        elif ambillagi=='n':
                            break
                    elif ambil=='n':
                        print('refresh hero store')
                        break 
    
    

        
    elif menu=='match':
        kondisi=random.choice(('menang','kalah'))


        kemenangan.append(kondisi)
        print(kemenangan)
        if 'kalah' in kemenangan:
            kemenangan.clear()
            print()


        if kondisi=='menang':
            print('menang')
            if gold<10:
              print('mendapatkan 7 gold')
              gold+=7+len(kemenangan)-1
              print('total gold sekarang= ',gold)
    
            elif 10<=gold<20:
              print('mendapatkan 9 gold')
              gold+=9+len(kemenangan)-1
              print('total gold sekarang= ',gold)
    
            elif gold>=20:
              print('mendapatkan 11 gold')
              gold+=11+len(kemenangan)-1
              print('total gold sekarang= ',gold)


        elif kondisi=='kalah':
            print('kalah')
            if gold<10:
              print('mendapatkan 5 gold')
              gold+=5
              print('total gold sekarang= ',gold)
            elif 10<=gold<20:
              print('mendapatkan 7 gold')
              gold+=7
              print('total gold sekarang= ',gold)
    
            elif gold>=20:
              print('mendapatkan 11 gold')
              gold+=11
              print('total gold sekarang= ',gold)

            if sinergiscavengger==2:
                        heroacak=random.choice(list(herostore))
                        print('hero acak dari scavenger=',heroacak)
                        indx=herostore.index(heroacak)
                        heroyangdipunya.append(heroacak)
                        print(heroyangdipunya)
                        
                        
                
            if sinergiscavengger==3:
                        heroacak=random.choice(list(herostore))
                        print('hero acak dari scavenger=',heroacak)
        

    
    
                
    
    