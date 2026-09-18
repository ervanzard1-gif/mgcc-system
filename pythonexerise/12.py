#membuat gabungan area rentang dari angka
#+++++++3-------10++++++++

inputuser = float(input('masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 ='))


iskurangdari=(inputuser<3)
print('kurang dari 3=',iskurangdari)

islebihdari=(inputuser>10)
print('lebih dari 10=',islebihdari)


iscorrect=iskurangdari or islebihdari
print('angka yang anda masukkan:',iscorrect)
print("===============")
#-------3+++++++10-------
inputuser=float(input('masukkan angka yang bernilai \ndiantara 3 sampai 10= '))

nilai=(3<inputuser<10)
print('angka yang dimasukkan=',nilai)



inputuser=float(input('masukan angka yang bernilai lebih dari 3 dan kurang dari 10 = '))

islebihdari=(inputuser>3)
print('lebih dari 10=', islebihdari)

iskurangdari=(inputuser<10)
print('kurang dari 10=',iskurangdari)

iscorrect= islebihdari and iskurangdari
print('angka yang dimasukkan=',iscorrect)
print("================")
#1.--------0++++++++5-------8++++++++11--------
inputuser=float(input('masukan angka yang berada diantara 0 sampai 5 dan 8 sampai 11= '))

islebihdari=(inputuser>0)
print('lebih dari 0=',islebihdari)

iskurangdari=(inputuser<5)
print('kurang dari 5= ',iskurangdari)

iscorrect= islebihdari and iskurangdari
print('angka yang dimasukan=',iscorrect)

islebihdari2=(inputuser>8)
print('lebih dari 8 = ', islebihdari2)

iskurangdari2=(inputuser<11)
print('kurang dari 11= ', iskurangdari)

iscorrect2= islebihdari and iskurangdari
print('angka yanh dimasukkan=', iscorrect2)


iscorrectfinal= iscorrect or iscorrect
print('keputusan final=', iscorrectfinal)

print('=================')
#2.++++++++0--------5+++++++8--------11++++++++
inputuser=float(input('masukan angka yang kurang dari 0 atau lebih dari 11 atau diantara 5 sampai 8= '))

islebihdari=(inputuser>5)
print('lebih dari 5= ',islebihdari)

iskurangdari=(inputuser<8)
print('kurang dari 8 = ', iskurangdari)

iscorrect= islebihdari and iskurangdari
print('angka yang dimasukan=',iscorrect)

iskurangdari2=(inputuser<0)
print('kurang dari 0=',iskurangdari2)

islebihdari2=(inputuser>11)
print('lebih dari 11= ', islebihdari2)

iscorrect2= islebihdari2 or iskurangdari2
print('angka yang dimasukkan=', iscorrect2)


iscorrectfinal= iscorrect or iscorrect2
print('keputusan final=', iscorrectfinal)



#3.+++++++++1--------4+++++++++7---------10++++++++++
inputuser=float(input('masukan angka yang kurang dari 1 atau berada diantara 4 sampai 7 atau lebih dari 10 : '))

iskurangdari=(inputuser<1)
print("kurang dari 1= ",iskurangdari )

islebihdari=(inputuser>10)
print('lebih dari 10= ',islebihdari)

iscorrect=islebihdari or iskurangdari
print('hasil= ',iscorrect)

islebihdari2=(inputuser>4)
print('lebih dari 4',islebihdari2)

iskurangdari2=(inputuser<7)
print('kurang dari 7', iskurangdari2)

iscorrect2=islebihdari2 and iskurangdari2
print('hasil2= ',iscorrect2)

keputusanfinal=iscorrect or iscorrect2
print('keputusan final= ',keputusanfinal)



#4.++++++7------12++++++15------20+++++++27-------

inputuser=float(input('masukan angka yanh kurang dari 7 atau diantara 12 sampai 15 atau diantara 20 sampai 27'))

iskurangdari=(inputuser<7)
print('kurang dari 7', iskurangdari)

islebihdari1=(inputuser>12)
print('lebih dari 12', islebihdari1)

iskurangdari1=(inputuser<15)
print('kurang dari 15',iskurangdari1)

iscorrect= islebihdari and iskurangdari1
print('keputusan', iscorrect)

islebihdari2=(inputuser>20)
print('lebih dari 20', islebihdari2)

iskurangdari2=(inputuser<27)
print('kurang dari 27', iskurangdari2)

iscorrect2= iskurangdari2 and islebihdari2
print('keputusan2', iscorrect2)

keputusanfinal1=iscorrect or iscorrect2 or iskurangdari
print('keputusan final', keputusanfinal1)
