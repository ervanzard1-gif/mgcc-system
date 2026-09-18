data1=[1,2]
data2=[3,4]
datag=[data1,data2]
print(datag)

people1=['mariadi',44,'laki-laki']
people2=['suryadi',39,'laki-laki']
people3=['amerta',40,'perempuan']

people_list=[people1,people2,people3]

for people in people_list:
    print(f'nama\t={people[0]}')
    print(f'umur\t={people[1]}')
    print(f'gender\t={people[2]}\n')


print('\n\n\n\n\n\n\n\n\n\n\n')

x=['epan','mgcc','gunadarma']
y=['raijar','hsr','upvnj']
z=['iqbal','roblox','sebelas maret']

listpeserta=[x,y,z]

for peserta in listpeserta:
    print('nama=',peserta[0])
    print('game=',peserta[1])
    print('univ=',peserta[2],'\n')


listbaru=listpeserta.copy()
print(listpeserta)
print(listbaru)

#listpeserta[0]='wokwok'

#print(listpeserta)
#print(listbaru)

x[0]='wokwok'

print(listpeserta)
print(listbaru)


#gunakan deepcopy untuk nyalin sampai dalam

#list
p1=['china goverment scholarship','china','non-bologna']
p2=['stipendium hungaricum','hungary','bologna']
p3=['icpc','taiwan','non-bologna']
p4=['arice','romania','bologna']
p5=['mfa','romania','bologna']

beasiswap=[p1,p2,p3,p4,p5,'this is my dream next year']

for beasiswa in beasiswap:
    print(f'nama beasiswa\t\t=',beasiswa[0])
    print(f'negara\t\t\t=',beasiswa[1])
    print(f'status bologna eropa\t=',beasiswa[2],'\n')


beasiswab=beasiswap.copy()
print(beasiswap)
print(beasiswab)

p1[0]='cgs'
print(beasiswap)
print(beasiswab)

beasiswap[5]='aamin'
print(beasiswap)
print(beasiswab)