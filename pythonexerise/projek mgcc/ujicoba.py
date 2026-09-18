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
gold1={'yin sun-shin','vale','phoveus','dyrroth','uranus','cici','minotour','eudora'}
gold2={'angela','balmond','bellerick','granger','miya','zhuxin','martis','harley','natalia','luo yi','hylos'}
gold3={'franco','clint','aldous','paquito','hilda','wanwan','edith','karina','tigreal','saber','mathilda','kadita'}
gold4={'karrie','lunox','gusion','yin','lolita','irithel','zilong','suyou','sora','gord','vexana','atlas'}
gold5={'lancelot','badang','thamuz','melissa','nana','baxia','odette','fanny','alice'}
gold1bintang2 = {
    'yin sun-shin★2',
    'vale★2',
    'phoveus★2',
    'dyrroth★2',
    'uranus★2',
    'cici★2',
    'minotour★2',
    'eudora★2'
    }

gold2bintang2 = {
    'angela★2',
    'balmond★2',
    'bellerick★2',
    'granger★2',
    'miya★2',
    'zhuxin★2',
    'martis★2',
    'harley★2',
    'natalia★2',
    'luo yi★2',
    'hylos★2'
    }

gold3bintang2 = {
    'franco★2',
    'clint★2',
    'aldous★2',
    'paquito★2',
    'hilda★2',
    'wanwan★2',
    'edith★2',
    'karina★2',
    'tigreal★2',
    'saber★2',
    'mathilda★2',
    'kadita★2'
    }

gold4bintang2 = {
    'karrie★2',
    'lunox★2',
    'gusion★2',
    'yin★2',
    'lolita★2',
    'irithel★2',
    'zilong★2',
    'suyou★2',
    'sora★2',
    'gord★2',
    'vexana★2',
    'atlas★2'
    }

gold5bintang2 = {
    'lancelot★2',
    'badang★2',
    'thamuz★2',
    'melissa★2',
    'nana★2',
    'baxia★2',
    'odette★2',
    'fanny★2',
    'alice★2'
    }
gold7={'alpha'}

gold7bintang2 = {
    'alpha★2'
    }
heroechomancer={'moskov','gatotkaca','x.borg'}

rolecrystal={'swiftblade','bruiser','dauntless','defender','marksman','weapon master','stargazer','mage'}
crystalfiction={'kishin','dragoncaller','dragonaltar','zodiac','spectre','echomancer','starballe'}
storemistbender={'gold4 hero','gold 15','gold3bintang2','7 gold','clone','role crystal','crystal fiction'}
storemistbender2={'gold4 hero','gold 15','gold3bintang2','7 gold','clone','role crystal','crystal fiction'}


#print(tuple(kishin & bruiser))
heroprotagonis={'atlas','vexana'}
gold=2
protagonis=random.choice(('atlas','vexana'))
print(f'protagonis pada game ini adalah={protagonis}')


heroyangdipunya=[random.choice(list(gold1)),random.choice(list(gold1)),random.choice(list(gold2))]
print(heroyangdipunya)
equipment=[]

def nama_hero(hero):
    return hero.replace("★2", "").replace("★3", "")
kemenangan=[]
stackechomancer=0
stackenchanted_tales=0
stackmistbender=0

granger_sudah=False
paquito_sudah=False
gord_sudah=False
alice_sudah=False
alpha_sudah=False
heropilihanechomancer=random.choice(list(heroechomancer))
bintang_1_echomancer=False
bintang_2_echomancer=False
bintang_3_echomancer=False

storemistbenderpilihan=random.choice(list(storemistbender))
storemistbenderpilihan2=random.choice(list(storemistbender2))
pilihmistbenderstack=['nana',storemistbenderpilihan,storemistbenderpilihan2]

sinergikishin_bonus=0
sinergistarballe_bonus=0
sinergispectre_bonus=0
sinergiechomancer_bonus=0
sinergidragoncaller_bonus=0
sinergidragonaltar_bonus=0
sinergizodiac_bonus=0
sinergibruiser_bonus=0
sinergimarksman_bonus=0
sinergidefender_bonus=0
sinergidauntless_bonus=0
sinergistargazer_bonus=0
sinergiswiftblade_bonus=0
sinergiweapon_master_bonus=0
sinergimage_bonus=0

stack_et_30=False
stack_et_60=False
stack_et_100=False
stack_et_150=False

