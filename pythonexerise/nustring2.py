data={
    'van':'ervanza',
    'jar':'raijar',
    'ji':'panji',
    'syau':'maharaja aqil'
}
print(data)

#del data['van']
#print(data)

#data.clear()
#print(data)


data1=data.copy()
print(data1)
print(data)

data['ji']='i putu'
print(data1)
print(data)

data1['jar']='tian'
print(data1)
print(data)

from copy import deepcopy
data2=deepcopy(data)
print(data2)
print(data)

data['ji']='i putu'
print(data2)
print(data)


data=['nama','umur','pengalaman']
data1=dict.fromkeys(data,'belum diisi')
print(data1)

data1['nama']='ervanza'
print(data1)


data={
    'nama':'evan',
    'agama':'islam',
    'umur':19
}

print(data.get('fregr'))
print(data['nama'])

data7='nama' in data
print(data7)


data={
    'nama':'syauqi',
    'umur':18,
    'univ':'universitas indonesia',
    'major':'sastra japan',
    'hobi':'motoran'
}

data1=data.setdefault('tinggi',168)
print(data)
data1=data.setdefault('berat',44)
print(data)


data.setdefault('tinggi',168)
data.setdefault('berat',44)
print(data)

data1=data.setdefault('hobi','speeding')
print(data1)


data.update({'nama':'maharaja aqil','umur':'108','bangun':'jam 7'})
print(data1)


#data0=data.keys()
#print(data0)
#
#data9=data.values()
#print(data9)
#
#data7=data.items()
#print(data7)