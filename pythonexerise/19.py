#width and alignment

data_nama='Ervanza Radithya Djani'
data_umur=18
data_universitas='Gunadarma University'
data_jurusan="informatika"
data_nilai=97.456

data_identitas=f'nama = {data_nama} \numur = {data_umur} \nuniversitas = {data_universitas} \njurusan = {data_jurusan}'

print(data_identitas)


print(5*'='+'...'+5*'=')
data_x="""
nama        = Ervanza Radithya Djani
umur        = 18
universitas = Gunadarma University
jurusan     = informatika"""
print(data_x)


print(5*'='+'...'+5*'=')
data_x=f"""
nama        = {data_nama:<3}
umur        = {data_umur}
universitas = {data_universitas}
jurusan     = {data_jurusan} 
nilai       = {data_nilai:.2f}
"""
print(data_x)

print(10*'='+'tugas'+'='*10)
x=''' 
Nama     Tugas     Nilai
------------------------
Andi       16       90
Budi       17       85
Citra      16       95
'''
print(x)

a= 'Ervanza'
b= '18'
c= 'depok'

print('====================================')
x=f''' 
Nama ={a:>8}
Umur ={b:>3}
Kota ={c:>6}
'''
print(x)

x='melinda enoki'
y='universitas indonesia'
z='kimia'

x=f"""
nama    ={x:>15}
college ={y:>23}
major   ={z:>7}
"""
print(x)