refresgratissetelahmatch=False
while True:
    menu=input('pilih menu= ')
    sinergimistbender=0
    sinergienchanted_tales=0
    sinergiscavengger=0
    sinergiechomancer=0
    datahero0=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero1=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero2=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero3=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    datahero4=random.choice(list(kishin)+list(dragoncaller)+list(bruiser)+list(dauntless)+list(marksman)+list(starballe)+list(weapon_master)+list(zodiac)+list(scavengger)+list(echomancer)+list(defender)+list(shadeweaver)+list(phasewarper)+list(stargazer)+list(dragonaltar)+list(mage)+list(swiftblade)+list(enchanted_tales)+list(mistbender)+list(spectre)+list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
    herostore=[datahero0,datahero1,datahero2,datahero3,datahero4]
    if menu=='store':
            while not refresgratissetelahmatch:
                    print(herostore)
                    ambil=input('apakah anda ingin mengambil hero? (y/n) : ')
                    if ambil=='y':
                        kode=input('masukkan kode hero yang ingin diambil (1-5) : ')
                        hero=herostore[(int(kode)-1)]
                        if hero in gold1 and gold>=1:
                            gold-=1
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)

                        elif hero in gold2 and gold>=2:
                            gold-=2
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)
                            
                        elif hero in gold3 and gold>=3:
                            gold-=3
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)
                            
                        elif hero in gold4 and gold>=4:
                            gold-=4
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)
                            
                        elif hero in gold5 and gold>=5:
                            gold-=5
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)

                        elif hero in gold7 and gold>=7:
                            gold-=7
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)

                        else:print('gold tidak cukup')
                

                        if None in heroyangdipunya:
                           data=heroyangdipunya.index(None)
                           del heroyangdipunya[data]
                        print(heroyangdipunya)


                        alpha=heroyangdipunya.count('alpha')
                        if alpha==4:
                            print('alpha 1 star ---> alpha 2 star')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.append(f'alpha{chr(9733)}2')
                            print(heroyangdipunya)

                        alpha2=heroyangdipunya.count(f'franco{chr(9733)}2')
                        if alpha2==4:
                            print('alpha 2 star ---> alpha 3 star')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.append(f'alpha{chr(9733)}3')
                            print(heroyangdipunya)

                        def upgrade_hero():
                            semua_hero = gold1 | gold2 | gold3 | gold4 | gold5
                        
                            for hero in semua_hero:
                        
                                # ★1 -> ★2
                                while heroyangdipunya.count(hero) >= 3:
                                    print(f'{hero} ★1 ---> {hero} ★2')
                        
                                    heroyangdipunya.remove(hero)
                                    heroyangdipunya.remove(hero)
                                    heroyangdipunya.remove(hero)
                        
                                    heroyangdipunya.append(f'{hero}{chr(9733)}2')
                                    print(heroyangdipunya)
                                # ★2 -> ★3
                                while heroyangdipunya.count(f'{hero}{chr(9733)}2') >= 3:
                                    print(f'{hero} ★2 ---> {hero} ★3')
                        
                                    heroyangdipunya.remove(f'{hero}{chr(9733)}2')
                                    heroyangdipunya.remove(f'{hero}{chr(9733)}2')
                                    heroyangdipunya.remove(f'{hero}{chr(9733)}2')

                                    heroyangdipunya.append(f'{hero}{chr(9733)}3')
                                    print(heroyangdipunya)


                        upgrade_hero()

   


    


                            

                            
                        
            
                        sinergikishin=0
                        sinergibruiser=0
                        sinergidragoncaller=0
                        sinergidauntless=0
                        sinergimarksman=0
                        sinergistarballe=0
                        sinergiweapon_master=0
                        sinergizodiac=0
                        sinergiphasewarper=0
                        sinergidragonaltar=0
                        sinergiswiftblade=0
                        sinergispectre=0
                        sinergishadeweaver=0
                        sinergidefender=0
                        sinergistargazer=0
                        sinergimage=0
            
            
            
                        sinergibruiser+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(bruiser))+sinergibruiser_bonus
                        if 0<sinergibruiser<=1:
                            print('sinergi bruiser anda adalah :',sinergibruiser)
                        elif 2<=sinergibruiser<4:
                            print(f'sinergi bruiser anda adalah :\x1b[31m  {sinergibruiser}  \x1b[0m')
                        elif 4<=sinergibruiser<6:
                            print(f'sinergi bruiser anda adalah :\x1b[34m  {sinergibruiser}  \x1b[0m')
                        elif sinergibruiser>=6:
                            print(f'sinergi bruiser anda adalah :\x1b[35m  {sinergibruiser}  \x1b[0m')
            
            
                        
                        sinergikishin+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(kishin))+sinergikishin_bonus
                        if 0<sinergikishin<=1:
                            print('sinergi kishin anda adalah :',sinergikishin)
                        elif 2<=sinergikishin<4:
                            print(f'sinergi kishin anda adalah :\x1b[31m  {sinergikishin}  \x1b[0m')
                        elif 4<=sinergikishin<6:
                            print(f'sinergi kishin anda adalah :\x1b[34m  {sinergikishin}  \x1b[0m')
                        elif sinergikishin>=6:
                            print(f'sinergi kishin anda adalah :\x1b[35m  {sinergikishin}  \x1b[0m')
                        
                        sinergidragoncaller+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(dragoncaller))+sinergidragoncaller_bonus
                        if 0<sinergidragoncaller<=1:
                            print('sinergi dragoncaller anda adalah :',sinergidragoncaller)
                        elif 2<=sinergidragoncaller<4:
                            print(f'sinergi dragoncaller anda adalah :\x1b[31m  {sinergidragoncaller}  \x1b[0m')
                        elif 4<=sinergidragoncaller<6:
                            print(f'sinergi dragoncaller anda adalah :\x1b[34m  {sinergidragoncaller}  \x1b[0m')
                        elif sinergidragoncaller>=6:
                            print(f'sinergi dragoncaller anda adalah :\x1b[35m  {sinergidragoncaller}  \x1b[0m')
            
                        sinergidauntless+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(dauntless))+sinergidauntless_bonus
                        if 0<sinergidauntless<=1:
                            print('sinergi dauntless anda adalah :',sinergidauntless)
                        elif 2<=sinergidauntless<4:
                            print(f'sinergi dauntless anda adalah :\x1b[31m  {sinergidauntless}  \x1b[0m')
                        elif 4<=sinergidauntless<6:
                            print(f'sinergi dauntless anda adalah :\x1b[34m  {sinergidauntless}  \x1b[0m')
                        elif sinergidauntless>=6:
                            print(f'sinergi dauntless anda adalah :\x1b[35m  {sinergidauntless}  \x1b[0m')
            
                        sinergimarksman+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(marksman))+sinergimarksman_bonus
                        if 0<sinergimarksman<=1:
                            print('sinergi marksman anda adalah :',sinergimarksman)
                        elif 2<=sinergimarksman<4:
                            print(f'sinergi marksman anda adalah :\x1b[31m  {sinergimarksman}  \x1b[0m')
                        elif 4<=sinergimarksman<6:
                            print(f'sinergi marksman anda adalah :\x1b[34m  {sinergimarksman}  \x1b[0m')
                        elif sinergimarksman>=6:
                            print(f'sinergi marksman anda adalah :\x1b[35m  {sinergimarksman}  \x1b[0m')
            
                        sinergistarballe+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(starballe))+sinergistarballe_bonus
                        if 0<sinergistarballe<=1:
                            print('sinergi starballe anda adalah :',sinergistarballe)
                        elif 2<=sinergistarballe<4:
                            print(f'sinergi starballe anda adalah :\x1b[31m  {sinergistarballe}  \x1b[0m')
                            print(f' anda mendapatkan stickballe dengan sinergi :\x1b[33m {1} \x1b[0m')
                        elif 4<=sinergistarballe<6:
                            print(f'sinergi starballe anda adalah :\x1b[34m  {sinergistarballe}  \x1b[0m')
                        elif sinergistarballe>=6:
                            print(f'sinergi starballe anda adalah :\x1b[35m  {sinergistarballe}  \x1b[0m')
            
                        sinergiweapon_master+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(weapon_master))+sinergiweapon_master_bonus
                        if 0<sinergiweapon_master<=1:
                            print('sinergi weapon master anda adalah :',sinergiweapon_master)
                        elif 2<=sinergiweapon_master<4:
                            print(f'sinergi weapon_master anda adalah :\x1b[31m  {sinergiweapon_master}  \x1b[0m')
                        elif 4<=sinergiweapon_master<6:
                            print(f'sinergi weapon_master anda adalah :\x1b[34m  {sinergiweapon_master}  \x1b[0m')
                        elif sinergiweapon_master>=6:
                            print(f'sinergi weapon_master anda adalah :\x1b[35m  {sinergiweapon_master}  \x1b[0m')
            
                        sinergizodiac+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(zodiac))+sinergizodiac_bonus
                        if 0<sinergizodiac<=1:
                            print('sinergi zodiac anda adalah :',sinergizodiac)
                        elif 2<=sinergizodiac<4:
                            print(f'sinergi zodiac anda adalah :\x1b[31m  {sinergizodiac}  \x1b[0m')
                        elif 4<=sinergizodiac<6:
                            print(f'sinergi zodiac anda adalah :\x1b[34m  {sinergizodiac}  \x1b[0m')
                        elif sinergizodiac>=6:
                            print(f'sinergi zodiac anda adalah :\x1b[35m  {sinergizodiac}  \x1b[0m')
            
                        sinergimage+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(mage))+sinergimage_bonus
                        if 0<sinergimage<=1:
                            print('sinergi mage anda adalah :',sinergimage)
                        elif 2<=sinergimage<4:
                            print(f'sinergi mage anda adalah :\x1b[31m  {sinergimage}  \x1b[0m')
                        elif 4<=sinergimage<6:
                            print(f'sinergi mage anda adalah :\x1b[34m  {sinergimage}  \x1b[0m')
                        elif sinergimage>=6:
                            print(f'sinergi mage anda adalah :\x1b[35m  {sinergimage}  \x1b[0m')
            
                        sinergiswiftblade+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(swiftblade))+sinergiswiftblade_bonus
                        if 0<sinergiswiftblade<=1:
                            print('sinergi swiftblade anda adalah :',sinergiswiftblade)
                        elif 2<=sinergiswiftblade<4:
                            print(f'sinergi swiftblade anda adalah :\x1b[31m  {sinergiswiftblade}  \x1b[0m')
                        elif 4<=sinergiswiftblade<6:
                            print(f'sinergi swiftblade anda adalah :\x1b[34m  {sinergiswiftblade}  \x1b[0m')
                        elif sinergiswiftblade>=6:
                            print(f'sinergi swiftblade anda adalah :\x1b[35m  {sinergiswiftblade}  \x1b[0m')
            
                        sinergistargazer+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(stargazer))+sinergistargazer_bonus
                        if 0<sinergistargazer<=1:
                            print('sinergi stargazer anda adalah :',sinergistargazer)
                        elif 2<=sinergistargazer<4:
                            print(f'sinergi stargazer anda adalah :\x1b[31m  {sinergistargazer}  \x1b[0m')
                        elif 4<=sinergistargazer<6:
                            print(f'sinergi stargazer anda adalah :\x1b[34m  {sinergistargazer}  \x1b[0m')
                        elif sinergistargazer>=6:
                            print(f'sinergi stargazer anda adalah :\x1b[35m  {sinergistargazer}  \x1b[0m')



            
                        sinergispectre+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(spectre))+sinergispectre_bonus
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
                            spectre.add('alpha')
                        
                        
                        


                        
            
                        sinergidefender+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(defender))+sinergidefender_bonus
                        if 0<sinergidefender<=1:
                            print('sinergi defender anda adalah :',sinergidefender)
                        elif 2<=sinergidefender<4:
                            print(f'sinergi defender anda adalah :\x1b[31m  {sinergidefender}  \x1b[0m')
                        elif 4<=sinergidefender<6:
                            print(f'sinergi defender anda adalah :\x1b[34m  {sinergidefender}  \x1b[0m')
                        elif sinergidefender>=6:
                            print(f'sinergi defender anda adalah :\x1b[35m  {sinergidefender}  \x1b[0m')



            
                        sinergiechomancer+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(echomancer))+sinergiechomancer_bonus
                        if 0<sinergiechomancer<=1:
                            print('sinergi echomancer anda adalah :',sinergiechomancer)
                        elif 2<=sinergiechomancer<4:
                            print(f'sinergi echomancer anda adalah :\x1b[31m  {sinergiechomancer}  \x1b[0m')
                            print(f'stack echomancer terbuka dengan hero {heropilihanechomancer}')
                        elif 4<=sinergiechomancer<6:
                            print(f'sinergi echomancer anda adalah :\x1b[34m  {sinergiechomancer}  \x1b[0m')
                        elif sinergiechomancer>=6:
                            print(f'sinergi echomancer anda adalah :\x1b[35m  {sinergiechomancer}  \x1b[0m')

            
                        sinergidragonaltar+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(dragonaltar))+sinergidragonaltar_bonus
                        if 0<sinergidragonaltar<=1:
                            print('sinergi dragonaltar anda adalah :',sinergidragonaltar)
                        elif 2<=sinergidragonaltar<4:
                            print(f'sinergi dragonaltar anda adalah :\x1b[31m  {sinergidragonaltar}  \x1b[0m')
                        elif 4<=sinergidragonaltar<6:
                            print(f'sinergi dragonaltar anda adalah :\x1b[34m  {sinergidragonaltar}  \x1b[0m')
                        elif sinergidragonaltar>=6:
                            print(f'sinergi dragonaltar anda adalah :\x1b[35m  {sinergidragonaltar}  \x1b[0m')
            
                        sinergienchanted_tales+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(enchanted_tales))
                        if 0<sinergienchanted_tales<=1:
                            print('sinergi enchanted_tales anda adalah :',sinergienchanted_tales)
                        elif 2<=sinergienchanted_tales<4:
                            print(f'sinergi enchanted_tales anda adalah :\x1b[36m  {sinergienchanted_tales}  \x1b[0m')
                        elif sinergienchanted_tales==4:
                            print(f'sinergi enchanted_tales anda adalah :\x1b[32m  {sinergienchanted_tales}  \x1b[0m')
                            
                        sinergishadeweaver+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(shadeweaver))
                        if 0<sinergishadeweaver<=1:
                            print('sinergi shadeweaver anda adalah :',sinergishadeweaver)
                        elif 2<=sinergishadeweaver<3:
                            print(f'sinergi shadeweaver anda adalah :\x1b[36m  {sinergishadeweaver}  \x1b[0m')
                        elif sinergishadeweaver==3:
                            print(f'sinergi shadeweaver anda adalah :\x1b[32m  {sinergishadeweaver}  \x1b[0m')
            
                        sinergiphasewarper+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(phasewarper))
                        if 0<sinergiphasewarper<=1:
                            print('sinergi phasewarper anda adalah :',sinergiphasewarper)
                        elif 2<=sinergiphasewarper<4:
                            print(f'sinergi phasewarper anda adalah :\x1b[36m  {sinergiphasewarper}  \x1b[0m')
                        elif sinergiphasewarper==4:
                            print(f'sinergi phasewarper anda adalah :\x1b[32m  {sinergiphasewarper}  \x1b[0m')
            
                        sinergimistbender+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(mistbender))
                        if sinergimistbender==1:
                            print(f'sinergi mistbender anda adalah :\x1b[33m {sinergimistbender} \x1b[0m')
                        elif sinergimistbender==2:
                            print(f'sinergi mistbender anda adalah :\x1b[36m  {sinergimistbender}  \x1b[0m')
                        elif sinergimistbender==3:
                            print(f'sinergi mistbender anda adalah :\x1b[32m  {sinergimistbender}  \x1b[0m')
                    
                        sinergiscavengger+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(scavengger))
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
                        break
                    elif ambil=='n':
                        print('refresh hero store')
                        break 
            
            

            while refresgratissetelahmatch and gold>=2:
                    gold-=2
                    print('sisa gold',gold)
                    print(herostore)
                    ambil=input('apakah anda ingin mengambil hero? (y/n) : ')
                    if ambil=='y':
                        kode=input('masukkan kode hero yang ingin diambil (1-5) : ')
                        hero=herostore[(int(kode)-1)]
                        if hero in gold1:
                            gold-=1
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)

                        elif hero in gold2:
                            gold-=2
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)
                            
                        elif hero in gold3:
                            gold-=3
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)
                            
                        elif hero in gold4:
                            gold-=4
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)
                            
                        elif hero in gold5:
                            gold-=5
                            herostore[int(kode)-1]=None
                            print('sisa gold=',gold)
                            heroyangdipunya.append(hero)
                

                        if None in heroyangdipunya:
                           data=heroyangdipunya.index(None)
                           del heroyangdipunya[data]
                        print(heroyangdipunya)


                        alpha=heroyangdipunya.count('alpha')
                        if alpha==4:
                            print('alpha 1 star ---> alpha 2 star')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.remove('alpha')
                            heroyangdipunya.append(f'alpha{chr(9733)}2')
                            print(heroyangdipunya)

                        alpha2=heroyangdipunya.count(f'alpha{chr(9733)}2')
                        if alpha2==4:
                            print('alpha 2 star ---> alpha 3 star')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.remove(f'alpha{chr(9733)}2')
                            heroyangdipunya.append(f'alpha{chr(9733)}3')
                            print(heroyangdipunya)

                        def upgrade_hero():
                            semua_hero = gold1 | gold2 | gold3 | gold4 | gold5
                        
                            for hero in semua_hero:
                        
                                # ★1 -> ★2
                                while heroyangdipunya.count(hero) == 3:
                                    print(f'{hero} ★1 ---> {hero} ★2')
                        
                                    heroyangdipunya.remove(hero)
                                    heroyangdipunya.remove(hero)
                                    heroyangdipunya.remove(hero)
                        
                                    heroyangdipunya.append(f'{hero}{chr(9733)}2')
                                # ★2 -> ★3
                                while heroyangdipunya.count(f'{hero}{chr(9733)}2') == 3:
                                    print(f'{hero} ★2 ---> {hero} ★3')
                        
                                    heroyangdipunya.remove(f'{hero}{chr(9733)}2')
                                    heroyangdipunya.remove(f'{hero}{chr(9733)}2')
                                    heroyangdipunya.remove(f'{hero}{chr(9733)}2')

                                    heroyangdipunya.append(f'{hero}{chr(9733)}3')


                        upgrade_hero()
                                                
                                                
            
                        sinergikishin=0
                        sinergibruiser=0
                        sinergidragoncaller=0
                        sinergidauntless=0
                        sinergimarksman=0
                        sinergistarballe=0
                        sinergiweapon_master=0
                        sinergizodiac=0
                        sinergiphasewarper=0
                        sinergidragonaltar=0
                        sinergiswiftblade=0
                        sinergispectre=0
                        sinergishadeweaver=0
                        sinergidefender=0
                        sinergistargazer=0
                        sinergimage=0
            
            
            
                        sinergibruiser+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(bruiser))+sinergibruiser_bonus
                        if 0<sinergibruiser<=1:
                            print('sinergi bruiser anda adalah :',sinergibruiser)
                        elif 2<=sinergibruiser<4:
                            print(f'sinergi bruiser anda adalah :\x1b[31m  {sinergibruiser}  \x1b[0m')
                        elif 4<=sinergibruiser<6:
                            print(f'sinergi bruiser anda adalah :\x1b[34m  {sinergibruiser}  \x1b[0m')
                        elif sinergibruiser>=6:
                            print(f'sinergi bruiser anda adalah :\x1b[35m  {sinergibruiser}  \x1b[0m')
            
            
                        
                        sinergikishin+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(kishin))+sinergikishin_bonus
                        if 0<sinergikishin<=1:
                            print('sinergi kishin anda adalah :',sinergikishin)
                        elif 2<=sinergikishin<4:
                            print(f'sinergi kishin anda adalah :\x1b[31m  {sinergikishin}  \x1b[0m')
                        elif 4<=sinergikishin<6:
                            print(f'sinergi kishin anda adalah :\x1b[34m  {sinergikishin}  \x1b[0m')
                        elif sinergikishin>=6:
                            print(f'sinergi kishin anda adalah :\x1b[35m  {sinergikishin}  \x1b[0m')
                        
                        sinergidragoncaller+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(dragoncaller))+sinergidragoncaller_bonus
                        if 0<sinergidragoncaller<=1:
                            print('sinergi dragoncaller anda adalah :',sinergidragoncaller)
                        elif 2<=sinergidragoncaller<4:
                            print(f'sinergi dragoncaller anda adalah :\x1b[31m  {sinergidragoncaller}  \x1b[0m')
                        elif 4<=sinergidragoncaller<6:
                            print(f'sinergi dragoncaller anda adalah :\x1b[34m  {sinergidragoncaller}  \x1b[0m')
                        elif sinergidragoncaller>=6:
                            print(f'sinergi dragoncaller anda adalah :\x1b[35m  {sinergidragoncaller}  \x1b[0m')
            
                        sinergidauntless+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(dauntless))+sinergidauntless_bonus
                        if 0<sinergidauntless<=1:
                            print('sinergi dauntless anda adalah :',sinergidauntless)
                        elif 2<=sinergidauntless<4:
                            print(f'sinergi dauntless anda adalah :\x1b[31m  {sinergidauntless}  \x1b[0m')
                        elif 4<=sinergidauntless<6:
                            print(f'sinergi dauntless anda adalah :\x1b[34m  {sinergidauntless}  \x1b[0m')
                        elif sinergidauntless>=6:
                            print(f'sinergi dauntless anda adalah :\x1b[35m  {sinergidauntless}  \x1b[0m')
            
                        sinergimarksman+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(marksman))+sinergimarksman_bonus
                        if 0<sinergimarksman<=1:
                            print('sinergi marksman anda adalah :',sinergimarksman)
                        elif 2<=sinergimarksman<4:
                            print(f'sinergi marksman anda adalah :\x1b[31m  {sinergimarksman}  \x1b[0m')
                        elif 4<=sinergimarksman<6:
                            print(f'sinergi marksman anda adalah :\x1b[34m  {sinergimarksman}  \x1b[0m')
                        elif sinergimarksman>=6:
                            print(f'sinergi marksman anda adalah :\x1b[35m  {sinergimarksman}  \x1b[0m')
            
                        sinergistarballe+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(starballe))+sinergistarballe_bonus
                        if 0<sinergistarballe<=1:
                            print('sinergi starballe anda adalah :',sinergistarballe)
                        elif 2<=sinergistarballe<4:
                            print(f'sinergi starballe anda adalah :\x1b[31m  {sinergistarballe}  \x1b[0m')
                            print(f' anda mendapatkan stickballe dengan sinergi :\x1b[33m {1} \x1b[0m')
                        elif 4<=sinergistarballe<6:
                            print(f'sinergi starballe anda adalah :\x1b[34m  {sinergistarballe}  \x1b[0m')
                        elif sinergistarballe>=6:
                            print(f'sinergi starballe anda adalah :\x1b[35m  {sinergistarballe}  \x1b[0m')
            
                        sinergiweapon_master+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(weapon_master))+sinergiweapon_master_bonus
                        if 0<sinergiweapon_master<=1:
                            print('sinergi weapon master anda adalah :',sinergiweapon_master)
                        elif 2<=sinergiweapon_master<4:
                            print(f'sinergi weapon_master anda adalah :\x1b[31m  {sinergiweapon_master}  \x1b[0m')
                        elif 4<=sinergiweapon_master<6:
                            print(f'sinergi weapon_master anda adalah :\x1b[34m  {sinergiweapon_master}  \x1b[0m')
                        elif sinergiweapon_master>=6:
                            print(f'sinergi weapon_master anda adalah :\x1b[35m  {sinergiweapon_master}  \x1b[0m')
            
                        sinergizodiac+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(zodiac))+sinergizodiac_bonus
                        if 0<sinergizodiac<=1:
                            print('sinergi zodiac anda adalah :',sinergizodiac)
                        elif 2<=sinergizodiac<4:
                            print(f'sinergi zodiac anda adalah :\x1b[31m  {sinergizodiac}  \x1b[0m')
                        elif 4<=sinergizodiac<6:
                            print(f'sinergi zodiac anda adalah :\x1b[34m  {sinergizodiac}  \x1b[0m')
                        elif sinergizodiac>=6:
                            print(f'sinergi zodiac anda adalah :\x1b[35m  {sinergizodiac}  \x1b[0m')
            
                        sinergimage+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(mage))+sinergimage_bonus
                        if 0<sinergimage<=1:
                            print('sinergi mage anda adalah :',sinergimage)
                        elif 2<=sinergimage<4:
                            print(f'sinergi mage anda adalah :\x1b[31m  {sinergimage}  \x1b[0m')
                        elif 4<=sinergimage<6:
                            print(f'sinergi mage anda adalah :\x1b[34m  {sinergimage}  \x1b[0m')
                        elif sinergimage>=6:
                            print(f'sinergi mage anda adalah :\x1b[35m  {sinergimage}  \x1b[0m')
            
                        sinergiswiftblade+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(swiftblade))+sinergiswiftblade_bonus
                        if 0<sinergiswiftblade<=1:
                            print('sinergi swiftblade anda adalah :',sinergiswiftblade)
                        elif 2<=sinergiswiftblade<4:
                            print(f'sinergi swiftblade anda adalah :\x1b[31m  {sinergiswiftblade}  \x1b[0m')
                        elif 4<=sinergiswiftblade<6:
                            print(f'sinergi swiftblade anda adalah :\x1b[34m  {sinergiswiftblade}  \x1b[0m')
                        elif sinergiswiftblade>=6:
                            print(f'sinergi swiftblade anda adalah :\x1b[35m  {sinergiswiftblade}  \x1b[0m')
            
                        sinergistargazer+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(stargazer))+sinergistargazer_bonus
                        if 0<sinergistargazer<=1:
                            print('sinergi stargazer anda adalah :',sinergistargazer)
                        elif 2<=sinergistargazer<4:
                            print(f'sinergi stargazer anda adalah :\x1b[31m  {sinergistargazer}  \x1b[0m')
                        elif 4<=sinergistargazer<6:
                            print(f'sinergi stargazer anda adalah :\x1b[34m  {sinergistargazer}  \x1b[0m')
                        elif sinergistargazer>=6:
                            print(f'sinergi stargazer anda adalah :\x1b[35m  {sinergistargazer}  \x1b[0m')



            
                        sinergispectre+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(spectre))+sinergispectre_bonus
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
                            spectre.add('alpha')
                        
                        
                        


                        
            
                        sinergidefender+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(defender))+sinergidefender_bonus
                        if 0<sinergidefender<=1:
                            print('sinergi defender anda adalah :',sinergidefender)
                        elif 2<=sinergidefender<4:
                            print(f'sinergi defender anda adalah :\x1b[31m  {sinergidefender}  \x1b[0m')
                        elif 4<=sinergidefender<6:
                            print(f'sinergi defender anda adalah :\x1b[34m  {sinergidefender}  \x1b[0m')
                        elif sinergidefender>=6:
                            print(f'sinergi defender anda adalah :\x1b[35m  {sinergidefender}  \x1b[0m')



            
                        sinergiechomancer+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(echomancer))+sinergiechomancer_bonus
                        if 0<sinergiechomancer<=1:
                            print('sinergi echomancer anda adalah :',sinergiechomancer)
                        elif 2<=sinergiechomancer<4:
                            print(f'sinergi echomancer anda adalah :\x1b[31m  {sinergiechomancer}  \x1b[0m')
                            print(f'stack echomancer terbuka dengan hero {heropilihanechomancer}')
                        elif 4<=sinergiechomancer<6:
                            print(f'sinergi echomancer anda adalah :\x1b[34m  {sinergiechomancer}  \x1b[0m')
                        elif sinergiechomancer>=6:
                            print(f'sinergi echomancer anda adalah :\x1b[35m  {sinergiechomancer}  \x1b[0m')

            
                        sinergidragonaltar+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(dragonaltar))+sinergidragonaltar_bonus
                        if 0<sinergidragonaltar<=1:
                            print('sinergi dragonaltar anda adalah :',sinergidragonaltar)
                        elif 2<=sinergidragonaltar<4:
                            print(f'sinergi dragonaltar anda adalah :\x1b[31m  {sinergidragonaltar}  \x1b[0m')
                        elif 4<=sinergidragonaltar<6:
                            print(f'sinergi dragonaltar anda adalah :\x1b[34m  {sinergidragonaltar}  \x1b[0m')
                        elif sinergidragonaltar>=6:
                            print(f'sinergi dragonaltar anda adalah :\x1b[35m  {sinergidragonaltar}  \x1b[0m')
            
                        sinergienchanted_tales+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(enchanted_tales))
                        if 0<sinergienchanted_tales<=1:
                            print('sinergi enchanted_tales anda adalah :',sinergienchanted_tales)
                        elif 2<=sinergienchanted_tales<4:
                            print(f'sinergi enchanted_tales anda adalah :\x1b[36m  {sinergienchanted_tales}  \x1b[0m')
                        elif sinergienchanted_tales==4:
                            print(f'sinergi enchanted_tales anda adalah :\x1b[32m  {sinergienchanted_tales}  \x1b[0m')
                            
                        sinergishadeweaver+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(shadeweaver))
                        if 0<sinergishadeweaver<=1:
                            print('sinergi shadeweaver anda adalah :',sinergishadeweaver)
                        elif 2<=sinergishadeweaver<3:
                            print(f'sinergi shadeweaver anda adalah :\x1b[36m  {sinergishadeweaver}  \x1b[0m')
                        elif sinergishadeweaver==3:
                            print(f'sinergi shadeweaver anda adalah :\x1b[32m  {sinergishadeweaver}  \x1b[0m')
            
                        sinergiphasewarper+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(phasewarper))
                        if 0<sinergiphasewarper<=1:
                            print('sinergi phasewarper anda adalah :',sinergiphasewarper)
                        elif 2<=sinergiphasewarper<4:
                            print(f'sinergi phasewarper anda adalah :\x1b[36m  {sinergiphasewarper}  \x1b[0m')
                        elif sinergiphasewarper==4:
                            print(f'sinergi phasewarper anda adalah :\x1b[32m  {sinergiphasewarper}  \x1b[0m')
            
                        sinergimistbender+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(mistbender))
                        if sinergimistbender==1:
                            print(f'sinergi mistbender anda adalah :\x1b[33m {sinergimistbender} \x1b[0m')
                        elif sinergimistbender==2:
                            print(f'sinergi mistbender anda adalah :\x1b[36m  {sinergimistbender}  \x1b[0m')
                        elif sinergimistbender==3:
                            print(f'sinergi mistbender anda adalah :\x1b[32m  {sinergimistbender}  \x1b[0m')
                    
                        sinergiscavengger+=1*len(set([nama_hero(hero) for hero in heroyangdipunya]).intersection(scavengger))
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
                        break
                    elif ambil=='n':
                        print('refresh hero store')
                        break 
            refresgratissetelahmatch=True
            while gold<2:
                print('gold tidak cukup untuk refresh store')
                break
            
            
    
    

        
    elif menu=='match'  :
        if len(heroyangdipunya)>=1:
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
    
                if sinergimistbender==1 and 'uranus' in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(3,5),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==1 and 'uranus' not in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(9,10),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==1 and 'uranus' not in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(6,8),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==2 and 'uranus' in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(12,14),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==2 and 'uranus' not in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(13,16),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==2 and 'uranus' in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(6,10),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==3:
                    stackmistbender=min(stackmistbender+random.randrange(9,20),99)
                    print('stack mistbender=',stackmistbender)
    
                if sinergienchanted_tales==2:
                    stackenchanted_tales=min(stackenchanted_tales+5,150)
    
                elif sinergienchanted_tales==4:
                    stackenchanted_tales=min(stackenchanted_tales+8,150)
    
                refresgratissetelahmatch=False
    
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
    
                if sinergimistbender==1 and 'uranus' in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(1,4),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==1 and 'uranus'  not in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(6,8),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==1 and 'uranus' not in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(4,6),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==2 and 'uranus' in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(7,10),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==2 and 'uranus' not in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(8,12),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==2 and 'uranus' in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(6,8),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==3 :
                    stackmistbender=min(stackmistbender+random.randrange(9,14),99)
                    print('stack mistbender=',stackmistbender)
    
                if sinergienchanted_tales==2:
                    stackenchanted_tales=min(stackenchanted_tales+3,150)
    
                elif sinergienchanted_tales==4:
                    stackenchanted_tales=min(stackenchanted_tales+5,150)
    
                refresgratissetelahmatch=False

        elif len(heroyangdipunya)==0:
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
    
                if sinergimistbender==1 and 'uranus' in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(1,4),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==1 and 'uranus'  not in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(6,8),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==1 and 'uranus' not in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(4,6),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==2 and 'uranus' in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' not in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(7,10),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==2 and 'uranus' not in heroyangdipunya and 'nana' in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(8,12),99)
                    print('stack mistbender=',stackmistbender)
                elif sinergimistbender==2 and 'uranus' in heroyangdipunya and 'nana' not in heroyangdipunya and 'aldous' in heroyangdipunya :
                    stackmistbender=min(stackmistbender+random.randrange(6,8),99)
                    print('stack mistbender=',stackmistbender)
    
                elif sinergimistbender==3 :
                    stackmistbender=min(stackmistbender+random.randrange(9,14),99)
                    print('stack mistbender=',stackmistbender)
    
                if sinergienchanted_tales==2:
                    stackenchanted_tales=min(stackenchanted_tales+3,150)
    
                elif sinergienchanted_tales==4:
                    stackenchanted_tales=min(stackenchanted_tales+5,150)
    
                refresgratissetelahmatch=False

        if sinergiscavengger==2:
                    heroacak=random.choice(list(gold1)+list(gold2))
                    print('hero acak dari scavenger=',heroacak)
                    heroyangdipunya.append(heroacak)
                    print(heroyangdipunya)
                              
            
        if sinergiscavengger==3:
                    heroacak=random.choice(list(gold1)+list(gold2)+list(gold3)+list(gold4)+list(gold5))
                    print('hero acak dari scavenger=',heroacak)
                    heroyangdipunya.append(heroacak)
                    print(heroyangdipunya)

        if 2<=sinergiechomancer<=3:
            stackechomancer=min(stackechomancer+10,999)
            print(f'stack echomancer={stackechomancer}')
        if 4<=sinergiechomancer<=5:
            stackechomancer=min(stackechomancer+25,999)
            print(f'stack echomancer={stackechomancer}')
        if sinergiechomancer==6:
            stackechomancer=min(stackechomancer+45,999)
            print(f'stack echomancer={stackechomancer}')


        

        if 100<=stackechomancer<300 and not bintang_1_echomancer :
            print(f'{heropilihanechomancer} ditambahkan')
            heroyangdipunya.append(heropilihanechomancer)
            print(heroyangdipunya)
            bintang_1_echomancer=True

        elif 300<=stackechomancer<999 and not bintang_2_echomancer:
            heropilihanechomancer2=f'{heropilihanechomancer}{chr(9733)}2'
            print(f'{heropilihanechomancer2} ditambahkan')
            heroyangdipunya.remove(heropilihanechomancer)
            heroyangdipunya.append(heropilihanechomancer2)
            print(heroyangdipunya)
            bintang_2_echomancer=True

        elif stackechomancer==999 and not bintang_3_echomancer:
            heropilihanechomancer3=f'{heropilihanechomancer}{chr(9733)}3'
            print(f'{heropilihanechomancer3} ditambahkan')
            heroyangdipunya.remove(heropilihanechomancer2)
            heroyangdipunya.append(heropilihanechomancer3)
            print(heroyangdipunya)
            bintang_3_echomancer=True


        if 30<=stackenchanted_tales<60 and not stack_et_30:
            print('mendapatkan 10 gold dan 2 hero 2 gold')
            gold+=10
            print('gold=',gold)
            hero1=random.choice(gold2)
            heroyangdipunya.append(hero1)
            hero2=random.choice(gold2)
            heroyangdipunya.append(hero2)
            print(heroyangdipunya)
            stack_et_30=True
            

        elif 60<=stackenchanted_tales<100 and not stack_et_60:
            print('mendapatakan vexana/atlas')
            acakprotagonis=random.choice(heroprotagonis)
            print('mendapatkan',acakprotagonis)
            heroyangdipunya.append(acakprotagonis)
            stack_et_60=True

        elif 100<=stackenchanted_tales<150 and not stack_et_100:
            print('mendapatkan 20 gold dan 1 hero 4 gold')
            gold+=20
            print('gold=',gold)
            hero=random.choice(gold4)
            heroyangdipunya.append(hero)
            print(heroyangdipunya)
            stack_et_100=True

        elif stackenchanted_tales==150 and not stack_et_150:
            print('mendapatkan 2 hero dengan kondisi protagonis')
            heroyangdipunya.append(protagonis)
            heroyangdipunya.append(protagonis)
            print(heroyangdipunya)
            stack_et_150=True
      
    elif menu=='mistbender' :
        print('open mistbender store')
        print(pilihmistbenderstack)

        data=input('ingin ambil?=')
        if data=='y':
            kode=int(input('masukan kode pilihan mistbender store='))
            if kode==1 and stackmistbender>=60:
                pilih=pilihmistbenderstack[kode-1]
                print('mendapatkan',pilih)
                herostore.append(pilih)
                pilihmistbenderstack[0]=None
                stackmistbender-=60
                print(stackmistbender)

            

            elif kode != 1:
                pilih2 = pilihmistbenderstack[kode - 1]
            
                if pilih2 == '7 gold' and stackmistbender>=35:
                    gold += 7
                    print('gold =', gold)
                    stackmistbender-=35
                    # GANTI SLOT YANG BARU SAJA DIAMBIL
                    pilihmistbenderstack[kode - 1] = random.choice(storemistbender)
    
                    print('store diperbarui',pilihmistbenderstack)
            
                elif pilih2 == 'gold 15' and stackmistbender>=70:
                    gold += 15
                    print('gold =', gold)
                    stackmistbender-=70
                    # GANTI SLOT YANG BARU SAJA DIAMBIL
                    pilihmistbenderstack[kode - 1] = random.choice(storemistbender)
    
                    print('store diperbarui',pilihmistbenderstack)
            
                elif pilih2 == 'clone' and stackmistbender>=80:
                    print('mendapatkan clone')
                    storemistbender.remove(pilih2)
                    equipment.append('clone')
                    stackmistbender-=80
                    # GANTI SLOT YANG BARU SAJA DIAMBIL
                    pilihmistbenderstack[kode - 1] = random.choice(storemistbender)
    
                    print('store diperbarui',pilihmistbenderstack)
            
                elif pilih2 == 'gold4 hero' and stackmistbender>=30:
                    print('mendapatkan', pilih2)
                    storemistbender.remove(pilih2)
                    storemistbender.append(random.choice(gold4))
                    heroyangdipunya.append(pilih2)
                    stackmistbender-=30
                    # GANTI SLOT YANG BARU SAJA DIAMBIL
                    pilihmistbenderstack[kode - 1] = random.choice(storemistbender)
    
                    print('store diperbarui',pilihmistbenderstack)
                    
            
                elif pilih2 == 'gold3bintang2' and stackmistbender>=45:
                    print('mendapatkan', pilih2)
                    storemistbender.remove(pilih2)
                    storemistbender.append(random.choice(gold3bintang2))
                    heroyangdipunya.append(pilih2)
                    stackmistbender-=45
                    pilihmistbenderstack[kode - 1] = random.choice(storemistbender)
                    print('store diperbarui',pilihmistbenderstack)


                elif pilih2 == 'crystal fiction' and stackmistbender>=90:
                    print('mendapatkan',pilih2)
                    storemistbender.remove(pilih2)
                    equipment.append(pilih2)
                    stackmistbender-=90
                    pilihmistbenderstack[kode - 1] = random.choice(storemistbender)
                    print('store diperbarui',pilihmistbenderstack)

                elif pilih2 == 'role crystal' and stackmistbender>=90:
                    print('mendapatkan',pilih2)
                    storemistbender.remove(pilih2)
                    equipment.append(pilih2)
                    stackmistbender-=90
                    


                    # GANTI SLOT YANG BARU SAJA DIAMBIL
                    pilihmistbenderstack[kode - 1] = random.choice(storemistbender)
                    print('store diperbarui',pilihmistbenderstack)

                else:print('stack mistbender tidak cukup')

            else:print('stack mistbender tidak cukup')



    elif menu=='equipment':
        print(equipment)
        keputusan=input('anda ingin menggunakan equipment?')
        if keputusan=='y':
            datapilihanequipment=int(input('masukan kode equipment'))
            dataequipment=equipment[datapilihanequipment-1]
            print(dataequipment)
    
            if dataequipment=='clone':
                print(heroyangdipunya)
                clonehero=int(input('masukan kode hero = '))
                herodiclone=heroyangdipunya[clonehero-1]
                if herodiclone in heroyangdipunya:
                    heroyangdipunya.append(herodiclone)
                    print(heroyangdipunya)
            elif dataequipment=='crystal fiction':
                cry=random.choice(crystalfiction)
                print('mendapatkan sinergi tambahan=',cry)
                if cry=='kishin':
                    sinergikishin_bonus+=1
                elif cry=='starballe':
                    sinergistarballe_bonus+=1
                elif cry=='dragoncaller':
                    sinergidragoncaller_bonus+=1
                elif cry=='dragonaltar':
                    sinergidragonaltar_bonus+=1
                elif cry=='zodiac':
                    sinergizodiac_bonus+=1
                elif cry=='echomancer':
                    sinergiechomancer_bonus+=1
                elif cry=='spectre':
                    sinergispectre_bonus+=1

            elif dataequipment=='role crystal':
                cry2=random.choice(rolecrystal)
                print('mendapatkan sinergi tambahan=',cry2)
                if cry2=='bruiser':
                    sinergibruiser_bonus+=1
                elif cry2=='marksman':
                    sinergimarksman_bonus+=1
                elif cry2=='defender':
                    sinergidefender_bonus+=1
                elif cry2=='dauntless':
                    sinergidauntless_bonus+=1
                elif cry2=='stargazer':
                    sinergistargazer_bonus+=1
                elif cry2=='swiftblade':
                    sinergiswiftblade_bonus+=1
                elif cry2=='mage':
                    sinergimage_bonus+=1
                elif cry2=='weapon master':
                    sinergiweapon_master_bonus+=1

    elif menu=='removehero':
        print(heroyangdipunya)
        kode=int(input('masukan kode hero yang ingin dibuang='))
        herodelete=heroyangdipunya[kode-1]
        heroyangdipunya.remove(herodelete)
        print(heroyangdipunya)


        

            
            
    



     
            


    

            

                
    
    