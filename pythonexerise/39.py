#data_dict={
#    'pan':'ervanza',
#    'der':'derian',
#    'lon':'marlon'
#}
#
#panjangdata=len(data_dict)
#print(panjangdata)
#
#key='der'
#data= key in data_dict
#print(data)
#key='jul'
#data= key in data_dict
#print(data)
#
#data_dict['pan']='ervanza radithya'
#print(data_dict)
#
#data_dict['jek']='zhaki'
#print(data_dict)
#
#data_dict.update({'pan':'ervanza'})
#print(data_dict)
#
#data_dict.update({'rel':'farrel'})
#print(data_dict)
#
#del data_dict['pan']
#print(data_dict)



datadict={
    'kur':'dimas',
    'jul':'ervanza',
    'king':'marlon'
}


panjang=len(datadict)
print(panjang)

print(datadict['jul'])

key='kur'
data=key in datadict
print(data)

datadict['king']='marlon sianturi'
print(datadict)

datadict['dep']='depara'
print(datadict)

datadict.update({'king':'marlon'})
print(datadict)

datadict.update({'tan':'nathan'})
print(datadict)

del datadict['jul']
print(datadict)